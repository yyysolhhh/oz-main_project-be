from rest_framework import generics, permissions

from apps.category.models import Category
from apps.category.serializers import CategorySerializer


class CategoryListView(generics.ListAPIView[Category]):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None
