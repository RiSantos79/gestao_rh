# Generated by Django 3.2.3 on 2021-06-03 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registo_hora_extra', '0004_alter_registohoraextra_horas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registohoraextra',
            name='motivo',
            field=models.CharField(max_length=100),
        ),
    ]
