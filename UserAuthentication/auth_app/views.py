from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        initialdata = {'username':'', 'email':'',"password1":'','password2':''}
        form = UserCreationForm(initial = initialdata)

    return render(request, 'auth/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'auth/login.html', {'form': form})

@login_required
def dashboard_view(request):
    return render(request, 'auth/dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')