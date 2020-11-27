from django.db import models
from django.utils.html import format_html

# Create your models here.
class Author(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()

class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author)
    publicationDate = models.DateField()

class List(models.Model):
    item = models.CharField(max_length=300)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.item

class MOVIE_DATA(models.Model):
    Name = models.CharField(max_length=30)
    link = models.CharField(max_length=2000)
    image = models.FileField(upload_to='upload',null=True,blank=True)

    def show_image(self):
        if self.image:
            return format_html('<img src="'+ self.image.url +'"height="50px">')
        return ''
    show_image.allow_tage = True

class MUSIC_DATA(models.Model):
    Name = models.CharField(max_length=30)
    link = models.CharField(max_length=2000)
    image = models.FileField(upload_to='upload',null=True,blank=True)

    def show_image(self):
        if self.image:
            return format_html('<img src="'+ self.image.url +'"height="50px">')
        return ''
    show_image.allow_tage = True


class SHOPING_DATA(models.Model):
    Name = models.CharField(max_length=30)
    link = models.CharField(max_length=2000)
    image = models.FileField(upload_to='upload',null=True,blank=True)

    def show_image(self):
        if self.image:
            return format_html('<img src="'+ self.image.url +'"height="50px">')
        return ''
    show_image.allow_tage = True

class GAME_DATA(models.Model):
    Name = models.CharField(max_length=30)
    link = models.CharField(max_length=2000)
    image = models.FileField(upload_to='upload',null=True,blank=True)

    def show_image(self):
        if self.image:
            return format_html('<img src="'+ self.image.url +'"height="50px">')
        return ''
    show_image.allow_tage = True