# Generated by Django 2.0.1 on 2018-01-21 20:42

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Amount')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('notes', models.TextField(blank=True, null=True, verbose_name='Notes')),
                ('attachment', models.FileField(blank=True, null=True, upload_to='projects/expense/%Y/%m/%d/', verbose_name='Attachment')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='projects.Project')),
            ],
            options={
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
                'ordering': ('name',),
                'default_related_name': 'expenses',
            },
        ),
    ]
