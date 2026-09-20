from django.contrib import admin

from adminPanel.models import Course, Student, Fee, Result

# Register your models here.
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Fee)
admin.site.register(Result)
