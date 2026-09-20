from django.contrib.auth import authenticate
from django.contrib import messages

from django.shortcuts import render, redirect

from adminPanel.models import Course, Student, Fee, Result



def admin_panel(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    total_students = Student.objects.all().count()
    total_course = Course.objects.all().count()
    context = {
        "total_course": total_course,
        "total_students": total_students,
    }
    return render(request, "adminPanel/dashboard.html", context)



def newCourse(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    if request.method == "POST":
        post = request.POST
        data = Course()
        data.course_code = post.get("course_code")
        data.course_name = post.get("course_name")
        data.duration = post.get("duration")
        data.description = post.get("description")
        if Course.objects.filter(course_code=data.course_code).exists():
            messages.error(request, 'Course code already exists....')
        else:
            data.save()
            messages.success(request, 'Course Added successfully....')
    return render(request, "adminPanel/newCourse.html")


def courseList(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    course_list = Course.objects.all()
    context = {
        "list": course_list
    }
    return render(request, "adminPanel/courseList.html", context)



def update_course(request, id):
    if request.user.is_anonymous:
        return redirect("admin_login")
    data = Course.objects.filter(id=id)[0]
    context = {
        "data": data
    }
    if request.method == "POST":
        post = request.POST
        data = Course.objects.filter(id=id)[0]
        data.course_code = post.get("course_code")
        data.course_name = post.get("course_name")
        data.duration = post.get("duration")
        data.description = post.get("description")
        data.save()
        messages.success(request, 'Course Updated successfully....')
        data = Course.objects.filter(id=id)[0]
        context = {
            "data": data
        }
        return redirect("/adminPanel/courseList/")

    return render(request, "adminPanel/update_course.html", context)


def delete_course(request, id):
    if request.user.is_anonymous:
        return redirect("admin_login")
    Course.objects.filter(id=id)[0].delete()
    messages.error(request, 'Course Deleted successfully....')
    course_list = Course.objects.all()
    context = {
        "list": course_list
    }

    return redirect("/adminPanel/courseList/")




def newStudent(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    course = Course.objects.all()
    context = {
        "course": course
    }
    if request.method == "POST":
        post = request.POST

        data = Student()
        data.roll_no = post.get("roll_no")
        data.student_name = post.get("student_name")
        data.fathers_name = post.get("fathers_name")
        data.mothers_name = post.get('mothers_name')
        data.dob = post.get('dob')
        data.gender = post.get('gender')
        data.mob_no = post.get('mob_no')
        data.email_id = post.get('email_id')
        data.address = post.get('address')
        data.admission_date = post.get('admission_date')
        data.course_id = post.get('course_id')
        data.session = post.get('session')
        data.fee = post.get('fee')
        if len(request.FILES) != 0:
            data.photo = request.FILES['photo']

        if Student.objects.filter(roll_no=data.roll_no).exists() and Student.objects.filter(email_id=data.email_id).exists():
            messages.error(request, 'Roll number and Email Id both already exists!')
        elif Student.objects.filter(roll_no=data.roll_no).exists():
            messages.error(request, 'Roll number already exists!')
        elif Student.objects.filter(email_id=data.email_id).exists():
            messages.error(request, 'Email Id already exists!')
        else:
            data.save()
            messages.success(request, 'Student Data Added successfully....')
    return render(request, "adminPanel/newStudent.html", context)



def studentList(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    student_list = Student.objects.all()
    final_student = []
    for student in student_list:
        student.course_id = Course.objects.filter(id=student.course_id).values('course_code')
        final_student.append(student)

    context = {
        "list": final_student
    }
    return render(request, 'adminPanel/studentList.html', context)

def update_student_data(request, id):
    if request.user.is_anonymous:
        return redirect("admin_login")
    course = Course.objects.all()
    data = Student.objects.filter(id=id)
    dob = data[0].dob
    dob = dob.strftime("%Y-%m-%d")
    admission_date = data[0].admission_date
    admission_date = admission_date.strftime("%Y-%m-%d")
    my_data = data[0]
    my_data.dob = dob
    my_data.admission_date = admission_date
    context = {
        "data": my_data,
        "course": course
    }
    if request.method == "POST":
        post = request.POST
        data = Student.objects.filter(id=id)[0]
        data.roll_no = post.get("roll_no")
        data.student_name = post.get("student_name")
        data.fathers_name = post.get("fathers_name")
        data.mothers_name = post.get('mothers_name')
        data.dob = post.get('dob')
        data.gender = post.get('gender')
        data.mob_no = post.get('mob_no')
        data.email_id = post.get('email_id')
        data.address = post.get('address')
        data.admission_date = post.get('admission_date')
        data.course_id = post.get('course_id')
        data.session = post.get('session')
        data.fee = post.get('fee')
        if len(request.FILES) != 0:
            data.photo = request.FILES['photo']
        data.save()
        messages.success(request, 'Student Data Updated successfully....')
        data = Student.objects.filter(id=id)[0]
        context = {
            "data": data
        }
        return redirect("/adminPanel/studentList/")

    return render(request, "adminPanel/update_student_data.html", context)


def delete_student_data(request, id):
    if request.user.is_anonymous:
        return redirect("admin_login")
    stud_data = Student.objects.filter(id=id)[0]
    roll = stud_data.roll_no
    fee_data = Fee.objects.filter(roll_no=roll)
    result_data = Result.objects.filter(roll_no=roll)
    if fee_data.exists():
        Fee.objects.filter(roll_no=roll).delete()
    if result_data.exists():
        Result.objects.filter(roll_no=roll).delete()
    Student.objects.filter(id=id).delete()
    messages.error(request, "Student data deleted successfully...")
    return redirect("/adminPanel/studentList/")


def fee(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    student_list = Student.objects.all()
    final_list = []
    for student in student_list:
        student.course_id = Course.objects.filter(id=student.course_id).values('course_code')
        final_list.append(student)

    context = {
        "list" : final_list
    }
    return render(request, 'adminPanel/fee.html', context)


def receive_fee(request, id):
    if request.user.is_anonymous:
        return redirect("admin_login")
    data = Student.objects.filter(roll_no=id)
    my_data = data[0]

    amount = Fee.objects.filter(roll_no=id)
    total_paid = 0
    for amt in amount:
        total_paid += int(amt.amount)
    my_data.dues_amount = int(my_data.fee) - total_paid
    all_list = Fee.objects.filter(roll_no=id)
    context = {
        "list": my_data,
        "all_list": all_list
    }
    if request.method == "POST":
        post = request.POST
        fee = Fee()
        fee.roll_no = post.get('roll_no')
        fee.payment_date = post.get('payment_date')
        fee.amount = post.get('amount')
        fee.save()
        messages.success(request, "Fee received successfully....")
        return redirect("/adminPanel/receive_fee/" + id)
    return render(request, 'adminPanel/receive_fee.html', context)



def delete_fee(request, id):
    if request.user.is_anonymous:
        return redirect("admin_login")
    fee = Fee.objects.get(id=id)
    fee.delete()
    return redirect("/adminPanel/fee")



def add_result(request, id):
    if request.user.is_anonymous:
        return redirect("admin_login")
    student = Student.objects.all()
    data = Student.objects.filter(roll_no=id)
    course = Course.objects.filter(id=data[0].course_id)[0]

    my_data = data[0]
    context = {
        "student": student,
        "list": my_data,
        'course': course.course_code
    }

    if request.method == "POST":
        post = request.POST

        result = Result()
        result.roll_no = post.get("roll_no")
        result.issue_date = post.get("issue_date")
        result.passing_date = post.get("passing_date")
        result.assignment_marks = post.get("assignment_marks")
        result.theory_marks = post.get("theory_marks")
        result.practical_marks = post.get("practical_marks")
        if Result.objects.filter(roll_no=result.roll_no).exists():
            messages.error(request, 'Marksheet of this Roll number already exists!')
        else:
            result.save()
            messages.success(request, 'Result Added successfully....')

    return render(request, 'adminPanel/add_result.html', context)

def marksList(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    marks_list = Result.objects.all()
    final_data = []
    for marks in marks_list:
        student = Student.objects.filter(roll_no=marks.roll_no).first()
        if student:
            student_data = {
                "roll_no" : student.roll_no,
                "student_name" : student.student_name,
                "course_id" : Course.objects.filter(id=student.course_id).values('course_code'),
                "passing_date" : marks.passing_date,
                "total_marks" : float(marks.assignment_marks or 0) + float(marks.theory_marks or 0) + float(marks.practical_marks or 0),
            }

            final_data.append(student_data)
    context = {
        "list": final_data
    }
    return render(request, 'adminPanel/marksList.html', context)



def update_marks(request, id):
    if request.user.is_anonymous:
        return redirect("admin_login")
    student = Student.objects.all()
    data = Student.objects.filter(roll_no=id)
    course = Course.objects.filter(id=data[0].course_id)[0]
    marks = Result.objects.filter(roll_no=id)

    passing_date = marks[0].passing_date
    passing_date = passing_date.strftime("%Y-%m-%d")
    issue_date = marks[0].issue_date
    issue_date = issue_date.strftime("%Y-%m-%d")
    my_marks = marks[0]
    my_marks.passing_date = passing_date
    my_marks.issue_date = issue_date

    my_data = data[0]
    context = {
        "student": student,
        "list": my_data,
        "marks": my_marks,
        'course': course.course_code
    }

    if request.method == "POST":
        post = request.POST

        result = Result.objects.filter(roll_no=id)[0]
        result.roll_no = post.get("roll_no")
        result.issue_date = post.get("issue_date")
        result.passing_date = post.get("passing_date")
        result.assignment_marks = post.get("assignment_marks")
        result.theory_marks = post.get("theory_marks")
        result.practical_marks = post.get("practical_marks")
        result.save()
        messages.success(request, "Marks details successfully updated...")
        return redirect("/adminPanel/marksList")
    return render(request, 'adminPanel/update_marks.html', context)



def change_password(request):
    if request.user.is_anonymous:
        return redirect("admin_login")
    if request.method == "POST":
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        user = authenticate(username=request.user.username, password=old_password)
        if user is not None:
            if new_password == confirm_password:
                request.user.set_password(new_password)
                request.user.save()
                messages.success(request, 'Password changed successfully!')
                return redirect('admin_login')  # Redirect to admin login page
            else:
                messages.error(request, 'New password and confirm password do not match.')
        else:
            messages.error(request, 'Incorrect old password.')
    return render(request, 'adminPanel/change_password.html')
