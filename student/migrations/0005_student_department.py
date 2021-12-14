# Generated by Django 3.2.7 on 2021-10-04 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_student_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='department',
            field=models.CharField(blank=True, choices=[('mechanical', 'Mechanical'), ('civil', 'Civil'), ('electrical', 'Electrical'), ('electronics', 'Electronics'), ('computer', 'Computer'), ('pharmacy', 'Pharmacy')], max_length=50, null=True),
        ),
    ]
