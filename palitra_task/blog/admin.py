from django.contrib import admin
from .models import Tag, Category, Menu, Blog, Comment

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Blog)
admin.site.register(Comment)