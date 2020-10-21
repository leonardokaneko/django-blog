from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Posts(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='media/uploads/%Y/%m/%d', blank=True)
    summary = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


def get_full_name(self):
    return str(f'{self.first_name} {self.last_name}')


User.add_to_class('__str__', get_full_name)
