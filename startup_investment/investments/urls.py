from django.urls import path
from .views import (
    login_request,
    logout_request,
    startup_list,
    invest_in_startup,
    user_dashboard,
    register_request,
    home,
    explanation_page,
    next_day,
    view_startup,
    reset_investments
)

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path('reset/',reset_investments, name='reset'),
    path('startups/', startup_list, name='startup_list'),
    path('startups/next_day', next_day, name='next_day'),
    path('startups/view/<int:startup_id>/', view_startup, name='view_startup'),
    path('startups/invest/<int:startup_id>/', invest_in_startup, name='invest_in_startup'),  # Adjusted URL pattern
    path('dashboard/', user_dashboard, name='dashboard'),
    path('explanation/', explanation_page, name='explanation'),  # Add the path for the explanation page
]
