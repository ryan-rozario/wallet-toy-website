from django import forms

class DepositForm(forms.Form):
    dep_amt = forms.IntegerField(min_value=0)

class WithdrawForm(forms.Form):
    wit_amt = forms.IntegerField(min_value=0)

class TransferForm(forms.Form):
    recipient = forms.CharField(label='Recipient Name', max_length=100)
    trans_amt = forms.IntegerField(min_value=0)