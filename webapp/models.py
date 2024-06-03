from django.db import models
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    title = models.CharField(max_length=200, default='Default Title')
    title_desck = models.CharField(max_length=500, default='Default Title Description')
    photo = models.ImageField(upload_to='photos/', default='default.jpg')
    top = models.BooleanField(default=False)
    author = models.CharField(max_length=100, default='Default Author')
    photo_autor = models.ImageField(upload_to='author_photos/', default='default_author.jpg')
    name_object = models.CharField(max_length=200, default='Default Object Name')
    kind_object = models.CharField(max_length=200, default='Default Kind Object')
    name_cost = models.CharField(max_length=200, default='Default Cost Name')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = RichTextField(default='Default description')

    def __str__(self):
        return self.title
