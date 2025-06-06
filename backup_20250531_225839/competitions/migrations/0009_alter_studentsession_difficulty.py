# Generated by Django 5.2.1 on 2025-05-29 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0008_studentsession_studentresponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsession',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'المستوى الأول - المرحلة الأولى'), (2, 'المستوى الثاني - المرحلة الأولى'), (3, 'المستوى الثالث - المرحلة الأولى'), (4, 'المستوى الرابع - المرحلة الأولى'), (5, 'المستوى الخامس - المرحلة الأولى'), (6, 'المستوى السادس - المرحلة الأولى'), (7, 'المستوى الأول - المرحلة الثانية'), (8, 'المستوى الثاني - المرحلة الثانية'), (9, 'المستوى الثالث - المرحلة الثانية')], verbose_name='مستوى الصعوبة'),
        ),
    ]
