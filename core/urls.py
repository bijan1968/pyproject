
from django.urls import path

from.views import Home,Add_Student,Delete_Student,EditStudent,Reg


urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('register/',Reg.as_view(),name='register'),
    path('add_Student/',Add_Student.as_view(),name='add_student'),
    path('delete_student/',Delete_Student.as_view(),name='delete_student'),
    path('edit_student/<int:id>/',EditStudent.as_view(),name='edit_student'),

]