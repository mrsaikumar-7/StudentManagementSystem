# Generated by Django 4.1.5 on 2023-02-17 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_library'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='image',
            field=models.ImageField(upload_to='library/'),
        ),
    ]
