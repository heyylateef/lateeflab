# Generated by Django 3.2.5 on 2022-04-19 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_alter_blogpost_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
