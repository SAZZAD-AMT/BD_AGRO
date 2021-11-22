from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .decorators import unauthenticated_user


@unauthenticated_user
def signup_view(request):
  form = SignUpForm(request.POST)
  if form.is_valid():
    form.save()
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password1')
    user = authenticate(username=username, password=password)
    # login(request, user)
    return redirect('login')
  return render(request, 'signup.html', {'form': form})


@unauthenticated_user
def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      login(request, user)
      return redirect('blog')
  else:
    form = AuthenticationForm()
  return render(request, 'login.html',  {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
