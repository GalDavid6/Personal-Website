from django.db import models

# Create your models here.
class Post(models.Model):
    id= models.AutoField(primary_key=True)
    title= models.CharField(max_length=50)
    content= models.TextField()
    author= models.CharField(max_length=20)
    slug= models.CharField(max_length=50)
    timeStamp= models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self) -> str:
        return self.title + ' - ' + self.author