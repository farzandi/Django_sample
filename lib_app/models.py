from statistics import mode

from django.db import models

# Create your models here.


class Article (models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publish_date = models.DateField(null=True, blank=True )
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    source = models.ForeignKey('Book', on_delete=models.CASCADE , null=True, blank=True)
    comment= models.ForeignKey('Comment', on_delete=models.CASCADE, null=True, blank=True)
    age= models.CharField(max_length=50 , null=True, blank=True )
    time_to_read = models.CharField(max_length=50 , null=True, blank=True)
    score = models.PositiveSmallIntegerField(null=True, blank=True)
    chapter_verses = models.ForeignKey('Verses',on_delete=models.CASCADE , null=True, blank=True)
    tradition = models.ForeignKey('Tradition', on_delete=models.CASCADE ,null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='files' )
    content = models.TextField(max_length=10000)
    file = models.FileField(null=True, blank=True, upload_to='files')

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    rezome = models.FileField(null=True, blank=True, upload_to='files')
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    education  = models.CharField(max_length=12)

    def __str__(self):
        return self.last_name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Verses(models.Model):
    chapter_name = models.ForeignKey('Chapter', on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    translation = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.text

class Chapter(models.Model):
    name = models.CharField(max_length=50)
    number_of_versus = models.PositiveSmallIntegerField(null=True, blank=True)
    type = models.CharField(max_length=100) # maki or madani
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

class Tradition(models.Model):
    text = models.TextField()
    saying= models.CharField(max_length=50 , null=True, blank=True)
    transmitter = models.CharField(max_length=100 , null=True, blank=True)
    source = models.CharField(max_length=200 , null=True, blank=True)
    type = models.CharField(max_length=100 , null=True, blank=True)
    def __str__(self):
        return self.text

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE , null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to='files')
    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey('user', on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.name
class Answer(models.Model):
    anwerer = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.text

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    rezome = models.FileField(null=True, blank=True, upload_to='files')
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    education  = models.CharField(max_length=12)
    interst = models.ForeignKey('Category', on_delete=models.CASCADE)
    def __str__(self):
        return self.last_name

class Question(models.Model):
    asker = models.ForeignKey('User', on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField()
    answer= models.ForeignKey('Answer', on_delete=models.CASCADE)
    def __str__(self):
        return self.text