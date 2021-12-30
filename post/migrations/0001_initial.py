# Generated by Django 3.2.10 on 2021-12-30 07:47

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', tinymce.models.HTMLField()),
                ('image', models.ImageField(upload_to='uploads')),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]