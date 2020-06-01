from django.contrib import admin
from django.urls import path,include
from blog import views


urlpatterns = [
    path('',views.allblogs,name='allblogs'),
    path('<int:blog_id>/',views.details,name='details'),

]