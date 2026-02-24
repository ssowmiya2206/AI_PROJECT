from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Avg
from .models import Student
from .ai_model import predict_performance


# Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# Dashboard
@login_required
def dashboard(request):
    students = Student.objects.all()
    total = students.count()
    avg_marks = students.aggregate(Avg('marks'))['marks__avg'] or 0

    context = {
        'students': students,
        'total': total,
        'avg_marks': round(avg_marks, 2),
    }
    return render(request, 'dashboard.html', context)


# Add Student
@login_required
def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            marks=request.POST['marks'],
            attendance=request.POST['attendance']
        )
        return redirect('dashboard')

    return render(request, 'student_form.html')


# AI Result
@login_required
def result(request, student_id):
    student = Student.objects.get(id=student_id)
    prediction = predict_performance(student.marks, student.attendance)

    return render(request, 'result.html', {
        'student': student,
        'prediction': prediction
    })