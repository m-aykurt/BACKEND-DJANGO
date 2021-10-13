from django.contrib import admin
from django.urls.conf import path
from .views import home
urlpatterns = [
    path("",home)
]

