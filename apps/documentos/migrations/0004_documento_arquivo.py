# Generated by Django 3.2.3 on 2021-05-22 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_alter_documento_pertence'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='arquivo',
            field=models.FileField(default='', upload_to='documentos'),
            preserve_default=False,
        ),
    ]
