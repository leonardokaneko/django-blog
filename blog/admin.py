from django.contrib import admin
from blog.models import Posts, Category, Profile

# Register your models here.
admin.site.register(Posts)
admin.site.register(Category)
admin.site.register(Profile)
