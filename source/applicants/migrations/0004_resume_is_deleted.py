# Generated by Django 4.1.7 on 2023-04-18 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0003_alter_resume_facebook_alter_resume_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удалено'),
        ),
    ]
