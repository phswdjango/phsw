# Generated by Django 3.2.6 on 2021-08-05 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210805_1038'),
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='fk_tabelaPreco',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pedidos.tabelapreco'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='fk_tipoEmpresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.tipoempresa'),
        ),
        migrations.AddField(
            model_name='user',
            name='fk_empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='base.empresa'),
        ),
    ]
