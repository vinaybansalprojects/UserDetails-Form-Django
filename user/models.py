from django.db import models

class Snippet(models.Model):
	name = models.CharField(max_length=100)
	birthday= models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=200,null=True)
	def __str__(self):
			return self.name