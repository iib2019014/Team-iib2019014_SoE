from django.test import TestCase, Client
from django.urls import reverse
from ..models import Account, AccountManager
from personal.models import Request

class TestViews(TestCase) :
    def setUp(self) :
        # print('setUp yes')
        self.client = Client()
        # self.an_account_manager = AccountManager.objects.create()
        self.a_super_account = Account.objects.create_superuser(
            email="super@gmail.com",
            username="super",
            firstname="super",
            password="super",
        )

        self.an_account = Account.objects.create_user(
            email="normal@gmail.com",
            username="normal",
            firstname="normal",
            # password="super",
        )
        # print(self.an_account.is_admin)
        # assert self.an_account.is_admin == True

    def test_UserRegistrationView_GET(self) :
        response = self.client.get(reverse('register'))
        # print(self.an_account.is_admin)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')