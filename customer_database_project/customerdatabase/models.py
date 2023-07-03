from django.db import models
from django.utils import timezone

ORDER_CHOICES = (
    ('psn','PSN'),
    ('client', 'CLIENT'),
)

class CustomerOrderDetails(models.Model):
    orderItem = models.CharField("Item", max_length=6, choices=ORDER_CHOICES, default='client')
    quantity = models.PositiveIntegerField("Quantity")
    
class CustomerOrderEntry(models.Model):
    customerName = models.CharField("Customer Name", max_length=200)
    entryDate = models.DateTimeField("date added")
    customerOrder = models.ForeignKey(CustomerOrderDetails, on_delete=models.CASCADE)

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.entryDate)
        return f"'{self.customerName}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


