# Generated by Django 2.2.8 on 2021-06-30 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SelF', '0014_auto_20210630_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile.png', null=True, upload_to=''),
        ),
    ]