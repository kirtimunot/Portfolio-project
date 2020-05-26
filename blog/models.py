from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateField()
    body=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='media/')