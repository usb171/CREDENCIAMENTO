# Generated by Django 2.2 on 2020-06-12 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0013_requisito_documento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisito',
            name='documento',
        ),
    ]
