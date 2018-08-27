from django.urls import path
from . import views



urlpatterns = [
    path('<int:page_id>/<slug:page_slug>/', views.page, name="page"), #Vista dinamica para las paginas
]