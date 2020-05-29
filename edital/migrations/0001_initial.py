# Generated by Django 2.2 on 2020-05-28 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('rascunho', 'Rascunho'), ('publicado', 'Publicado'), ('cancelado', 'Cancelado'), ('encerrado', 'Encerrado')], default='rascunho', max_length=30)),
                ('titulo', models.CharField(max_length=250, null=True, verbose_name='Título')),
                ('categoria', models.CharField(choices=[('0', 'Pessoa Física'), ('1', 'Pessoa Jurídica'), ('2', 'Pessoa Física/Jurídica')], max_length=60, verbose_name='Categoria')),
                ('descricao', models.TextField(null=True, verbose_name='Descrição')),
                ('data_publicacao', models.DateTimeField(verbose_name='Data de Publicação')),
                ('inicio_inscricao', models.DateTimeField(verbose_name='Inicio das Inscrições')),
                ('fim_inscricao', models.DateTimeField(verbose_name='Fim das Inscrições')),
            ],
            options={
                'verbose_name': 'Edital',
                'verbose_name_plural': 'Editais',
                'ordering': ['-id'],
            },
        ),
    ]
