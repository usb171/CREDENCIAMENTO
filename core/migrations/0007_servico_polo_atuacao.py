# Generated by Django 2.2 on 2020-06-13 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200613_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='polo_atuacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.PoloAtuacao', verbose_name='Polo de atuação'),
        ),
    ]
