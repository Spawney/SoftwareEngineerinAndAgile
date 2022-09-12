import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from customerdatabase.forms import CustomerOrderEntryForm, CustomerOrderDetailsForm
from customerdatabase.models import CustomerOrderEntry, CustomerOrderDetails
from django.views.generic import ListView
from django.contrib import messages

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = CustomerOrderEntry

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def order(request):
        if request.method == "POST":
            pform = CustomerOrderEntryForm(request.POST, instance=CustomerOrderEntry())
            cforms = CustomerOrderDetailsForm(request.POST, instance=CustomerOrderDetails())
            if pform.is_valid():
                if(request.user.has_perm('customerdatabase.add_bar')):
                    message = pform.save(commit=False)
                    message.entryDate = datetime.now()
                    order_details = cforms.save(commit=False)
                    order_details.save()
                    message.customerOrder = cforms.instance
                    message.save()
                    return redirect("home")
                else: 
                    messages.error(request, 'Sorry, You do not have permission to add an order to the system.')
        else:
            pform = CustomerOrderEntryForm(instance=CustomerOrderEntry())
            cforms = CustomerOrderDetailsForm(instance=CustomerOrderDetails())
        return render(request, 'customerdatabase/order.html', {'customerorderentryform': pform, 'customerorderform': cforms})