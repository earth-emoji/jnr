# Generated by Django 2.2.3 on 2019-07-16 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_professional',
            field=models.BooleanField(default=False, verbose_name='professional status'),
        ),
    ]
