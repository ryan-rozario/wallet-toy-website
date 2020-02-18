from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import transaction


class Wallet(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    current_balance = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def add_money(self,val):
        with transaction.atomic():
            t=Transaction(wallet=self,val=val,running_balance=self.current_balance + val)
            t.save()
            self.current_balance += val
            self.save()

    def remove_money(self, val):
        if val>self.current_balance:
            print("No funds in wallet")
            return

        with transaction.atomic():        
            t=Transaction(wallet=self,val=-val,running_balance=self.current_balance - val)
            t.save()
            self.current_balance -= val
            self.save()

    def transfer(self, wallet, value):
        
        if self==wallet:
            print("Funds cant be transfered within same account")
            return

        if value>self.current_balance:
            print("No funds in wallet")
            return

        with transaction.atomic():
            self.remove_money(value)
        with transaction.atomic():
            wallet.add_money(value)



class Transaction(models.Model):
    wallet = models.ForeignKey(Wallet,on_delete=models.SET_NULL,null=True)
    val = models.BigIntegerField(default=0)
    running_balance = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

