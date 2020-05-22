from django import forms
from c_invoice.models import Factor,Records

class FactorForm(forms.ModelForm):
    class Meta:
        model=Factor
        fields=('invoice_number','seller_name','seller_add','seller_num','buyer_name','buyer_add','buyer_num')

class RecordForm(forms.ModelForm):
    class Meta:
        model=Records
        fields=('name','code','price','count','dis_percent','tax')