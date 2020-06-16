# Generated by Django 2.2 on 2020-06-15 08:53

from django.db import migrations
import private_storage.fields
import private_storage.storage.files


class Migration(migrations.Migration):

    dependencies = [
        ('edital', '0031_auto_20200615_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentorequisitoinscricao',
            name='documento',
            field=private_storage.fields.PrivateFileField(null=True, storage=private_storage.storage.files.PrivateFileSystemStorage(), upload_to='', verbose_name='Documento'),
        ),
    ]