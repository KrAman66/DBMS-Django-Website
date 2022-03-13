from django.urls import path
from newapp import views


urlpatterns = [
        path('', views.home),
        path('dis/', views.display),
        path('dis/edit/<int:id>', views.update,name='update'),
        path('sum/', views.addition,name='Addition'),
        path('sum/result/', views.result,name='res'),




]