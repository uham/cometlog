from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Category(MPTTModel):
    subject = models.CharField(max_length=128, unique=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    
    class MPTTMeta:
        order_insertion_by = ['subject']

class Post(models.Model):
    subject = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    category = TreeForeignKey(
        Category,
        related_name='posts',
        on_delete=models.CASCADE
    )
    slug = models.SlugField(max_length=126)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
