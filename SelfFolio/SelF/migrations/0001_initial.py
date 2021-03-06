# Generated by Django 2.2.8 on 2021-05-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Bio', models.TextField(blank=True)),
                ('University', models.CharField(max_length=50)),
                ('Profession', models.CharField(choices=[('Student', 'Student'), ('Professional', 'Professional')], default='Student', max_length=32)),
                ('DOB', models.DateField()),
                ('UserEmail', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=32)),
            ],
        ),
    ]
