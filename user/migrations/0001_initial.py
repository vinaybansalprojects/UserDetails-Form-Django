# Generated by Django 3.0.7 on 2021-02-23 20:38

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('birthday', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', phone_field.models.PhoneField(max_length=31)),
            ],
        ),
    ]