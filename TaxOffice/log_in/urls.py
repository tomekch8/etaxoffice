from django.urls import path
from .views import profile_view, verify_changes
from . import views

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('verify-changes/<str:token>/', verify_changes, name='verify_changes'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # path('register/', register, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
