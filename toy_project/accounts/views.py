import django
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import auth
from .forms import ProfileForm


def signup(request):
    if request.method == 'POST':

        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1']
            )

            user.save()

            auth.login(request, user)
            return redirect('main:index')
    else:

        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main:index')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('main:index')


def create_profile(request):
    if request.method == "POST":
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            user = request.user
            user = User.objects.get(username=user)
            profile_form = profile_form.save(commit=False)
            profile_form.user = user
            profile_form.save()
            return redirect('main:index')
    else:
        profile_form = ProfileForm()
    return render(request, 'create_profile.html', {'profile_form': profile_form})


def modify_profile(request, pk):
    my_profile = Profile.objects.get(pk=pk)

    if request.method == "POST":
        modify_form = ProfileForm(request.POST, instance=my_profile)
        if modify_form.is_valid():
            modify_form = modify_form.save(commit=False)
            modify_form.user = request.user
            modify_form.save()
            return redirect('main:index')
    else:
        modify_form = ProfileForm(instance=my_profile)
    return render(request, 'modify_profile.html', {'modify_form': modify_form})
