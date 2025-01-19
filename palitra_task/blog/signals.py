from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Blog, Category, Tag, Comment, Menu
from palitra_task.mongo_utils import get_mongo_db, sync_to_mongo, delete_from_mongo
from .serializers import (
    BlogSerializer,
    CategorySerializer,
    TagSerializer,
    CommentSerializer,
    MenuSerializer
)

@receiver(post_save, sender=Blog)
def sync_blog_to_mongo(sender, instance, **kwargs):
    sync_to_mongo(instance, "blogs", serializer_class=BlogSerializer)

@receiver(post_delete, sender=Blog)
def delete_blog_from_mongo(sender, instance, **kwargs):
    delete_from_mongo(instance, "blogs")

@receiver(post_save, sender=Category)
def sync_blog_to_mongo(sender, instance, **kwargs):
    sync_to_mongo(instance, "categories", serializer_class=CategorySerializer)

@receiver(post_delete, sender=Category)
def delete_blog_from_mongo(sender, instance, **kwargs):
    delete_from_mongo(instance, "categories")


@receiver(post_save, sender=Tag)
def sync_blog_to_mongo(sender, instance, **kwargs):
    sync_to_mongo(instance, "tags", serializer_class=TagSerializer)


@receiver(post_delete, sender=Tag)
def delete_blog_from_mongo(sender, instance, **kwargs):
    delete_from_mongo(instance, "tags")

@receiver(post_save, sender=Menu)
def sync_blog_to_mongo(sender, instance, **kwargs):
    sync_to_mongo(instance, "menus", serializer_class=MenuSerializer)


@receiver(post_delete, sender=Menu)
def delete_blog_from_mongo(sender, instance, **kwargs):
    delete_from_mongo(instance, "menus")


@receiver(post_save, sender=Comment)
def sync_blog_to_mongo(sender, instance, **kwargs):
    sync_to_mongo(instance, "comments", serializer_class=CommentSerializer)


@receiver(post_delete, sender=Comment)
def delete_blog_from_mongo(sender, instance, **kwargs):
    delete_from_mongo(instance, "comments")




