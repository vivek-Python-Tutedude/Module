# we have to create this file by default it does not exists

from django.urls import path
from . import views
urlpatterns = [
    path("", views.home_page),
    path('allposts', views.blogposts),
    path("python-intro", views.python_intro),
    path("allposts/django-basics", views.django_basic)
]

# after this we have to go inside the urls.py which is inside the mywebsite