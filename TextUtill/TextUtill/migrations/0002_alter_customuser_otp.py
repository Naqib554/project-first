# Generated by Django 4.2.5 on 2023-10-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextUtill', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
