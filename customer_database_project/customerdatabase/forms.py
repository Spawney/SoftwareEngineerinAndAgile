from django import forms
from customerdatabase.models import CustomerOrderEntry, CustomerOrderDetails

class CustomerOrderEntryForm(forms.ModelForm):
    class Meta:
        model = CustomerOrderEntry
        fields = ("customerName", )

class CustomerOrderDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomerOrderDetails
        fields = ("orderItem", "quantity", )