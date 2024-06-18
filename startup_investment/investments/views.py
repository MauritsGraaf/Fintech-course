import base64
import io
import urllib
import random

from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Startup, Investment, calculate_date
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import InvestmentForm
from django.db.models import Sum
import matplotlib.pyplot as plt

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
    if request.user.is_authenticated:
        return redirect("dashboard")
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
def user_dashboard(request):
    investments = Investment.objects.filter(user=request.user)
    total_invested = investments.aggregate(total_invested=Sum('amount'))['total_invested'] or 0
    total_interest = sum([investment.calculate_profits() for investment in investments])
    current_date = calculate_date()
    return render(request, 'investments/dashboard.html', {'investments': investments, 'total_invested': total_invested, 'total_interest': total_interest, 'current_date': current_date})

@login_required
def next_day(request):
    cur_date = calculate_date()
    startups = Startup.objects.all()
    for startup in startups:
        startup.add_investments(cur_date)
    return redirect('dashboard')

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


def view_startup(request, startup_id):
    startup = get_object_or_404(Startup, pk=startup_id)

    investments = Investment.objects.filter(startup=startup)
    investment_amounts_per_day = investments.values('date_invested').annotate(total_invested=Sum('amount')).order_by('date_invested')
    cumulative_investments_per_day = []
    total_invested = 0
    for investment in investment_amounts_per_day:
        total_invested += investment['total_invested']
        cumulative_investments_per_day.append({'date_invested': investment['date_invested'], 'total_invested': total_invested})

    # plot
    plt.figure(figsize=(10,5))
    plt.plot([investment['date_invested'] for investment in cumulative_investments_per_day], [investment['total_invested'] for investment in cumulative_investments_per_day])
    plt.xlabel('Date')
    plt.ylabel('Total Investment')
    plt.title('Investment Growth')
    plt.ticklabel_format(scilimits=(-5, 100))
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request, 'startup.html', {'startup': startup, 'image': uri})


def reset_investments(request):
    Investment.objects.all().delete()

    for startup in Startup.objects.all():
        amount = random.randint(100, 10000)
        investment = Investment.objects.create(user=User.objects.first(), startup=startup, amount=amount, date_invested=0)
        investment.save()
        for i in range(1, 10):
            startup.add_investments(i)

    return redirect('dashboard')
