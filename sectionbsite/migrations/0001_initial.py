# Generated by Django 5.0.6 on 2024-05-17 13:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('gender_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=55)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'genders',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=55)),
                ('middle_name', models.CharField(blank=True, max_length=55)),
                ('last_name', models.CharField(max_length=55)),
                ('age', models.IntegerField()),
                ('birth_date', models.DateField()),
                ('username', models.CharField(max_length=55)),
                ('password', models.CharField(max_length=255)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sectionbsite.gender')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
