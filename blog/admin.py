from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from blog.models import Category, Comment, Post

# Register your models here.
admin.site.register(Category, DraggableMPTTAdmin)
admin.site.register(Post)
admin.site.register(Comment)