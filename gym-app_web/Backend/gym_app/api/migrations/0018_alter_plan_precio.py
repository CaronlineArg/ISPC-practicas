# Generated by Django 4.2.1 on 2024-05-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0017_mensaje_alter_reserva_clase_alter_reserva_cliente"),
    ]

    operations = [
        migrations.AlterField(
            model_name="plan",
            name="precio",
            field=models.PositiveIntegerField(),
        ),
    ]