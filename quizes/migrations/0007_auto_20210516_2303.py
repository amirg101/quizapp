# Generated by Django 3.1.2 on 2021-05-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0006_alter_quiz_image_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='image_logo',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
