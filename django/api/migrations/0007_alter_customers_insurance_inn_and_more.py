# Generated by Django 4.2.7 on 2023-11-21 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_customers_insurance_bik_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='insurance_inn',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='insurance_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]