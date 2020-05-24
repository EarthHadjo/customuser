from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from customuser_app.models import MyUser
from customuser_app.forms import LoginForm, SignupForm
from customusers import settings

# Create your views here.
@login_required
def index(request):
    data = settings.AUTH_USER_MODEL
    return render(request, 'index.html', {'data': data})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = MyUser.objects.create_user(
                username=data['username'],
                displayname=data['displayname'],
                password=data['password']
            )
            return HttpResponseRedirect(reverse('homepage'))

    form = SignupForm()
    return render(request, 'signup.html', {'form':form})


def loginview(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('homepage'))
                )
    form = LoginForm()
    return render(request, 'signup.html', {'form': form})