from django.db import models

# Create your models here.

#Назначаем поле "email" в моделе юзер уникальным в 2 строки
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True