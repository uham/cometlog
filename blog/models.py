from django.urls import reverse
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from django.contrib.auth.models import User

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

    def __str__(self):
        return self.subject


class Post(models.Model):
    subject = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    category = TreeForeignKey(
        Category,
        related_name='posts',
        on_delete=models.CASCADE
    )
    slug = models.SlugField(max_length=256, null=False, unique=True, allow_unicode=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={"slug":self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.subject, allow_unicode=True)
        return super().save(*args, **kwargs)

class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content