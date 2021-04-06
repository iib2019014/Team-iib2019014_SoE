from django.test import SimpleTestCase
from ..forms import UserRegistrationForm, AccountAuthenticationForm, AccountUpdationForm

class TestForms(SimpleTestCase) :
    def test_UserRegistrationForm_with_valid_data(self) :
        a_form = UserRegistrationForm()
        a_form.data = {
                'email' : "user@gmail.com",
                'username' : "user",
                'password1' : "password",
                'password2' : "password",
            }

        self.assertTrue(a_form.is_valid())

    # def test_AccountUpdationForm_with_valid_data(self) :
    #     a_form = AccountUpdationForm()
    #     a_form.data = {'email' : "user@gmail.com"}
    #     print('yes')
    #     print(a_form.data)

    #     self.assertTrue(a_form.is_valid())