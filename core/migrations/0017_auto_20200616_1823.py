# Generated by Django 2.2 on 2020-06-16 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_requisito_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisito',
            name='codigo',
        ),
        migrations.AlterField(
            model_name='servico',
            name='codigo',
            field=models.CharField(max_length=250, verbose_name='Código'),
        ),
    ]
