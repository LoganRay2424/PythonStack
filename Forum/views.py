from django.shortcuts import render, redirect
from .models import *
import bcrypt


def index(request):
    return render(request, 'index.html')


def logout(request):
    request.session.clear()
    return redirect('/')


def register(request):
    errors = User.objects.validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    user_in_db = User.objects.filter(email=request.POST['email']).first()

    if user_in_db:
        messages.error(request, "Email already used.  Please Login")
        return redirect('/')

    hashed_password = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()).decode()

    new_user = User.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        email=request.POST['email'],
        password=hashed_password
    )

    request.session['user_id'] = new_user.id

    return redirect('/success')


def success(request):
    user_id = request.session.get('user_id')
    if user_id is None:
        messages.error(request, "Please log in or Register")
        return redirect('/')

    context = {
        "user": User.objects.get(id=user_id),
        "message": Message.objects.all()
    }
    return render(request, 'success.html', context)


def login2(request):
    return render(request, 'log_in.html')


def login(request):
    found_user = User.objects.filter(email=request.POST['email'])
    if len(found_user) > 0:
        user_from_db = found_user[0]

        correct_pw = bcrypt.checkpw(
            request.POST['password'].encode(),
            user_from_db.password.encode()
        )

        if correct_pw == True:
            request.session['user_id'] = user_from_db.id
            return redirect('/success')
    messages.error(request, 'Invailid Email, Please Register')
    return redirect('/')


def post_message(request):
    errors = Message.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/success')
    user_id = request.session.get('user_id')
    if user_id is None:
        messages.error(request, "Please log in or register")
        return redirect('/')

    user_posted = User.objects.get(id=user_id)

    Message.objects.create(
        message=request.POST['message'],
        user_related=user_posted
    )
    return redirect('/success')


def profile(request, id):
    user_id = request.session.get('user_id')
    if user_id is None:
        messages.error(request, "Please log in or Register")
        return redirect('/')
    context = {
        "user": User.objects.get(id=id)
    }
    return render(request, "profile.html", context)


def edit_account(request, id):
    context = {
        "user": User.objects.get(id=id)
    }

    return render(request, "edit.html", context)


def delete(request, user_id):
    user_posted = Message.objects.get(id=user_id)
    if user_posted:
        user_posted.delete()
    return redirect('/success')


def update(request, id):
    errors = Message.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/success')
    user_id = request.session.get('user_id')
    if user_id is None:
        messages.error(request, "Please log in or register")
        return redirect('/')

    errors = User.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit.html')

    user_from_db = User.objects.get(id=id)

    user_from_db.first_name = request.POST['first_name']
    user_from_db.last_name = request.POST['last_name']
    user_from_db.email = request.POST['email']
    user_from_db.save()

    return redirect('/success')
