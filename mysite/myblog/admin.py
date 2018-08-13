# Register your models here.
from django.contrib import admin # <- this is already there.
from myblog.models import Post
from myblog.models import Category
from django.contrib import admin

from myblog.models import Post
from myblog.models import Category

# Create a customized ModelAdminLinks to an external site. class for the Post and Category models
class CategoryAdmin(admin.ModelAdmin):
    # Impacting the category form

    fields = ('name', 'description')
    exclude = ('posts',)


class CategoryInline(admin.TabularInline):
    model = Post.categories.through


class PostAdmin(admin.ModelAdmin):
    # this affects the add post form, not the list of posts

    fields = ('title', 'text', 'author')
    inlines = [
        CategoryInline,
    ]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
# admin.site.register(Post)
# admin.site.register(Category)

