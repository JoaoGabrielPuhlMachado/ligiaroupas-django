# Generated by Django 4.2.7 on 2023-12-06 17:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("usuario", "0002_usuario_tipo_usuario"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="tipo_usuario",
            field=models.IntegerField(choices=[(1, "Admin"), (2, "Cliente")], default=2, verbose_name="User Type"),
        ),
    ]
