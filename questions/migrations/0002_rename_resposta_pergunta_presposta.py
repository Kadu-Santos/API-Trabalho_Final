# Generated by Django 4.1.7 on 2023-04-12 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pergunta',
            old_name='resposta',
            new_name='Presposta',
        ),
    ]
