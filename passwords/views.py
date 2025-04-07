from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, PasswordForm
from .models import PasswordEntry

# Register User
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Login User
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')

# Dashboard (Show saved passwords)
def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.set_password(request.POST['password'])
            entry.save()
            return redirect('dashboard')

    form = PasswordForm()
    passwords = PasswordEntry.objects.filter(user=request.user)
    
    for entry in passwords:
        entry.decrypted_password = entry.get_password()

    return render(request, 'dashboard.html', {'form': form, 'passwords': passwords})

# Delete Password
def delete_password(request, password_id):
    entry = PasswordEntry.objects.get(id=password_id, user=request.user)
    entry.delete()
    return redirect('dashboard')
