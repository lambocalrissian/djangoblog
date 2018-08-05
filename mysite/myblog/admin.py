from django.contrib import admin

# Register your models here.
from django.contrib import admin # <- this is already there.
from myblog.models import Post

admin.site.register(Post)