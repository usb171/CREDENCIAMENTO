# Generated by Django 2.2 on 2020-05-30 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0004_auto_20200529_1850'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(default=True)),
                ('ordem', models.IntegerField(default=1, null=True)),
                ('documento', models.FileField(null=True, upload_to='uploads/%Y/%m/%d', verbose_name='Documento')),
                ('edital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edital.Edital', verbose_name='Edital')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
    ]