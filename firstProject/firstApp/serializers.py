from .models import Blog
from rest_framework import serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'created')

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'body', 'created')

class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'body')