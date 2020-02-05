from django import forms

class DepositForm(forms.Form):
    amt = forms.IntegerField(min_value=0)

class WithdrawForm(forms.Form):
    amt = forms.IntegerField(min_value=0)

class TransferForm(forms.Form):
    recipient = forms.CharField(label='Recipient Name', max_length=100)
    amt = forms.IntegerField(min_value=0)