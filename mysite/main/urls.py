from django.urls import path
from main.views import *


urlpatterns = [
    path('', index),
    path('about/', about),
    path('categories/', categories),
    path('contacts/', contacts)
]