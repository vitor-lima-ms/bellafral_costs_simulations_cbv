# Generated by Django 5.2 on 2025-04-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fralda', '0004_alter_fralda_identificador_alter_fralda_modelo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fralda',
            name='modelo',
            field=models.CharField(choices=[('ABS BELLAFRAL CONFORT', 'ABS BELLAFRAL CONFORT'), ('ABS BELLAFRAL BASIC', 'ABS BELLAFRAL BASIC'), ('ABS BIG CONFORT', 'ABS BIG CONFORT'), ('FRALDA BELLAFRAL CONFORT', 'FRALDA BELLAFRAL CONFORT'), ('FRALDA BELLAFRAL BASIC', 'FRALDA BELLAFRAL BASIC'), ('FRALDA BIG CONFORT', 'FRALDA BIG CONFORT')], max_length=100, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='fralda',
            name='tamanho',
            field=models.CharField(choices=[('XG', 'XG'), ('G', 'G'), ('M', 'M')], max_length=100, verbose_name='Tamanho'),
        ),
    ]
