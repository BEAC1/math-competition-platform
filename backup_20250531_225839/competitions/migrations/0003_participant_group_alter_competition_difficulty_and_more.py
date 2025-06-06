# Generated by Django 5.2.1 on 2025-05-14 20:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0002_participant_alter_competition_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='group',
            field=models.IntegerField(choices=[(1, 'الفوج الأول'), (2, 'الفوج الثاني')], default=1, verbose_name='الفوج'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'المستوى الأول'), (2, 'المستوى الثاني'), (3, 'المستوى الثالث'), (4, 'المستوى الرابع')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
        migrations.AlterField(
            model_name='mathquestion',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'المستوى الأول'), (2, 'المستوى الثاني'), (3, 'المستوى الثالث'), (4, 'المستوى الرابع')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)]),
        ),
    ]
