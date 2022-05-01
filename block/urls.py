from django.urls import path

from . import views

urlpatterns = [
    path('blocks/', views.BlogApiView.as_view()),
]
