# Generated by Django 3.1.2 on 2021-05-17 14:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0011_auto_20210517_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='image_logo',
            field=models.FileField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
