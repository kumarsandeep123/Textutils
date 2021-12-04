from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.san, name='san'),
    path('analyze', views.analyze, name='analyze'),




]
