# Generated by Django 3.2.3 on 2021-05-23 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registo_hora_extra', '0002_registohoraextra_funcionario'),
    ]

    operations = [
        migrations.AddField(
            model_name='registohoraextra',
            name='horas',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=3),
            preserve_default=False,
        ),
    ]
