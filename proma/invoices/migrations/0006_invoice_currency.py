# Generated by Django 2.0.9 on 2019-06-01 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0005_invoice_payment_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR'), ('PEN', 'PEN')], default='USD', max_length=5, verbose_name='Currency'),
        ),
    ]
