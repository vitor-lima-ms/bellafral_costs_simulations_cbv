# Generated by Django 5.2 on 2025-04-13 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='custo',
            name='custoPolietileno750',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=10),
        ),
    ]
