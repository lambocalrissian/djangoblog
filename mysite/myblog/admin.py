# Register your models here.
from django.contrib import admin # <- this is already there.
from myblog.models import Post
from myblog.models import Category

admin.site.register(Post)
admin.site.register(Category)

