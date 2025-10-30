from django.contrib import admin
from django.urls import path

from arbitrage.views import ArbitragemListView, ArbitragemCreateView, ArbitragemCardListView
from coins.views import MoedasListView, MoedasImportListView
from produto.views import ProdutoCreateView, ProdutoListView, ProdutoUpdateView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", ArbitragemListView.as_view(), name="arbitragem_list"),
    path("arbitragem/novo", ArbitragemCreateView.as_view(), name="arbitragem_form"),
    path("arbitragem/card", ArbitragemCardListView.as_view(), name="arbitragemcard_list"),
        
    path('moedas/', MoedasListView.as_view(), name='moedas_list'),
    path('moedas/importar/', MoedasImportListView.as_view(), name='getcoins'),

    path('customizado/', MoedasListView.as_view(), name='getcoins'),

    path('produto/', ProdutoListView.as_view(), name='produto_list'),
    path('produto/novo', ProdutoCreateView.as_view(), name='produto_form'),
    #path('produtos/detalhe/<int:pk>/', ProdutoDetailView.as_view(), name='detalhe_produto'),
    #path('produtos/detalhe/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='editar_produto'),
    
]