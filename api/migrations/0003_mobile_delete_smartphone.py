# Generated by Django 5.0.2 on 2024-03-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_smartphones_smartphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(max_length=255)),
                ('img_url', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('ram', models.IntegerField()),
                ('memory', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Smartphone',
        ),
    ]
