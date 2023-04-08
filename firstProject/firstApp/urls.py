from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('blog/', views.BlogsAPIView.as_view()),
    path('blog/<int:pk>/', views.BlogAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)