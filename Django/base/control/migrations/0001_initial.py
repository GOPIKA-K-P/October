# Generated by Django 4.1 on 2023-10-10 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dept', models.CharField(max_length=10)),
                ('college', models.CharField(max_length=3)),
            ],
        ),
    ]
