# Generated by Django 2.2 on 2020-06-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0013_auto_20200612_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(blank=True, choices=[('0', 'Masculino'), ('1', 'Feminino')], default='0', max_length=1, null=True),
        ),
    ]
