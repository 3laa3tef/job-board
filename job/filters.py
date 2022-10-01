import django_filters
from .models import job

class JobFilter(django_filters.FilterSet):
    describtion = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = job
        fields = '__all__'
        exclude = ['published_at', 'image', 'salary', 'vacancy','owner', 'slug']