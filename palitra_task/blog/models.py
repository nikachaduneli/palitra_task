from django.db import models
from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=100)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def __str__(self): return self.title


class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self): return self.title


class Blog(models.Model):
    title = models.CharField(max_length=100)
    main_image = models.ImageField()
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    tags = models.ManyToManyField(Tag, related_name='blogs')
    create_date = models.DateTimeField(auto_now_add=True)
    active_status = models.BooleanField(default=True)

    def __str__(self): return self.title


class Menu(models.Model):
    title = models.CharField(max_length=100)
    position = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menus', blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self): return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)
    likes_count = models.PositiveIntegerField(default=0)
    dislikes_count = models.PositiveIntegerField(default=0)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self): return f'{self.blog.title} comment'