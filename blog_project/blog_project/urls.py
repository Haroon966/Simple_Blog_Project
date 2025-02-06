from django.contrib import admin
from django.urls import path, include
from blog.views import home  # Import the home view

urlpatterns = [
    path('', home, name='home'),  # Add this line to route the home view
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),
]