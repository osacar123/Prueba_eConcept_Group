from django.db import models

#Creacion del modelo en la base de datos
class Users(models.Model):
	name = models.CharField(max_length=200,null=False)
	password = models.CharField(max_length=50,null=False)
	email = models.EmailField(unique=True)
	