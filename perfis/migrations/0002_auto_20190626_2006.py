# Generated by Django 2.2.2 on 2019-06-26 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='contatos',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Convite',
        ),
        migrations.DeleteModel(
            name='Perfil',
        ),
    ]
