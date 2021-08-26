from django.contrib import admin
from phsw_site.pedidos.models import Item, TabelaPreco, ItemPreco, Pedido, ItemPedido, StatusPedido, CategoriaItem


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id_item', 'fk_categoria', 'verbose_name', 'descricao', 'unidade', 'codigo_barras', 'ativado')
    # list_filter = ('CategoriaItem.verbose_name', 'status')
    list_filter = ('fk_categoria', 'ativado')
    # prepopulated_fields = {'slug': ('title',)}
    search_fields = ('verbose_name', 'ativado')
    ordering = ('fk_categoria', 'verbose_name')
    list_editable = ('ativado', 'verbose_name')  # editavel ao acessar a pagina ItemAdmin
    list_display_links = ('id_item', 'unidade')  # link para acessar o registro.


@admin.register(ItemPreco)
class ItemPrecoAdmin(admin.ModelAdmin):
    list_display = ('fk_tabelaPreco', 'fk_item', 'preco_unit', 'data')


@admin.register(TabelaPreco)
class TabelaPrecoAdmin(admin.ModelAdmin):
    list_display = ('verbose_name', 'id_tabela')
    ordering = ('verbose_name',)


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'fk_empresa', 'fk_usuario', 'fk_status', 'data_pedido', 'data_faturamento', 'valor_total')
    list_filter = ('fk_empresa', 'fk_usuario', 'data_pedido', 'fk_status')
    ordering = ('data_pedido',)
    inlines = [
        ItemPedidoInline
    ]


@admin.register(CategoriaItem)
class CategoriaItemAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'descricao', 'verbose_name')


@admin.register(StatusPedido)
class StatusPedidoAdmin(admin.ModelAdmin):
    list_display = ('verbose_name', 'descricao')
