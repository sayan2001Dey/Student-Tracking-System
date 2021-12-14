from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from student.models import Student, Semester
from teacher.models import Teacher



def index(request):
    return render(request, 'home.html')




def about(request):
    return render(request, 'about.html')




def contact(request):
    return render(request, 'contact.html')




def login_view(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'student'):
            return redirect('student:dashboard')
        elif hasattr(request.user, 'teacher'):
            return redirect('teacher:dashboard')
        else:
            return redirect('cdc:dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if role == 'student':
            user = authenticate(request, username=username, password=password)
            if user is not None:
                user_temp = get_object_or_404(User, username=username)
                user_student = Student.objects.filter(user=user_temp)
                if not user_student.exists():
                    return redirect('authentication:login')
                login(request, user)
                return redirect('student:dashboard')
            else:
                return redirect('authentication:login')
        elif role == 'professor':
            user = authenticate(request, username=username, password=password)
            if user is not None:
                user_temp = get_object_or_404(User, username=username)
                user_teacher = Teacher.objects.filter(user=user_temp)
                if not user_teacher.exists():
                    return redirect('authentication:login')
                login(request, user)
                return redirect('teacher:dashboard')
            else:
                return redirect('authentication:login')
        elif role == 'cdc':
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('cdc:dashboard')
            else:
                return redirect('authentication:login')

    return render(request, 'signin.html')





def signup(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'student'):
            return redirect('student:dashboard')
        elif hasattr(request.user, 'teacher'):
            return redirect('teacher:dashboard')
        else:
            return redirect('cdc:dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if role == 'student':
            user_temp = User.objects.filter(username=username)
            if user_temp.exists():
                return redirect('authentication:login')
            user = User.objects.create_user(username=username, password=password)
            student = Student.objects.create(user=user)
            for i in range(1,9):
                Semester.objects.create(user=student, semester=i)
            return redirect('authentication:index')
        elif role == 'professor':
            user_temp = User.objects.filter(username=username)
            if user_temp.exists():
                return redirect('authentication:login')
            user = User.objects.create_user(username=username, password=password)
            Teacher.objects.create(user=user)
            return redirect('authentication:index')
    return render(request, 'signin.html')




def logout_view(request):
    logout(request)
    return redirect('authentication:login')