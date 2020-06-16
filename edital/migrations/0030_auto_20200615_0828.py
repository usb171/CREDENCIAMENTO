# Generated by Django 2.2 on 2020-06-15 08:28

from django.db import migrations, models
import private_storage.fields
import private_storage.storage.files


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0029_auto_20200615_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentorequisitoinscricao',
            name='documento',
            field=private_storage.fields.PrivateFileField(null=True, storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='', verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='documentorequisitoinscricao',
            name='status',
            field=models.CharField(choices=[('0', 'Em Análise'), ('1', 'Documento OK'), ('2', 'Documento Vencido'), ('3', 'Documento Ilegível'), ('4', 'Documento Inválido')], default='0', max_length=100, verbose_name='Status do Documento'),
        ),
    ]