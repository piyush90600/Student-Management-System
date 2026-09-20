from django.urls import path

from adminPanel import views



urlpatterns = [
    path('', views.admin_panel, name='adminPanel'),
    path('adminPanel/', views.admin_panel, name='adminPanel'),
    path('newCourse/', views.newCourse, name='newCourse'),
    path('courseList/', views.courseList, name='courseList'),
    path('update_course/<id>', views.update_course, name='update_course'),
    path('delete_course/<id>', views.delete_course, name='delete_course'),
    path('newStudent/', views.newStudent, name='newStudent'),
    path('studentList/', views.studentList, name='studentList'),
    path('update_student_data/<id>', views.update_student_data, name='update_student_data'),
    path('delete_student_data/<id>', views.delete_student_data, name='delete_student_data'),
    path('fee/', views.fee, name='fee'),
    path('receive_fee/<id>', views.receive_fee, name='receive_fee'),
    path('delete_fee/<id>', views.delete_fee, name='delete_fee'),
    path('add_result/<id>', views.add_result, name='add_result'),
    path('marksList/', views.marksList, name='marksList'),
    path('update_marks/<id>', views.update_marks, name='update_marks'),
    path('change_password/', views.change_password, name='change_password'),
]




