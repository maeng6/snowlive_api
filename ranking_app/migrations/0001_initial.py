# Generated by Django 5.0.6 on 2024-07-01 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('resort_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slope_pass_temp',
            fields=[
                ('slope_pass_id', models.AutoField(primary_key=True, serialize=False)),
                ('pass_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ranking_record',
            fields=[
                ('ranking_id', models.AutoField(primary_key=True, serialize=False)),
                ('pass_time', models.DateTimeField()),
                ('slope_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resort_app.slope_info')),
            ],
        ),
    ]
