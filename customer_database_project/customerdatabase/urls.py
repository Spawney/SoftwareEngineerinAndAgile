from django.urls import path
from customerdatabase.models import CustomerOrderEntry
from customerdatabase import views
from django.contrib import admin

home_list_view = views.HomeListView.as_view(
    queryset=CustomerOrderEntry.objects.order_by("-entryDate"),
    context_object_name="message_list",
    template_name="customerdatabase/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("order/", views.order, name="order"),
]

