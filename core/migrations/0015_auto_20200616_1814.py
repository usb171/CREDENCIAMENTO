# Generated by Django 2.2 on 2020-06-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200613_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='codigo',
            field=models.CharField(max_length=250, null=True, unique=True, verbose_name='Código do Documento'),
        ),
        migrations.AlterField(
            model_name='requisito',
            name='titulo',
            field=models.CharField(max_length=250, null=True, unique=True, verbose_name='Título do Documento'),
        ),
    ]
