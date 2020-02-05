from django.shortcuts import render, redirect
from django.views.generic.list import ListView

from .models import Wallet, Transaction
from django.contrib.auth.models import User
from .forms import DepositForm, WithdrawForm, TransferForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.



def registration(request):

    if request.method=='POST':
        form =UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            password

            user = authenticate(username=username,password=password)
            

            login(request,user)
            w=Wallet(user=user)
            w.save()
            return redirect('/')

    form =UserCreationForm()
    context={'form':form}
    return render(request,'registration/registration.html',context)

def logout_user(request):
	logout(request)
	return redirect('/')

@login_required()
def home_view(request,*args,**kwargs):

    user = None
    if request.user.is_authenticated:
        user = request.user


    w = Wallet.objects.get(user=user)
    #print(w.current_balance)
    dep = DepositForm()
    wit = WithdrawForm()
    trans = TransferForm()
    con = {"w":w,"deposit":dep,"withdraw":wit,"transfer":trans}
    return render(request, 'payment/detail.html', con)

@login_required()
def deposit_view(request,*args,**kwargs):

    user = None
    if request.user.is_authenticated:
        user = request.user
    w = Wallet.objects.get(user=user)

    if request.method=='POST':
        dep =DepositForm(request.POST)

        if dep.is_valid():
            amt=dep.cleaned_data['amt']

            w.add_money(amt)
            


    return redirect('/')

@login_required()
def withdraw_view(request,*args,**kwargs):

    user = None
    if request.user.is_authenticated:
        user = request.user
    w = Wallet.objects.get(user=user)

    if request.method=='POST':
        wit =WithdrawForm(request.POST)

        if wit.is_valid():
            amt=wit.cleaned_data['amt']

            w.remove_money(amt)
            


    return redirect('/')

@login_required()
def transfer_view(request,*args,**kwargs):

    user = None
    if request.user.is_authenticated:
        user = request.user
    sender = Wallet.objects.get(user=user)

    if request.method=='POST':
        trans =TransferForm(request.POST)

        if trans.is_valid():
            amt=trans.cleaned_data['amt']
            reciever_username = trans.cleaned_data['recipient']
            reciever_object = User.objects.get(username=reciever_username)
            reciever = Wallet.objects.get(user=reciever_object)
            #print(reciever)
            sender.transfer(reciever, amt)
            


    return redirect('/')




#def TransactionListView():
#    paginate_by = 10

#    queryset=Transaction.objects.get(name="Cheddar Talk")

