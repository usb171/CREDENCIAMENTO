# Generated by Django 2.2 on 2020-06-16 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0036_auto_20200616_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(blank=True, choices=[('1', 'Feminino'), ('0', 'Masculino')], default='0', max_length=1, null=True),
        ),
    ]
