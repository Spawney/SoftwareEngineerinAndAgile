from django.test import SimpleTestCase
from django.conf import settings

import django

settings.configure()
django.setup()

from customerdatabase.forms import CustomerOrderEntryForm


class CustomerOrderEntryFormTests(SimpleTestCase):
    def test_customer_name_cannot_have_numbers(self):
        form = CustomerOrderEntryForm(data={"customerName": "123"})
        self.assertTrue(form.has_error)
    
    def test_customer_name_longer_than_200_errors(self):
        form = CustomerOrderEntryForm(data={"customerName": "fudighsdfghfdjghfdsjkghdsfkjghfdskjghfksjdghs"
                                            +"kfjgjfdghjfdglkdfhgdffgndsjfkshdnfksdhfsdkfhsdkfhsdjkfhsdjkfh"
                                            +"sjdkfhsjdkfhjsdkfhsjdkhfjdkshfjkdshfjsdkhfjksdhfeuhrishjdhfeuis"
                                            +"hdjksfhdjskfhdsjkhdsasdsasdsadsa"
                                            })
        self.assertTrue(form.has_error)
    
