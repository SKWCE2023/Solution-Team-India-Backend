# Generated by Django 4.2.7 on 2023-11-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_customers_social_sec_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='insurance_bik',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='customers',
            name='insurance_policy',
            field=models.CharField(max_length=50, null=True),
        ),
    ]