#from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse 


class Users(models.Model):
	name = models.CharField(max_length=100)
	login = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	sex = models.CharField(max_length=6)
	badge = models.CharField(max_length=20)
	age = models.CharField(max_length=3)
	def __str__(self):
            return self.name	



class Contributions(models.Model):
	user = models.ForeignKey(Users, on_delete=models.CASCADE)
	#reactions = models.ForeignKey(Reactions, on_delete=models.CASCADE)
	date = models.DateField
	content = models.CharField(max_length=1000)
	def __str__(self):
            return self.content


	

class Files(models.Model):
	name = models.CharField(max_length=100)
	size = models.IntegerField
	user = models.ForeignKey(Users, on_delete=models.CASCADE)
	def __str__(self):
            return self.file_name



class Posts(models.Model):
        title = models.CharField(max_length=100)
        content = models.CharField(max_length=10000)
        owner = models.ForeignKey(Users, on_delete=models.CASCADE)
        def __str__(self):
            return self.title


