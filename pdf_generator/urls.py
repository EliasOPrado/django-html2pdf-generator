from django.contrib import admin
from django.urls import path
from .views import index, render_pdf
urlpatterns = [
    path('', index, name='index'),
    path('download', render_pdf, name='render_pdf'),
]