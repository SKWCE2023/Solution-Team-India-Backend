# Generated by Django 4.2.7 on 2023-11-21 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_customers_dob_timestamp_customers_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='insurance_bik',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='insurance_inn',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='insurance_policy',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
