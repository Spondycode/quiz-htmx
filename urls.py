"""
URL configuration for a_core project.
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', include('a_sim.urls')),
]
