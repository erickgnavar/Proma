# Generated by Django 2.0.1 on 2018-03-08 09:18

from django.db import migrations, models
import secrets


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_populate_invoice_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='token',
            field=models.CharField(default=secrets.token_hex, editable=False, max_length=64, unique=True),
        ),
    ]
