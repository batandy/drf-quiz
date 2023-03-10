# Generated by Django 4.1.7 on 2023-03-10 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_name', models.CharField(default='', max_length=20)),
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(default='', max_length=100, unique=True)),
                ('nickname', models.CharField(default='', max_length=100, unique=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_name', models.CharField(default='', max_length=20)),
                ('quiz_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizs', to='quiz.category')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('body', models.TextField()),
                ('answer', models.IntegerField()),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='quiz.quiz')),
            ],
        ),
    ]
