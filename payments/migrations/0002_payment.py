# Generated by Django 4.2.3 on 2023-08-03 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('merchent_id', models.CharField(max_length=128, null=True)),
                ('checkout_id', models.CharField(max_length=128, null=True)),
                ('is_complete', models.BooleanField(default=False)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.bill')),
            ],
            options={
                'ordering': ['-updated_at'],
                'abstract': False,
            },
        ),
    ]
