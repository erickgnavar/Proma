# Generated by Django 2.0.1 on 2018-01-21 19:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('status', models.CharField(choices=[('ACTIVE', 'Active'), ('ARCHIVED', 'Archived')], default='ACTIVE', max_length=20, verbose_name='Status')),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Start date')),
                ('payment_type', models.CharField(choices=[('FLAT RATE', 'Flat Rate'), ('HOURLY RATE', 'Hourly Rate'), ('DAILY RATE', 'Daily Rate'), ('WEEKLY RATE', 'Weekly Rate'), ('MOUNTHLY RATE', 'Mounthly Rate')], default='FLAT RATE', max_length=20, verbose_name='Payment type')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Rate')),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('PEN', 'PEN')], default='USD', max_length=5, verbose_name='Currency')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='clients.Client')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ('name',),
                'default_related_name': 'projects',
            },
        ),
    ]
