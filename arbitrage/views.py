from django.views.generic import ListView, CreateView, View
from .models import Arbitragem, ArbitragemCard
from django.urls import reverse_lazy #usado para redirecionamento pós criação
from django.shortcuts import get_object_or_404, redirect

class ArbitragemListView(ListView):
    model = Arbitragem #Procura o nome da APP e o nome do modelo

class ArbitragemCreateView(CreateView):
    model = Arbitragem
    fields = ['price_a', 'cripto_a', 'price_b', 'cripto_b', 'data', 'processo'] #fields: Quais campos quero que apareçam no formulário
    success_url = reverse_lazy("arbitragem_list")  # Redireciona para a página inicial após criar a leitura

class ArbitragemCompleteView(View):
    def get(self, request, pk):    
        arbitragem = get_object_or_404(Arbitragem, pk=pk)
        return redirect('arbitragem_list')

class ArbitragemCardListView(ListView):
    model = ArbitragemCard  #Procura o nome da APP e o nome do modelo