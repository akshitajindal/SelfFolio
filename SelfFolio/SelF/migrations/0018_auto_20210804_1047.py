# Generated by Django 2.2.8 on 2021-08-04 05:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SelF', '0017_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='credits',
            field=models.FloatField(null=True),
        ),
        migrations.CreateModel(
            name='Reminders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, null=True)),
                ('code', models.CharField(max_length=32, null=True)),
                ('task', models.TextField(null=True)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('userProfile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]