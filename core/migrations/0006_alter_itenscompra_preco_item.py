# Generated by Django 4.2.7 on 2023-12-07 23:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0005_remove_produto_tamanho_produto_tamanho"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itenscompra",
            name="preco_item",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]