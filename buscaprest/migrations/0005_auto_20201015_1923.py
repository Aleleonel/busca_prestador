# Generated by Django 3.1.2 on 2020-10-15 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscaprest', '0004_auto_20201008_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestador',
            name='categoria',
            field=models.CharField(blank=True, choices=[('MOTO', 'Moto'), ('MECANICA', 'Mecanica'), ('FUNILARIA', 'Funilaria'), ('VIDRO', 'Vidro')], max_length=60, null=True),
        ),
    ]
