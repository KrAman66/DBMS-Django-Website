from django.urls import path
from web import views

urlpatterns = [
    path('main/',views.main,name='main'),
    # path('student/',views.stu_info,name='stu_info'),
    # path('teacher/',views.tea_info,name='tea_info'),
    path('student/',views.student_details,name='student'),
    path('portal/',views.portal,name='portal'),
    path('display/',views.display_student,name='display'),
    path('display/edit/<int:id>',views.update_student,name='update'),
    path('display/delete/<int:id>',views.delete_student,name='delete'),
    path('result/',views.student_result,name='result'),
    path('display_result/',views.display_result,name='display_result'),
    path('display_result/edit/<int:roll>',views.update_result,name='update_result'),
    path('display_result/delete/<int:roll>',views.delete_result,name='delete_result'),
    path('add_result/<int:id>',views.result,name='add_result'),
    path('stu_portal/',views.student_portal,name='stu_portal'),
    path('search_result/',views.search_result,name='search_result'),
    path('search_student/',views.search_student,name='search_student'),
    path('chart/',views.graph_chart,name='chart'),
    path('graph/',views.chart,name='graph'),
    path('standard/',views.standard,name='standard'),



]
