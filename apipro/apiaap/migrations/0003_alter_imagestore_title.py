# Generated by Django 3.2.4 on 2021-06-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiaap', '0002_alter_imagestore_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagestore',
            name='title',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]