from django.shortcuts import render, redirect, Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/profile')

    if request.method == 'GET':
        pass
    else:
        username = request.POST['username']
        password = request.POST['password']

        print('username', username)
        print('password', password)

        user = authenticate(username=username, password=password)
        print('user', user)

        if user is not None:
            login(request, user)
            return redirect('/profile')

    return render(request, 'users/login.html')


@login_required
def profile_view(request):
    return render(request, 'users/profile.html')


@login_required
def logout_view(request):
    if request.method == 'GET':
        raise Http404()

    logout(request)
    return redirect('/login')
