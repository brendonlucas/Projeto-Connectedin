# Generated by Django 2.2.2 on 2019-06-26 23:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0002_auto_20190626_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=20)),
                ('nome_empresa', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contatos', models.ManyToManyField(to='profile.Perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Convite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('convidado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_recebidos', to='profile.Perfil')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='convites_feitos', to='profile.Perfil')),
            ],
        ),
    ]