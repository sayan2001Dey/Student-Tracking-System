from django.db import models
from django.contrib.auth.models import User
from teacher.models import Teacher


class Student(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year = models.IntegerField(blank=True, null=True)
    reg_no = models.BigIntegerField(blank=True, null=True)
    roll_no = models.BigIntegerField(blank=True, null=True)
    education = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    projects = models.TextField(blank=True)
    exp = models.TextField(blank=True)
    DEPT = (
        ('mechanical', 'Mechanical'),
        ('civil', 'Civil'),
        ('electrical', 'Electrical'),
        ('electronics', 'Electronics'),
        ('computer', 'Computer'),
        ('pharmacy', 'Pharmacy'),
    )
    department = models.CharField(max_length=50, choices=DEPT, blank=True, null=True)
    img_profile = models.ImageField(upload_to="profile_img/", blank=True)

    def __str__(self):
        return self.user.username

    def get_name(self):
        return self.user.first_name if self.user.first_name else self.user.username
    
    def get_len_semester(self):
        return self.semester_set.all().count()

    def get_url_image(self):
        return self.img_profile.url if self.img_profile else 'https://dummyimage.com/300.png/09f/fff'

    def get_display_skills(self):
        if self.user.skills_set.all().count() > 0:
            skills = ", ".join([x.skill for x in self.user.skills_set.all()])
        else:
            skills = "-"
        return skills

    def is_activity(self):
        return self.user.activity_set.all().count() != 0





class Semester(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    semester = models.IntegerField()
    marks = models.FloatField(blank=True, null=True)
    attendance = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.user) + ' | ' + str(self.semester)

    def get_marks(self):
        return self.marks / 100 * 1000

    def get_attendance(self):
        return self.attendance / 100 * 1000
