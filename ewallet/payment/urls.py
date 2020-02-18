from .views import registration, home_view, logout, deposit_view, withdraw_view, transfer_view
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register',registration,name="register"),
    path('',home_view,name="home"),
    path('deposit',deposit_view,name="deposit"),
    path('withdraw',withdraw_view,name="withdraw"),
    path('transfer',transfer_view,name="transfer"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
