"""college URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from student import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentregister/',views.studentRegister,name='Author'),
    path('student/data',views.studentData,name='data'),
    path('student/update/<int:uid>/',views.studentUpdate,name= 'update'),
    path('student/delete/<int:uid>/',views.studentDelete ,name='delete'),
    path('faculty/',include('faculty.urls')),
    path('student/addBook/', views.addBook,name='library'),
    path("" , views.home,name='home'),
    path("library/boooks",views.viewBooks,name="books"),
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
