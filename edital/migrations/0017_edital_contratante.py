# Generated by Django 2.2 on 2020-06-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('edital', '0016_auto_20200613_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='edital',
            name='contratante',
            field=models.ManyToManyField(related_query_name='+', to='core.Contratante'),
        ),
    ]