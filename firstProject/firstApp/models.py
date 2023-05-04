from django.db import models
from django.conf import settings

class Blog(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(default='media/blog/default_image.jpeg', upload_to='blog', null=True)

    def update(self, **kwargs):
        self.image = kwargs.get('image', self.image)
        self.save()
        return self