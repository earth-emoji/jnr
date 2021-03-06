# Generated by Django 2.2.3 on 2019-07-16 23:58

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'verbose_name': 'job', 'verbose_name_plural': 'jobs'},
        ),
        migrations.AlterField(
            model_name='job',
            name='description',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='positions_to_fill',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
