from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .models import Blog
from .serializers import BlogSerializer, DetailSerializer, CreateSerializer

#글 작성 및 수정, 전체 목록보기
class BlogsAPIView(APIView):
	def get(self,request):
		blogs = Blog.objects
		serializer = BlogSerializer(blogs, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self,request):
		serializer = CreateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogAPIView(APIView):
	def get(self, request, pk):
		blog = get_object_or_404(Blog, id=pk)
		serializer = DetailSerializer(blog)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, pk):
		blog = get_object_or_404(Blog, id=pk)
		blog.delete()
		return Response()