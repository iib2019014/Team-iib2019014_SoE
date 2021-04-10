from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# import core.models
import personal

# Create your models here.




class AccountManager(BaseUserManager) :
    def create_user(self, email, username, firstname, the_building, building_id = None, password = None) :
        if not email :
            raise ValueError("please provide a valid email...")
        if not username :
            raise ValueError("please provide a valid username...")

        else :
            user = self.model(
                email = self.normalize_email(email),
                username = username,
                building_id = building_id,
                the_building = personal.models.Building.objects.get(building_id=building_id)
            )

            # user.set_password("123456")
            # print("1111111111111111 hhhhheeeelllooooo")
            user.save(using = self._db)

            return user

    def create_superuser(self, email, username, firstname, password) :
        if not email :
            raise ValueError("please provide a valid email...")
        if not username :
            raise ValueError("please provide a valid username...")

        else :
            superuser = self.model(
                email = self.normalize_email(email),
                username = username,
                password = password,
            )

            superuser.is_admin = True
            superuser.is_staff = True
            superuser.is_superuser= True

            superuser.set_password(password)
            superuser.save(using = self._db)

            return superuser


class Account(AbstractBaseUser) :
    email                       = models.EmailField(verbose_name="email", max_length=30, unique=True)
    username                    = models.CharField(max_length=20, unique=True)
    firstname                   = models.CharField(max_length=20, unique=False)
    building_id                 = models.CharField(max_length=10, unique=False, default="")
    the_building                = models.ForeignKey(personal.models.Building, on_delete=models.CASCADE, null=True)




    # the below 6 are needed for a CUM,
    date_joined = models.DateTimeField(verbose_name = "date_joined", auto_now_add = True)
    last_login = models.DateTimeField(verbose_name = "last_login", auto_now = True)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    objects = AccountManager()
    

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username', 'firstname']


    def __str__(self) :
        return self.email + ", " + self.username

    
    def has_perm(self, perm, obj = None) :
        return self.is_admin

    def has_module_perms(self, app_label) :
        return True


# class Device(models.Model) :
#     device_name = models.CharField(max_length=20, unique=False)

#     def __str__(self) :
#         return self.device_name