# Generated by Django 2.2 on 2020-05-31 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0007_auto_20200531_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edital',
            name='ano_publicacao',
            field=models.CharField(max_length=5, null=True, verbose_name='Ano de Publicação'),
        ),
    ]