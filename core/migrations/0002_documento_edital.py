# Generated by Django 2.2 on 2020-06-22 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('edital', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='edital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edital.Edital', verbose_name='Edital'),
        ),
    ]