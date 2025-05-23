# Generated by Django 5.2 on 2025-04-13 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Custo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=100)),
                ('custoCeluloseVirgem', models.DecimalField(decimal_places=4, max_digits=10)),
                ('custoGel', models.DecimalField(decimal_places=4, max_digits=10)),
                ('custoTnt750', models.DecimalField(decimal_places=4, max_digits=10)),
                ('custoTnt780', models.DecimalField(decimal_places=4, max_digits=10)),
                ('custoFitaAdesiva', models.DecimalField(decimal_places=4, max_digits=10)),
                ('custoElastico', models.DecimalField(decimal_places=4, max_digits=10)),
                ('custoBarreira', models.DecimalField(decimal_places=4, max_digits=10)),
                ('custoPolietileno780', models.DecimalField(decimal_places=4, max_digits=10)),
                ('custoHotMelt', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
    ]
