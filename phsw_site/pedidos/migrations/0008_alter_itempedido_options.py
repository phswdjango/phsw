# Generated by Django 3.2.6 on 2021-08-26 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_alter_item_imagem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itempedido',
            options={'verbose_name': 'Item do pedido', 'verbose_name_plural': 'Itens do pedido'},
        ),
    ]
