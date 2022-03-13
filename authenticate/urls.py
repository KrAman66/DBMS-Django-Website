from django.urls import path
from authenticate import views

urlpatterns = [
    path('index/',views.home,name='home'),
    path('tea_register/',views.teacher_register,name='tea_register'),
    path('stu_register/',views.student_register,name='stu_register'),
    path('tea_login/',views.teacher_login,name='tea_login'),
    path('stu_login/',views.student_login,name='stu_login'),
    path('logout/',views.user_logout,name='logout'),
    path('stu_profile/',views.user_profile,name='stu_profile'),
    path('tea_profile/',views.admin_profile,name='tea_profile'),
    path('change_user/',views.change_user,name='change_user'),
    # path('password/',views.change_pass,name='password'),



]
