# Generated by Django 2.2 on 2020-06-12 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0012_auto_20200610_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='requisito',
            name='documento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edital.Documento', verbose_name='Documento'),
        ),
    ]
