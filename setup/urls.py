from django.contrib import admin
from django.urls import path

from arbitrage.views import ArbitragemListView, ArbitragemCreateView, ArbitragemCardListView
from coins.views import MoedasListView, MoedasImportListView
from coins.views import iniciar_tarefa_e_progresso

urlpatterns = [
    path("admin/", admin.site.urls),

    path("",                ArbitragemListView.as_view(), name="arbitragem_list"),
    path("arbitragem/novo", ArbitragemCreateView.as_view(), name="arbitragem_form"),
    path("arbitragem/card", ArbitragemCardListView.as_view(), name="arbitragemcard_list"),
        
    path('moedas/',         MoedasListView.as_view(), name='moedas_list'),
    path('moedas/importar', MoedasImportListView.as_view(), name='moedas_importar'),
    
    path('iniciar-tarefa/', iniciar_tarefa_e_progresso, name='iniciar_tarefa'),
    
]