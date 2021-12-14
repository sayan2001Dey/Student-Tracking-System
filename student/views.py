from django.shortcuts import redirect, render, get_object_or_404
from activity.models import Activity
from django.db.models import Q
from django.utils.dateparse import parse_date
from skills.models import Skills
from .models import Semester
from teacher.models import Teacher

from .decorator import is_student
from django.contrib.auth.decorators import login_required



@login_required(login_url='authentication:login')
@is_student
def dashboard(request):
    all_teacher = Teacher.objects.all()
    all_skills = Skills.objects.filter(user=request.user)
    all_activity = Activity.objects.filter(user=request.user)
    recent_activity = all_activity.distinct().order_by('-date')[:20]
    my_activity = Activity.objects.filter(user=request.user)
    semesters = Semester.objects.filter(user=request.user.student)

    context = {
        'student': request.user.student,
        'activities': recent_activity,
        'my_activity': my_activity,
        'all_teacher':all_teacher,
        'all_skills': all_skills,
        'semesters': semesters,
    }
    return render(request, 'StudentProfile.html', context)


@login_required(login_url='authentication:login')
@is_student
def update_profile(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        reg_no = request.POST.get('reg_no')
        roll_no = request.POST.get('roll_no')
        education = request.POST.get('education')
        year = request.POST.get('year')
        location = request.POST.get('location')
        projects = request.POST.get('projects')
        exp = request.POST.get('exp')
        skills = request.POST.get('skills')
        img_profile = request.FILES.get('img_profile')
        teacher = request.POST.get('teacher')
        department = request.POST.get('department')

        student = request.user.student

        student.user.first_name = name
        student.user.email = email
        student.reg_no = reg_no
        student.roll_no = roll_no
        student.education = education
        student.year = int(year)
        student.location = location
        student.projects = projects
        student.exp = exp
        Skills.objects.create(user=request.user, skill=skills)
        student.department = department

        if img_profile is not None:
            student.img_profile = img_profile
        if teacher:
            teach = Teacher.objects.get(id=int(teacher))
            student.teacher = teach

        student.save()
        request.user.save()

        return redirect('student:dashboard')



@login_required(login_url='authentication:login')
@is_student
def add_activity(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        activity = request.POST.get('activity')
        file = request.FILES.get('file')

        Activity.objects.create(user=request.user, name=name, date=date, activity=activity, file=file)

        return redirect('student:dashboard')



@login_required(login_url='authentication:login')
@is_student
def edit_activity(request, id):
    if request.method == 'POST':
        activity = get_object_or_404(Activity, id=id)
        name = request.POST.get('name')
        date = request.POST.get('date')
        act = request.POST.get('activity')
        file = request.FILES.get('file', activity.file)

        activity.name = name
        activity.date = date
        activity.activity = act
        activity.file = file
        activity.save()

        return redirect('student:dashboard')

