# Generated by Django 2.2 on 2020-06-16 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20200616_1823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='titulo',
            field=models.CharField(max_length=240, null=True, verbose_name='Título'),
        ),
    ]