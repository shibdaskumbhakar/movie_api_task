# Generated by Django 2.2 on 2021-01-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('title', models.CharField(max_length=100)),
                ('released_year', models.CharField(max_length=500)),
                ('rating', models.IntegerField()),
                ('genres', models.CharField(max_length=500)),
            ],
        ),
    ]