# Generated by Django 2.0.1 on 2018-01-22 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End date'),
        ),
    ]
