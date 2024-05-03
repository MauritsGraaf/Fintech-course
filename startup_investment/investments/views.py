from django.shortcuts import render, redirect, get_object_or_404
from .models import Startup, Investment
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import InvestmentForm
from django.db.models import Sum

def register_request(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Account created successfully. You are now logged in as {username}.')
                return redirect("login")  # Redirect to the login page after successful registration
            else:
                messages.error(request, 'Failed to authenticate user after registration.')
        else:
            messages.error(request, 'Invalid registration form data.')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
    return render(request, "login.html")

@login_required
def startup_list(request):
    startups = Startup.objects.all()
    return render(request, 'investments/startup_list.html', {'startups': startups})

@login_required
def explanation_page(request):
    return render(request, 'explanation.html')

@login_required
def invest_in_startup(request):
    if request.method == 'POST':
        startup_id = request.POST.get('startup_id')
        amount = request.POST.get('amount')
        if startup_id and amount:
            startup = Startup.objects.get(id=startup_id)
            Investment.objects.create(user=request.user, startup=startup, amount=amount)
            return redirect('dashboard')  # Redirect to the dashboard after investment
    else:
        startups = Startup.objects.all()  # Display available startups to invest in
        return render(request, 'investments/invest.html', {'startups': startups})

@login_required
def user_dashboard(request):
    investments = Investment.objects.filter(user=request.user)
    total_invested = investments.aggregate(total_invested=Sum('amount'))['total_invested'] or 0
    total_profits = investments.aggregate(total_profits=Sum('profits'))['total_profits'] or 0
    return render(request, 'investments/dashboard.html', {'investments': investments, 'total_invested': total_invested, 'total_profits': total_profits})

def logout_request(request):
    logout(request)
    return redirect("login")

def home(request):
    return render(request, 'investments/home.html')

def invest_in_startup(request, startup_id):
    startup = get_object_or_404(Startup, pk=startup_id)
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if amount < 1000:
                messages.error(request, 'Minimum investment amount is $1000.')
            else:
                investment = Investment(user=request.user, startup=startup, amount=amount)
                investment.save()
                messages.success(request, 'Investment successful.')
                return redirect('dashboard')
    else:
        form = InvestmentForm()
    return render(request, 'invest_in_startup.html', {'form': form, 'startup': startup})
