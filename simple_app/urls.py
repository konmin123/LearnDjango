
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datetime/', views.SimpleView.as_view()),
    path('blog/', views.SimpleView1.as_view()),
]
