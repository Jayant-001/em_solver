# Generated by Django 3.2.9 on 2021-11-30 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MathData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_list', models.CharField(max_length=100)),
                ('y_list', models.CharField(max_length=100)),
                ('x2_list', models.CharField(max_length=100)),
                ('xy_list', models.CharField(max_length=100)),
            ],
        ),
    ]
