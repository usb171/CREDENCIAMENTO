# Generated by Django 2.2 on 2020-06-19 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0043_auto_20200618_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentorequisitoinscricao',
            name='inscricao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='edital.Inscricao'),
        ),
    ]
