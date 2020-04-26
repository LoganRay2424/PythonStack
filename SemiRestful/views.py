from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    return redirect('/shows')


def all_shows(request):
    all_shows = Show.objects.all()
    context = {
        "shows": all_shows
    }
    return render(request, 'index.html', context)


def new_show(request):
    return render(request, 'new_show.html')


def create_new_show(request):
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    Show.objects.create(
        title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'])
    return redirect("/shows")


def show_page(request, id):
    show_page = Show.objects.get(id=id)
    context = {
        "show": show_page
    }
    return render(request, "show_page.html", context)


def edit_page(request, id):
    edit_page = Show.objects.get(id=id)
    context = {
        "show": edit_page
    }
    return render(request, "edit_page.html", context)


def update_page(request, id):
    update_page = Show.objects.get(id=id)
    id = str(Show.objects.last().id)
    errors = Show.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')
    else:
        show = Show.objects.get(id=id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['desc']
        show.save()
        context = {
            "show": show
        }
        return redirect(f'/shows/{id}', context)

    return


def delete_page(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')
