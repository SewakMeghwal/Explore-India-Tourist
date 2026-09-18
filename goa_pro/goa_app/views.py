from django.shortcuts import render, redirect, get_object_or_404
from .models import Destinations, State, Season, Restaurants, profileimage
from .forms import Destinations_form, contact_us_form, profileimageform
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.
@login_required(login_url='login')
def home(request):
    featured_destinations = Destinations.objects.all()[:6]
    return render(request, 'home.html', {'destinations': featured_destinations})

@login_required(login_url='login')
def show(request):
    data = Destinations.objects.all()
    return render(request, 'show.html', {'data': data})

@login_required(login_url='login')
def readmore(request, id):
    data = get_object_or_404(Destinations, id=id)
    return render(request, 'readmore.html', {'data': data})

@login_required(login_url='login')
def res_read(request, id):
    data = get_object_or_404(Restaurants, id=id)
    return render(request, 'readmore2.html', {'data': data})

@login_required(login_url='login')
def form(request):
    if not request.user.is_superuser:
        messages.error(request, "Only administrator accounts can add new destinations.")
        return redirect('home')
        
    if request.method == 'GET':
        data = Destinations_form()
        return render(request, 'form.html', {'data': data})
    else:
        data = Destinations_form(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            messages.success(request, "Destination added successfully!")
            return redirect('show')
        else:
            return render(request, 'form.html', {'data': data})

@login_required(login_url='login')
def search(request):
    query = request.POST.get('search') or request.GET.get('search', '')
    query = query.strip()
    if query:
        data = Destinations.objects.filter(Title__icontains=query)
    else:
        data = Destinations.objects.none()
    return render(request, 'search.html', {'data': data, 'query': query})

@login_required(login_url='login')
def state_fil(request, state1):
    s = State.objects.filter(state__iexact=state1)
    if s.exists():
        data = Destinations.objects.filter(state__in=s)
        return render(request, 'kerala.html', {'data': data, 's': s, 'state_name': state1})
    return render(request, 'kerala.html', {'data': [], 'state_name': state1})

@login_required(login_url='login')
def diff_plsce(request):
    return render(request, 'diff_place.html')

@login_required(login_url='login')
def hotels(request):
    data = Restaurants.objects.all()
    return render(request, 'hotels.html', {'data': data})

@login_required(login_url='login')
def honeymoon(request):
    data = Destinations.objects.all()
    return render(request, 'honeymoon.html', {'data': data})

@login_required(login_url='login')
def season_fil(request, season1):
    b = Season.objects.filter(season__iexact=season1)
    if b.exists():
        data = Destinations.objects.filter(season__in=b)
        return render(request, 'honeymoon.html', {'data': data, 'b': b, 'season_name': season1})
    return render(request, 'honeymoon.html', {'data': [], 'season_name': season1})

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        c_password = request.POST.get('c_password', '')

        if password != c_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')
            
        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists with this username.")
            return render(request, 'register.html')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return render(request, 'register.html')
            
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')
    
    return render(request, 'register.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        user_authenticated = authenticate(username=username, password=password)

        if user_authenticated is None:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login.html')
        else:
            auth_login(request, user_authenticated)
            messages.success(request, f"Welcome back, {user_authenticated.username}!")
            return redirect('home')
        
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('index')

def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def contact(request):
    if request.method == 'GET':
        form = contact_us_form()
        return render(request, 'contact.html', {'form': form})
    else:
        form = contact_us_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
        else:
            return render(request, 'contact.html', {'form': form})

@login_required(login_url='login')
def profile(request):
    user_qs = [request.user]
    img_qs = profileimage.objects.all()
    dat3 = {
        'da1': user_qs,
        'da2': img_qs
    }
    return render(request, 'profile.html', dat3)

@login_required(login_url='login')
def changep(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changep.html', {'form': form})

@login_required(login_url='login')
def profile_image(request):
    if request.method == 'GET':
        form = profileimageform()
        return render(request, 'profile_image.html', {'form': form})
    else:
        form = profileimageform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile image updated successfully!")
            return redirect('profile')
        
    return render(request, 'profile_image.html')

@login_required(login_url='login')
def update(request, id):
    data = get_object_or_404(profileimage, id=id)
    if request.method == 'GET':
        form = profileimageform(instance=data)
        return render(request, 'profile_image.html', {'form': form})
    else:
        form = profileimageform(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile image updated!")
            return redirect('profile')
        
    return render(request, 'profile_image.html', {'form': form})
