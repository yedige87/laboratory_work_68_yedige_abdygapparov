# Generated by Django 4.1.7 on 2023-04-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicants', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resume',
            options={'verbose_name': 'Резюме', 'verbose_name_plural': 'Резюме'},
        ),
        migrations.AlterField(
            model_name='resume',
            name='salary',
            field=models.PositiveIntegerField(verbose_name='Желаемая зарплата'),
        ),
    ]
