# Generated by Django 4.1.7 on 2023-04-11 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('level', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puzzleEnunciado', models.CharField(max_length=250)),
                ('puzzleComand', models.CharField(max_length=250)),
                ('puzzleResposta', models.CharField(max_length=250)),
                ('puzzleNivel', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='level.level')),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=250)),
                ('alternativa_a', models.CharField(max_length=250)),
                ('alternativa_b', models.CharField(max_length=250)),
                ('alternativa_c', models.CharField(max_length=250)),
                ('alternativa_d', models.CharField(max_length=250)),
                ('resposta', models.CharField(max_length=250)),
                ('perguntaNivel', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='level.level')),
            ],
        ),
    ]
