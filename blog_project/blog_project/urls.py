from django.contrib import admin
from django.urls import path, include
from blog.views import home  # Import the home view

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]