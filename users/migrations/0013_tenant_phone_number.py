# Generated by Django 4.2.3 on 2023-08-03 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_delete_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='phone_number',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
