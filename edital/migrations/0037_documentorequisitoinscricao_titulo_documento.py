# Generated by Django 2.2 on 2020-06-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0036_auto_20200615_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentorequisitoinscricao',
            name='titulo_documento',
            field=models.CharField(max_length=250, null=True, verbose_name='Título do Documento'),
        ),
    ]
