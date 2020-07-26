from django.db import models
 
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email= models.EmailField( max_length=254)
    gender =models.CharField(max_length=20)
    phone=  models.CharField(max_length=15)
    message= models.TextField()
    date= models.DateTimeField( auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "contacts"

    


    