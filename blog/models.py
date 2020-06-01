from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateField()
    body=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='media/')

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title

    def disp_date(self):
        return self.pub_date.strftime('%b %e %Y')

