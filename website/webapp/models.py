from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notice(models.Model):
	subject=models.CharField(max_length=200)
	description=models.CharField(max_length=2000)
	dateshow = models.CharField(max_length=20,blank=True)

class User_details(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	postalcode=models.CharField(max_length=20)
	address=models.CharField(max_length=50)


class Complain_table(models.Model):
	complainer_name=models.CharField(max_length=20)
	complainer_email=models.EmailField(max_length=254)
	complainer_phone_number=models.CharField(max_length=12)
	complaint_area_name=models.TextField()
	complaint_postal_code=models.CharField(max_length=20)
	house_holdin_number=models.CharField(max_length=10)
	complain_subject=models.CharField(max_length=30)
	complain=models.TextField()
	image_field=models.ImageField(upload_to='images/',default='webapp/images/icon.png')
	dateshow = models.CharField(max_length=20,blank=True)
	timeshow = models.CharField(max_length=20,blank=True)



class House_holding_number(models.Model):
	holder_name=models.CharField(max_length=24)
	holding_number=models.CharField(max_length=15)