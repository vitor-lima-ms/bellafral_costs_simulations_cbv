# Generated by Django 5.2 on 2025-04-14 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulacao', '0004_alter_simulacao_custoobj_alter_simulacao_fraldaobj'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulacao',
            name='polietileno162CUT',
            field=models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='simulacao',
            name='tnt162CUT',
            field=models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=10),
        ),
    ]
