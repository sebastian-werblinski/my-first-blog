from django.urls import path
from . import views

# Define URL patterns for the blog app
urlpatterns = [
    path('',views.post_list, name='post_list'),
]