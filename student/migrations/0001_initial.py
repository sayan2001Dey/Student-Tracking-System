# Generated by Django 3.2.7 on 2021-10-03 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True)),
                ('semester', models.IntegerField(blank=True)),
                ('reg_no', models.BigIntegerField(blank=True)),
                ('roll_no', models.BigIntegerField(blank=True)),
                ('education', models.CharField(blank=True, max_length=255)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('skills', models.TextField(blank=True)),
                ('projects', models.TextField(blank=True)),
                ('exp', models.TextField(blank=True)),
                ('img_profile', models.ImageField(blank=True, upload_to='profile_img/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
