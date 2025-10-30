import sqlite3
import json
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, View
from .models import Moedas
from django.urls import reverse_lazy, reverse #usado para redirecionamento pós criação
from django.shortcuts import get_object_or_404, redirect, render
# from django.utils import timezone
# from django.http import JsonResponse
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

class MoedasListView(ListView):
    model = Moedas #Procura o nome da APP e o nome do modelo

class MoedasImportListView(ListView):
    model = Moedas #Procura o nome da APP e o nome do modelo
    
    def getcoins(request):
        print("--------------------------------------------------")
        if request.method == 'POST':
            try:
                print ('passou4')
                coin_list = cg.get_coins_list(include_platform=True)

                ## Imprime as primeiras 20000 moedas para exemplo
                #print("Primeiras 20000 moedas disponíveis na CoinGecko API:")
                print("--------------------------------------------------")
                for coin in coin_list[:20000]:
                    print(f"ID: {coin['id']}, Símbolo: {coin['symbol']}, Nome: {coin['name']}, Plataformas: {coin['platforms']}")
                    #insere_moeda({coin['symbol']}, {coin['name']}, {coin['platforms']}, None, datetime.now())                
                
                ## Para ver o número total de moedas, você pode usar a função len()
                print(f"\nTotal de moedas disponíveis: {len(coin_list)}")

                if(coin_list):
                    print ('passou5')
                    return redirect('moedas_list')
                    return redirect(reverse('/moedas_importar.html'))
                    #return coin_list        

            except Exception as e:
                print ('passou6')
                print(f"Ocorreu um erro ao conectar-se à CoinGecko API: {e}")
                return None
            
            print ('passou7')
            return redirect('moedas_list', {'coin_list': coin_list})
            return render(request, '/moedas_importar.html', {'coin_list': coin_list})
            
        # Se a requisição não for POST, redirecione ou faça outra coisa
        print ('passou8')
        return HttpResponse("Método não permitido!!!!!!!!!!", status=405)

    #Função para inserir os dados no banco de dados SQLite
    def insere_moeda(symbol, name, platforms, currency, data):
        print ('passou9')
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        query = "INSERT INTO coins_moedas ( symbol, name, platforms, currency, data) " \
                f"VALUES (symbol = {symbol} ,name = {name} ,platforms = {platforms} ,currency = {currency} ,data = {data});"
        #cursor.execute("INSERT INTO leitor_pdf_leitor (data, num_cartao, estabelecimento, valor) VALUES (?, ?, ?, ?)", (data, numero, estabelecimento, valor))
        cursor.execute(query)
        conn.commit()
        conn.close()
    #
    #

# class MoedasCreateView(CreateView):
#     model = Moedas
#     fields = ['symbol', 'name', 'platforms', 'currency', 'data'] #fields: Quais campos quero que apareçam no formulário
#     success_url = reverse_lazy("moeda_list")  # Redireciona para a página inicial após criar a leitura

# class MoedasCompleteView(View):
#     def get(self, request, pk):    
#         moeda = get_object_or_404(Moedas, pk=pk)        
#         return redirect('moedas_list')

# def tamanho_da_str(request):
#     print('post?')
#     if request.method == 'POST':    
#         print ('passou3')         
#         palavra_digitada = request.POST.get('palavra')
#         print (palavra_digitada)
#         len_string = len(palavra_digitada)
#         dicionario = {'tamanho': len_string}
#         return redirect('moedas_list')
#         return render(request, "/moedas_importar.html", dicionario)





# #exemplo1
# def meu_formulario(request):
#     print('post?')
#     if request.method == 'POST':
#         # Acessa dados do formulário
#         nome = request.POST.get('nome')
#         email = request.POST.get('email')
#         # Faça algo com os dados, como salvar em um banco de dados
#         return HttpResponse(f"Nome: {nome}, Email: {email}")
    
#     # Se o método for GET, renderiza o formulário HTML
#     return render(request, 'moedas_list.html') 


# #exemplo2
# def minha_view_json(request):
#     print('post?')
#     if request.method == 'POST':
#         try:
#             # Analisa os dados JSON recebidos no corpo da requisição
#             dados_json = json.loads(request.body)
#             nome = dados_json.get('nome')
#             idade = dados_json.get('idade')
            
#             # Faça algo com os dados
#             resposta = {
#                 'status': 'sucesso',
#                 'mensagem': f'Dados recebidos: Nome {nome}, Idade {idade}'
#             }
#             return JsonResponse(resposta)
#         except json.JSONDecodeError:
#             return JsonResponse({'status': 'erro', 'mensagem': 'JSON inválido'}, status=400)
    
#     return JsonResponse({'status': 'erro', 'mensagem': 'Método não permitido'}, status=405)





# class UserItemListView(ListView):
#     model = Moedas
    
#     def get_queryset(self):
#         # Filtra os itens para mostrar apenas os do usuário logado
#         return Moedas.objects.filter(usuario=self.request.user)

# class CustomListView(ListView):
#     model = Moedas
    
#     def get_context_data(self, **kwargs):
#         # Chama a implementação base para obter o contexto original
#         context = super().get_context_data(**kwargs)
        
#         # Adiciona dados extras ao contexto
#         context['now'] = timezone.now()
#         context['outra_variavel'] = 'Dados adicionais para o template'
        
#         return context
    
#     def outra_view(self):
#         from django.shortcuts import redirect
# from django.urls import reverse

# def outra_view_exemplo(request):
#     # Lógica da view
#     # ...
#     # Redireciona para a sua ListView personalizada
#     return redirect(reverse('moedas_list'))