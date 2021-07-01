from django.db import models

# Create your models here.

class imagestore(models.Model):
    id = models.AutoField
    title = models.CharField(null=True,blank = True,max_length=10000)
    images = models.ImageField(null=True,blank = True)
    def __str__(self):
        return str(self.id)