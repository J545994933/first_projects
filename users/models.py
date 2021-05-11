from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UsersModel(User):

    class Meta:
        db_table = 'users'
