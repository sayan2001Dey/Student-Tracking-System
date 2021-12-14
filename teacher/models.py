from django.db import models
from django.contrib.auth.models import User
import uuid





class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_teacher = models.CharField(max_length=255, blank=True)
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
    date_join = models.DateField(auto_now_add=True, null=True)
    img_profile = models.ImageField(upload_to="profile_img/", blank=True)

    def __str__(self):
        return self.user.username

    def get_all_student(self):
        return self.student_set.all() or None

    def get_url_image(self):
        return self.img_profile.url if self.img_profile else 'https://dummyimage.com/300.png/09f/fff'

    def get_name(self):
        return self.user.first_name if self.user.first_name else self.user.username

    def save(self, *args, **kwargs):
        if not self.id:
            self.id_teacher = str(uuid.uuid4())[:6]
        return super().save( *args, **kwargs)

    def get_display_skills(self):
        if self.user.skills_set.all().count() > 0:
            skills = ", ".join([x.skill for x in self.user.skills_set.all()])
        else:
            skills = "-"
        return skills