from django.contrib import admin
from .models import Blog, BlogImage

class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline]

admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogImage)