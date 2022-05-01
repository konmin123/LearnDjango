from django.urls import path

from . import views

urlpatterns = [
    path('datetime/', views.SimpleView.as_view()),
    path('SayHi/', views.SimpleView1.as_view()),
]
