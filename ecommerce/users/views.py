from django.shortcuts import render, redirect, Http404, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
# from users.forms import RegisterForm
# from users.forms import UserForm
# from django.contrib.auth.forms import UserCreationForm
from users.forms import ProfileAvatarForm, CustomUserCreationForm


# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('/profile')
#
#     if request.method == 'GET':
#         pass
#     else:
#         username = request.POST['username']
#         password = request.POST['password']
#
#         print('username', username)
#         print('password', password)
#
#         user = authenticate(username=username, password=password)
#         print('user', user)
#
#         if user is not None:
#             login(request, user)
#             return redirect('/profile')
#
#     return render(request, 'users/login.html')

# @login_required
# def logout_view(request):
#     if request.method == 'GET':
#         raise Http404()
#
#     logout(request)
#     return redirect('/login')


@login_required
def profile_view(request):
    # print('\n' * 2)
    # print('request.POST', request.POST)
    # print('request.FILES', request.FILES['avatar'])
    # print('\n' * 2)
    if request.method == 'GET':
        form = ProfileAvatarForm()
    else:
        form = ProfileAvatarForm(files=request.FILES, instance=request.user.profile)
        if form.is_valid:
            form.save()
            return redirect(reverse('users:profile'))

    return render(request, 'users/profile.html', {
        'form': form
    })


# Use this for registering users with a custom form
# def register_view(request):
#     if request.user.is_authenticated:
#         return redirect(reverse(settings.LOGIN_REDIRECT_URL))
#
#     if request.method == 'GET':
#         form = RegisterForm()
#     else:
#         form = RegisterForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(reverse(settings.LOGIN_REDIRECT_URL))
#
#     return render(request, 'users/register.html', {
#         'form': form
#     })

# Use this for registering users with a model form
# def register_view(request):
#     if request.user.is_authenticated:
#         return redirect(reverse(settings.LOGIN_REDIRECT_URL))
#
#     if request.method == 'GET':
#         form = UserForm()
#     else:
#         form = UserForm(request.POST)
#
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect(reverse(settings.LOGIN_REDIRECT_URL))
#
#     return render(request, 'users/register.html', {
#         'form': form
#     })

def register_view(request):
    if request.user.is_authenticated:
        return redirect(reverse(settings.LOGIN_REDIRECT_URL))

    if request.method == 'GET':
        # form = UserCreationForm()
        form = CustomUserCreationForm()
    else:
        # form = UserCreationForm(request.POST)
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse(settings.LOGIN_REDIRECT_URL))

    return render(request, 'users/register.html', {
        'form': form
    })
