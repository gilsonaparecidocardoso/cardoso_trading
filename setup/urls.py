from django.contrib import admin
from django.urls import path, include

from arbitrage.views import ArbitragemListView, ArbitragemCreateView, ArbitragemCardListView, ProdutoListView
from coins.views import MoedasListView, MoedasImportView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", ArbitragemListView.as_view(), name="arbitragem_list"),
    path("arbitragem/novo", ArbitragemCreateView.as_view(), name="arbitragem_form"),
    path("arbitragem/card", ArbitragemCardListView.as_view(), name="arbitragemcard_list"),
        
    path('moedas/', MoedasListView.as_view(), name='moedas_list'),
    path('moedas/importar/', MoedasImportView.as_view(), name='moedas_list'),

    path('customizado/', MoedasListView.as_view(), name='getcoins'),
]