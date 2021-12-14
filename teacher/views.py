from django.shortcuts import render, redirect, get_object_or_404
from activity.models import Activity
from django.db.models import Q
import operator
from skills.models import Skills
from student.models import Student, Semester
from django.contrib.auth.decorators import login_required
from .decorator import is_teacher



@login_required(login_url='authentication:login')
@is_teacher
def dashboard(request):
    all_students = request.user.teacher.get_all_student()
    all_activites = []
    all_skills = Skills.objects.filter(user=request.user)

    activity = Activity.objects.filter(user=request.user)
    if activity.exists():
        for i in activity:
            if i not in all_activites:
                all_activites.append(i)

    if all_students:
        for student in all_students:
            act = Activity.objects.filter(user=student.user)
            if act.exists():
                for x in act:
                    if x not in all_activites:
                        all_activites.append(x)

    data = sorted(all_activites, key=operator.attrgetter('date'))    
    
    context = {
        'teacher': request.user.teacher,
        'activities': data[:20],
        'all_skills': all_skills,
    }
    return render(request, 'TeacherProfile.html', context)



@login_required(login_url='authentication:login')
@is_teacher
def update_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        education = request.POST.get('education')
        location = request.POST.get('location')
        projects = request.POST.get('projects')
        exp = request.POST.get('exp')
        skills = request.POST.get('skills')
        department = request.POST.get('department')
        img_profile = request.FILES.get('img_profile')

        teacher = request.user.teacher

        teacher.user.first_name = name
        teacher.user.email = email
        teacher.education = education
        teacher.location = location
        teacher.projects = projects
        teacher.exp = exp
        Skills.objects.create(user=request.user, skill=skills)
        teacher.department = department

        if img_profile:
            teacher.img_profile = img_profile

        teacher.save()
        request.user.save()

        return redirect('teacher:dashboard')



@login_required(login_url='authentication:login')
@is_teacher
def add_activity(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        activity = request.POST.get('activity')
        file = request.FILES.get('file')

        Activity.objects.create(user=request.user, name=name, date=date, activity=activity, file=file)

        return redirect('teacher:dashboard')



@login_required(login_url='authentication:login')
@is_teacher
def all_students(request):
    students = Student.objects.filter(teacher=request.user.teacher)

    mechanical = Student.objects.filter(department='mechanical').count()
    civil = Student.objects.filter(department='civil').count()
    electrical = Student.objects.filter(department='electrical').count()
    electronics = Student.objects.filter(department='electronics').count()
    computer = Student.objects.filter(department='computer').count()
    pharmacy = Student.objects.filter(department='pharmacy').count()

    context = {
        'students': students,
        'mechanical': mechanical,
        'civil': civil,
        'electrical': electrical,
        'electronics': electronics,
        'computer': computer,
        'pharmacy': pharmacy,
        'teacher': request.user.teacher
    }
    return render(request, 'students_profile.html', context)


@login_required(login_url='authentication:login')
@is_teacher
def add_marks(request, id_student):
    if request.method == 'POST':
        std = get_object_or_404(Student, id=id_student)
        for i in range(1,9):
            mark = request.POST.get('sem-' + str(i), None)
            if mark:
                semester = get_object_or_404(Semester, user=std, semester=i)
                semester.marks = mark
                semester.save()
    return redirect('teacher:all_students')



@login_required(login_url='authentication:login')
@is_teacher
def add_attendance(request, id_student):
    if request.method == 'POST':
        std = get_object_or_404(Student, id=id_student)
        for i in range(1,9):
            attendance = request.POST.get('sem-' + str(i), None)
            if attendance:
                semester = get_object_or_404(Semester, user=std, semester=i)
                semester.attendance = attendance
                semester.save()
    return redirect('teacher:all_students')