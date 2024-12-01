from django.db import models

# Create your models here.


class AccountsUser(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'bangtuitui_py_easeapi_accounts_user'

    def __str__(self):
        return self.username