from django.db import models

# Create your models here.

class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True) ##########
    gender = models.CharField(max_length=55) #gender VARCHAR(55) NOT NULL
    created_at = models.DateTimeField(auto_now_add=True) #Created_at TIME STAMP DEFALT CURRENT_TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True) #updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

    class Meta:
        db_table = 'genders'

class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=55)
    middle_name = models.CharField(max_length=55, blank=True)
    last_name = models.CharField(max_length=55)
    age = models.IntegerField()
    birth_date = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    username = models.CharField(max_length=55)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'users'
   