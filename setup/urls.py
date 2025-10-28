from django.contrib import admin
from django.urls import path

from arbitrage.views import ArbitragemListView, ArbitragemCreateView, ArbitragemCardListView, ProdutoListView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", ArbitragemListView.as_view(), name="arbitragem_list"),
    path("arbitragem/novo", ArbitragemCreateView.as_view(), name="arbitragem_form"),
    path("arbitragem/card", ArbitragemCardListView.as_view(), name="arbitragemcard_list"),
    
    path('produtos/', ProdutoListView.as_view(), name='produto_list'),
]