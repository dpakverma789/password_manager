# Generated by Django 3.2.7 on 2022-02-05 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]