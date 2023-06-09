from rest_framework import serializers
from .models import Product, Review, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name products_count'.split()


class ProductReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title rating'.split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


