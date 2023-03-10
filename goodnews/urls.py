from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path('about/', views.about, name="about"),
    path('event/', views.event, name="event"),
    path('support/', views.support, name="support"),
    path('contact/', views.contact, name="contact"),
]