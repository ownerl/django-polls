from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_baby, name='index'),
    path('britney/', views.hit_me_baby_one_more_time, name='britney')
]