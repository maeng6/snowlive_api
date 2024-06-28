# Generated by Django 5.0.6 on 2024-06-28 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResortInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resortNum', models.IntegerField(default=1)),
                ('fullName', models.CharField(max_length=100)),
                ('nickName', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('resortHomeUrl', models.CharField(max_length=255)),
                ('webcamUrl', models.CharField(max_length=255)),
                ('slopeUrl', models.CharField(max_length=255)),
                ('naverUrl', models.CharField(max_length=255)),
                ('busUrl', models.CharField(max_length=255)),
            ],
        ),
    ]
