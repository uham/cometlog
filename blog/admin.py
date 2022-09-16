from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from blog.models import Category, Post

# Register your models here.
admin.site.register(Category, DraggableMPTTAdmin)
admin.site.register(Post)