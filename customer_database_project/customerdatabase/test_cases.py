from django.test import TestCase
from django.contrib.auth.models import User, Permission
from django.conf import settings
from customerdatabase.forms import CustomerOrderEntryForm
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password


class TestCustomerOrderEntryForm(TestCase):

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

class TestAuthenticatedEndpoints(TestCase):
    
    def test_logged_out_user_cannot_POST(self):
        response = self.client.post("/order/", data={"customerName": "123", "orderItem" : "client", "quantity": 2})
        messages = list(response.context['messages'])
        self.assertEqual(messages[0].message, 'Sorry, You do not have permission to add an order to the system.')

    def test_logged_in_user_cannot_POST_without_permission(self):
        user = User.objects.create_user(username='testUser1', email = 'test_email@test.com', password="A1B2C4D8$&BBddiiL")
        self.assertTrue(self.client.login(username = 'testUser1', password = 'A1B2C4D8$&BBddiiL'))

        response = self.client.post("/order/", data={"customerName": "123", "orderItem" : "client", "quantity": 2})
        messages = list(response.context['messages'])
        self.assertEqual(messages[0].message, 'Sorry, You do not have permission to add an order to the system.')


class TestValidators(TestCase):

    def test_password_length_validator(self):
        self.assertRaises(ValidationError, validate_password, "a1D!")
    
    def test_password_contains_special_characters_validator(self):
        self.assertRaises(ValidationError, validate_password, "fdjsk1fhsd8kfhsdjkDDDD")
    
    def test_password_contains_one_uppercase_validator(self):
        self.assertRaises(ValidationError, validate_password, "fdsfdsfdsfkhjsd8fhsjdk%")
    
    def test_password_contains_one_digit_validator(self):
        self.assertRaises(ValidationError, validate_password, "afgdshjfgsdjfsgdDD&")

    def test_conformant_password(self):
        validate_password("A1B2C4D8$&BBddiiL")
