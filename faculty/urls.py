from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='register' ),
    path('data/',views.facultyData,name='facultyData'),
    path('update/<int:uid>/',views.facultyUpdate,name = 'facultyUpdate'),
    path('delete/<int:uid>',views.facultyDelete, name='facultyDelete'),
]