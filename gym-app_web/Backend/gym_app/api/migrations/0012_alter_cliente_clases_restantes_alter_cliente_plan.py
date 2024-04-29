# Generated by Django 4.2.1 on 2023-05-19 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_cliente_clases_restantes_alter_cliente_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='clases_restantes',
            field=models.PositiveBigIntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='plan',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.plan'),
        ),
    ]
