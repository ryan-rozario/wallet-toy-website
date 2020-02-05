from .views import registration, home_view, logout, deposit_view, withdraw_view, transfer_view
from django.urls import path, include

urlpatterns = [
    path('register',registration,name="register"),
    path('',home_view,name="home"),
    path('deposit',deposit_view,name="deposit"),
    path('withdraw',withdraw_view,name="withdraw"),
    path('transfer',transfer_view,name="transfer"),
    path('logout',logout,name="logout"),
]
