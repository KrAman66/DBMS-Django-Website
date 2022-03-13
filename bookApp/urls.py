from django.urls import path
from bookApp import views


urlpatterns = [
        path('book_home/', views.book_home,name='book_home'), #static path
        path('book_display', views.book_display,name='book_display'),
        path('book_display/edit/<int:id>', views.book_update,name='book_update'), #dynamic path
        path('book_display/delete/<int:id>', views.book_delete,name='book_delete'),
        path('find/', views.find_book,name='find_book'),
        path('search/', views.srch_book,name='search'),



]

