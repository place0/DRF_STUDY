from .models import Blog, BlogImage
from rest_framework import serializers

class BlogImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = BlogImage
        fields = ('id', 'image')

class BlogSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(max_length=None, allow_empty_file=True, required=False), required=False)

    class Meta:
        model = Blog
        fields = ('id', 'title', 'created', 'images')

    def create(self, validated_data):
        images = validated_data.pop('images', None)
        instance = Blog.objects.create(**validated_data)
        if images:
            for image_data in images:
                BlogImage.objects.create(blog=instance, image=image_data)
        else:
            BlogImage.objects.create(blog=instance, image=BlogImage.default_image())
        return instance

class DetailSerializer(serializers.ModelSerializer):
    images = BlogImageSerializer(source='blogimage_set', many=True, read_only=True)
    
    class Meta:
        model = Blog
        fields = ('id', 'title', 'body', 'created', 'images')

class CreateSerializer(serializers.ModelSerializer):
    images = serializers.ListField(
        child=serializers.ImageField(max_length=None, allow_empty_file=True, required=False), 
        required=False
    )

    class Meta:
        model = Blog
        fields = ('title', 'body', 'images')
        extra_kwargs = {
            'title': {'required': False},
            'body': {'required': False},
            'images': {'required': False},
        }

    def create(self, validated_data):
        images = validated_data.pop('images', None)
        instance = Blog.objects.create(**validated_data)
        if images:
            for image_data in images:
                BlogImage.objects.create(blog=instance, image=image_data)
        else:
            BlogImage.objects.create(blog=instance, image=BlogImage.default_image())
        return instance