from django.contrib import admin
from django.urls import path , include
from myproject import views

#File Upload
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),   
    path('', views.start,name='start_page'),
    path('extend/', views.extend,name='extend_page'),
    
    path('book/', include('bookApp.urls')),

    path('new/', include('newapp.urls')),

    path('web/', include('web.urls')),

    path('user/', include('authenticate.urls')),



]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

