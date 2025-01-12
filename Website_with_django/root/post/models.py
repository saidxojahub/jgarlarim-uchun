from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')

    def __str__(self):

        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name