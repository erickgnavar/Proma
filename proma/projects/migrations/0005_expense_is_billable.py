# Generated by Django 2.0.1 on 2018-02-25 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20180126_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='is_billable',
            field=models.BooleanField(default=False, verbose_name='Is billable?'),
        ),
    ]
