# Generated by Django 2.2 on 2020-06-15 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0024_auto_20200615_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentorequisitoinscricao',
            name='inscricao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='edital.Inscricao'),
        ),
        migrations.AlterField(
            model_name='documentorequisitoinscricao',
            name='edital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Servico'),
        ),
    ]
