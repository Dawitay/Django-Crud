# Generated by Django 5.0.7 on 2024-08-16 15:52

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
                ('name', models.CharField(max_length=25, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=25, null=True)),
            ],
        ),
    ]
