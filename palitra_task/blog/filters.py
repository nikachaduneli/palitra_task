from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import DateFilter
from .models import Blog


class BlogFilterSet(FilterSet):
    start_date = DateFilter(field_name="create_date", lookup_expr='gte')
    end_date = DateFilter(field_name="create_date", lookup_expr='lte')

    class Meta:
        model = Blog
        fields = ['author', 'category', 'tags', 'start_date', 'end_date']
