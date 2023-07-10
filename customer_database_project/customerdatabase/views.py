import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404, HttpResponseRedirect
from customerdatabase.forms import CustomerOrderEntryForm, CustomerOrderDetailsForm
from customerdatabase.models import CustomerOrderEntry, CustomerOrderDetails
from django.views.generic import ListView
from django.contrib import messages
import logging
logging.basicConfig(filename='debug.log', encoding='utf-8', level=logging.INFO)
class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = CustomerOrderEntry
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        
        return context
    
def order(request):
        if request.method == "POST":
            logging.info('POST Received to /order')
            pform = CustomerOrderEntryForm(request.POST, instance=CustomerOrderEntry())
            cforms = CustomerOrderDetailsForm(request.POST, instance=CustomerOrderDetails())
            if pform.is_valid() & cforms.is_valid():
                logging.info('Both Forms are valid')
                if(request.user.has_perm('customerdatabase.add_customerorderentry')):
                    logging.info('User ' + request.user.username + ' has permissions to add order')
                    message = pform.save(commit=False)
                    message.entryDate = datetime.now()
                    order_details = cforms.save(commit=False)
                    order_details.save()
                    message.customerOrder = cforms.instance
                    message.save()
                    logging.info('Committing order to database')
                    return redirect("home")
                else: 
                    logging.error('user' + request.user.username + ' does not have permission to log order')
                    messages.error(request, 'Sorry, You do not have permission to add an order to the system.')
        else:
            logging.info('GET Received to /order')
            pform = CustomerOrderEntryForm(instance=CustomerOrderEntry())
            cforms = CustomerOrderDetailsForm(instance=CustomerOrderDetails())
        return render(request, 'customerdatabase/order.html', {'customerorderentryform': pform, 'customerorderform': cforms})

def detail(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
  
    # add the dictionary during initialization
    context["data"] = CustomerOrderEntry.objects.get(id = id)
          
    return render(request, "customerdatabase/detail.html", context)

def update(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj2 = get_object_or_404(CustomerOrderEntry, id=id)
    obj1 = get_object_or_404(CustomerOrderDetails, id = obj2.customerOrder_id)
    # pass the object as instance in form
    form1 = CustomerOrderEntryForm(request.POST or None, instance = obj2)
    form2 = CustomerOrderDetailsForm(request.POST or None, instance = obj1)
    # save the data from the form and
    # redirect to detail_view
    if form1.is_valid():
        form1.save()
        if form2.is_valid():
         form2.save()
        return HttpResponseRedirect("/detail/"+id)
    
    context["form"] = form1, form2
  
    return render(request, 'customerdatabase/update.html', {'customerorderentryform': form1, 'customerorderform': form2})

def delete(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj2 = get_object_or_404(CustomerOrderEntry, id=id)
    obj1 = get_object_or_404(CustomerOrderDetails, id = obj2.customerOrder_id)
 
 
    if request.method =="POST":
        # delete object
        obj1.delete()
        obj2.delete
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "customerdatabase/delete.html", context)