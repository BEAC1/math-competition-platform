# Generated by Django 5.2.1 on 2025-05-12 04:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('student', 'تلميذ'), ('admin', 'مشرف')], default='student', max_length=10)),
                ('grade', models.CharField(blank=True, choices=[('1', 'الصف الأول'), ('2', 'الصف الثاني'), ('3', 'الصف الثالث'), ('4', 'الصف الرابع'), ('5', 'الصف الخامس'), ('6', 'الصف السادس')], max_length=2, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
