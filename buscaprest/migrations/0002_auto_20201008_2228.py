# Generated by Django 3.1.2 on 2020-10-09 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buscaprest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestador',
            old_name='bairro',
            new_name='Bairro',
        ),
        migrations.RenameField(
            model_name='prestador',
            old_name='categoria',
            new_name='Categoria',
        ),
        migrations.RenameField(
            model_name='prestador',
            old_name='cidade',
            new_name='Cidade',
        ),
        migrations.RenameField(
            model_name='prestador',
            old_name='endereco',
            new_name='Endereco',
        ),
        migrations.RenameField(
            model_name='prestador',
            old_name='prestador',
            new_name='Prestador',
        ),
        migrations.RenameField(
            model_name='prestador',
            old_name='telefone',
            new_name='Telefone2',
        ),
    ]
