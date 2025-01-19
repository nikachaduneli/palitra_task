from rest_framework.serializers import  ModelSerializer
from .models import Comment, Menu, Blog, Category, Tag


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        extra_kwargs = {'author': {'required': False, 'allow_null': True} }


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'