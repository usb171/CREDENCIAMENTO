# Generated by Django 2.2 on 2020-06-18 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0040_auto_20200616_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentorequisitoinscricao',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
        migrations.AddField(
            model_name='documentorequisitoinscricao',
            name='update_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Atualizado em'),
        ),
    ]