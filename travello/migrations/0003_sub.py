# Generated by Django 4.2.1 on 2023-07-15 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_destination_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
