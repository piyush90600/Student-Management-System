from adminPanel.urls import path
from front import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('student_verify/', views.student_verify, name='student_verify'),
    path('view_result/', views.view_result, name='view_result'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
]