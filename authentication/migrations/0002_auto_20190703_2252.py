# Generated by Django 2.2.2 on 2019-07-03 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_verified',
            field=models.DateField(blank=True, null=True),
        ),
    ]