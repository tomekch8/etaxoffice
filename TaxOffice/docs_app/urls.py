from django.urls import path
from .views import list_document, upload_document, document_detail
from . import views

urlpatterns = [
    path('list/', list_document, name='list'),
    path('document/<int:pk>/', document_detail, name='document_detail'),

    path('upload/', upload_document, name='upload'),


    # path('register/', register, name='register'),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]
