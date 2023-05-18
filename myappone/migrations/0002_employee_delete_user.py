# Generated by Django 4.2 on 2023-04-23 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myappone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=100)),
                ('job_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
