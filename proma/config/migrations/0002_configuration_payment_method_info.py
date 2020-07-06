# Generated by Django 2.0.9 on 2020-01-03 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='payment_method_info',
            field=models.TextField(blank=True, help_text='This information will be sent within invoice email', null=True, verbose_name='Payment method info'),
        ),
    ]