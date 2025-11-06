from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# TOD0: fix log out.
# 6- add animations (last)

@login_required(login_url='xina:login')
def mainPage(request):
    return render(request, 'Xina/main.html')

@login_required(login_url='xina:login')
def Create(request):
    return render(request, 'Xina/Create.html')

def index(request):
    return render(request, 'Xina/index.html') 

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        # Authenticate credentials
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Incorrect username or password.")
            return render(request, 'Xina/Auth.html')

        # Login successful
        login(request, user)
        return redirect('xina:main')

    # GET request: render login form
    return render(request, 'Xina/Auth.html')

def logoutUser(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('xina:index')

def SignUpPage(request):
    sign_up_active = True  # By default, show signup tab
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()

        if not username or not email or not password:
            messages.error(request, "All fields are required.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        elif len(password) < 6:
            messages.error(request, "Password must be at least 6 characters long.")
        else:
            # Create user and log in
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            messages.success(request, f"Welcome, {username}! Your account has been created.")
            return redirect('xina:main')

    # GET request or failed POST: render the page with signup active
    return render(request, 'Xina/Auth.html', {'sign_up_active': sign_up_active})

