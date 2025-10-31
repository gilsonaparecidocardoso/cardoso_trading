from django.contrib import admin
from django.urls import path

from arbitrage.views import ArbitragemListView, ArbitragemCreateView, ArbitragemCardListView
from coins.views import MoedasListView, MoedasImportListView, MoedasImportarListView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", ArbitragemListView.as_view(), name="arbitragem_list"),
    path("arbitragem/novo", ArbitragemCreateView.as_view(), name="arbitragem_form"),
    path("arbitragem/card", ArbitragemCardListView.as_view(), name="arbitragemcard_list"),
        
    path('moedas/', MoedasListView.as_view(), name='moedas_list'),
    path('moedas/importar', MoedasImportListView.as_view(), name='moedas_importar'),
    path('moedas/importar/importar/', MoedasImportarListView.as_view(), name='fn_moedas_importar'),

]