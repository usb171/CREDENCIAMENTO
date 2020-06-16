# Generated by Django 2.2 on 2020-06-15 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200613_1835'),
        ('edital', '0023_inscricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscricao',
            name='servicos',
            field=models.ManyToManyField(to='core.Servico'),
        ),
        migrations.CreateModel(
            name='DocumentoRequisitoInscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('0', 'Em Análise'), ('1', 'Inabilitada'), ('2', 'Habilitada'), ('3', 'Expirada'), ('4', 'Descredenciada')], default='0', max_length=100, verbose_name='Status do Documento')),
                ('observacao', models.TextField(verbose_name='Observações')),
                ('edital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edital.Edital')),
            ],
        ),
    ]