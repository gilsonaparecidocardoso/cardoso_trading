from django.views.generic import ListView, CreateView, View
from .models import Arbitragem, ArbitragemCard, Produto
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



class ProdutoListView(ListView):
    model = ArbitragemCard #ABRINDO OUTRO FORM SEM CRIAR BANCO???

# class ProdutoCreateView(CreateView):
#     model = Produto
#     fields = ['nome', 'preco'] #fields: Quais campos quero que apareçam no formulário
#     success_url = reverse_lazy("produto_list")  # Redireciona para a página inicial após criar a leitura

# class ProdutoCompleteView(View):
#     def get(self, request, pk):    
#         produto = get_object_or_404(Produto, pk=pk)
#         return redirect('produto_list')



class ArbitragemCardListView(ListView):
    model = ArbitragemCard  #Procura o nome da APP e o nome do modelo

# class ArbitragemCardCreateView(CreateView):
#     model = ArbitragemCard
#     fields = ['price_a', 'cripto_a', 'price_b', 'cripto_b', 'data', 'processo'] #fields: Quais campos quero que apareçam no formulário
#     success_url = reverse_lazy("arbitragemcard_list")  # Redireciona para a página inicial após criar a leitura

# class ArbitragemCardCompleteView(View):
#     def get(self, request, pk):    
#         arbitragemcard = get_object_or_404(ArbitragemCard, pk=pk)
#         return redirect('arbitragemcard_list')