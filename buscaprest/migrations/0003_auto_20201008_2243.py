# Generated by Django 3.1.2 on 2020-10-09 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buscaprest', '0002_auto_20201008_2228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestador',
            old_name='Bairro',
            new_name='bairro',
        ),
        migrations.RenameField(
            model_name='prestador',
            old_name='Categoria',
            new_name='categoria',
        ),
        migrations.RenameField(
            model_name='prestador',
            old_name='Cidade',
            new_name='cidade',
        ),
        migrations.RenameField(
            model_name='prestador',
            old_name='Prestador',
            new_name='prestador',
        ),
        migrations.RenameField(
            model_name='prestador',
            old_name='Telefone2',
            new_name='telefone2',
        ),
    ]