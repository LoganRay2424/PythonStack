from django.shortcuts import render

from django.shortcuts import render, redirect
import random


def index(request):
    if 'activity' not in request.session:
        request.session['activity'] = []
    if 'total' not in request.session:
        request.session['total'] = 0
    return render(request, 'ninja.html')


def process(request):
    activity = request.session['activity']
    total = request.session['total']
    if request.POST['location'] == "farm":
        rand_num = random.randint(10, 20)
        total += rand_num
        request.session['total'] = total
        activity.append(f'Earned{rand_num} golds from the Farm!')
        print(rand_num)
    request.session['money'] = request.POST['process_money']

    # return render(request, 'ninja.html')

    if request.POST['location'] == "Cave":
        rand_num = random.randint(5, 10)
        total += rand_num
        request.session['total'] = total
        print(rand_num)
        activity.append(f'Earned{rand_num} golds from the Cave!')
    request.session['money'] = request.POST['process_money']

    if request.POST['location'] == "House":
        rand_num = random.randint(2, 5)
        total += rand_num
        request.session['total'] = total
        print(rand_num)
        activity.append(f'Earned{rand_num} golds from the House!')

    request.session['money'] = request.POST['process_money']

    if request.POST['location'] == "Casino":
        rand_num = random.randint(0, 50)
        if rand_num % 2 == 1:
            total += rand_num
            activity.append(f'Entered a casino and won{rand_num} golds!')

        else:
            total -= rand_num
            activity.append(f'Entered a casino and lost{rand_num} golds!')
        request.session['total'] = total
        print(rand_num)
    request.session['money'] = request.POST['process_money']

    return render(request, 'ninja.html')
