# Generated by Django 3.1.6 on 2021-06-20 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('est_app', '0003_auto_20210620_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='picture1',
            field=models.ImageField(blank=True, null=True, upload_to='prop_pix/'),
        ),
    ]