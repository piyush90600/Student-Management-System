from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from adminPanel.models import Course, Student, Result
from front.models import Contact


# Create your views here.
def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'front/index.html')



def home(request):
    return render(request, 'front/home.html')


def about_us(request):
    return render(request, 'front/about_us.html')



def student_verify(request):
    data = None
    course = None
    student_info = False
    if request.method == "POST":
        post = request.POST
        roll_no = post.get('roll_no')
        data = Student.objects.filter(roll_no=roll_no)
        if data.exists():
            course = Course.objects.filter(id=data[0].course_id)
            messages.success(request, "Verify Successfully")
            student_info = True
        else:
            messages.error(request, "Student Doesn't found! Please enter Valid Roll Number")
            return render(request, 'front/student_verify.html')
    return render(request, 'front/student_verify.html', {'data': data, 'course': course, 'student_info': student_info})



def view_result(request):
    data = None
    course = None
    result = None
    student_result = False
    if request.method == "POST":
        post = request.POST
        roll_no = post.get('roll_no')
        data = Student.objects.filter(roll_no=roll_no)

        result = Result.objects.filter(roll_no=roll_no)
        if data.exists():
            course = Course.objects.filter(id=data[0].course_id)
            student_result = True
        else:
            messages.error(request, "Result Doesn't found! Please enter Valid Roll Number")
            return render(request, 'front/view_result.html')
    return render(request, 'front/view_result.html', {'data': data, 'course': course, 'result': result, 'student_result': student_result})




def contact_us(request):
    course = Course.objects.all()
    context = {
        "course": course
    }
    if request.method == "POST":
        post = request.POST

        data = Contact()
        data.name = post.get("name")
        data.phone_no = post.get("phone_no")
        data.email_id = post.get("email_id")
        data.course_id = post.get("course_id")
        data.message = post.get("message")
        if (Contact.objects.filter(phone_no=data.phone_no).exists() and Contact.objects.filter(email_id=data.email_id)
                .exists()):
            messages.error(request, 'Phone number and Email Id both already used! Please enter another Phone '
                                    'Number and Email Id.')
        elif Contact.objects.filter(phone_no=data.phone_no).exists():
            messages.error(request, 'Phone number already used!  Please enter another Phone Number')
        elif Contact.objects.filter(email_id=data.email_id).exists():
            messages.error(request, 'Email Id already used!  Please enter another Email Id.')
        else:
            data.save()
            messages.success(request, 'Thank you for your inquiry! Your contact information and message was '
                                      'successfully submitted')
    return render(request, 'front/contact_us.html', context)



def admin_login(request):
    if request.method == "POST":
        post = request.POST
        username = post.get('username')
        password = post.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/adminPanel')
        else:
            messages.success(request, "Invalid username or password")
            return render(request, 'front/admin_login.html')
    return render(request, 'front/admin_login.html')


def user_logout(request):
    logout(request)
    return redirect("admin_login")




