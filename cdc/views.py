from django.shortcuts import render
from student.models import Student

from django.contrib.auth.decorators import login_required
from .decorator import is_cdc


@login_required(login_url='authentication:login')
@is_cdc
def dashboard(request):
    students = Student.objects.all()

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
    }
    return render(request, 'cdc_profile.html', context)