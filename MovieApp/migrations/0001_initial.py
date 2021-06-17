# Generated by Django 3.2.4 on 2021-06-17 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genres', models.CharField(max_length=50)),
                ('overview', models.TextField()),
                ('popularity', models.FloatField(default=0)),
                ('adult', models.BooleanField(default=False)),
                ('production', models.CharField(max_length=60)),
                ('runtime', models.IntegerField(default=0)),
                ('release', models.CharField(max_length=20)),
                ('budget', models.IntegerField(default=0)),
                ('voteAver', models.FloatField(default=0)),
                ('voteCount', models.IntegerField(default=0)),
                ('tagLine', models.TextField()),
                ('status', models.CharField(max_length=20)),
                ('video', models.TextField()),
                ('poster', models.TextField()),
                ('backdrop', models.TextField()),
                ('cast', models.TextField()),
                ('director', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieApp.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieApp.user')),
            ],
        ),
    ]
