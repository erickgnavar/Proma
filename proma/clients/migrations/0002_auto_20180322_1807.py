# Generated by Django 2.0.1 on 2018-03-22 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='client',
            name='alias',
            field=models.CharField(default='', max_length=30, verbose_name='Alias'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='client',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='client',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone'),
        ),
        migrations.AddField(
            model_name='client',
            name='state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='client',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Zipcode'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(help_text='This name will be used for invoicing', max_length=100, verbose_name='Legal name'),
        ),
    ]
