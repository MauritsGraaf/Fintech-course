from django.urls import path
from .views import (
    login_request,
    logout_request,
    startup_list,
    invest_in_startup,
    user_dashboard,
    register_request,
    home,
    explanation_page
)

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
    path('startups/', startup_list, name='startup_list'),
    path('startups/invest/<int:startup_id>/', invest_in_startup, name='invest_in_startup'),  # Adjusted URL pattern
    path('dashboard/', user_dashboard, name='dashboard'),
    path('explanation/', explanation_page, name='explanation'),  # Add the path for the explanation page
]
