from datetime import datetime 
import sqlite3
import json
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from .models import Moedas
#from django.urls import reverse_lazy, reverse #usado para redirecionamento pós criação
from django.shortcuts import get_object_or_404, redirect, render
# from django.utils import timezone
# from django.http import JsonResponse
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()


#
#
def getcoins(request):
    if request.method == 'POST':
        try:
            inserir_preco = False
            coin_list = cg.get_coins_list(include_platform=True)
            if(total_moeda() == len(coin_list)):
                print("getcoins-3-Todas as moedas já incluídas.")
            else:             
                cont=0
                count_erro=0
                print(f'Moedas {len(coin_list)} a serem incluídas.')
                for coin in coin_list[:len(coin_list)]:

                    if(inserir_preco):

                        try:
                            #value_coin_list = cg.get_price(ids=coin['id'], vs_currencies='brl')
                            value_coin_list = {0}
                            print('LEN: ', len(value_coin_list))                        
                            if(len(value_coin_list) > 1):
                                #print('11value_coin_list tem valor')
                                #print(f"ID: {coin['id']}, Símbolo: {coin['symbol']}, Nome: {coin['name']}, Plataformas: {coin['platforms']}")
                                try:
                                    valor = value_coin_list[coin['id']]['brl']
                                except KeyError as k:
                                    #print('primeiro erro')
                                    count_erro = count_erro+1
                                    print(f">>getcoins-9-A chave 'brl' não existe para a moeda {coin['id']} e será incuído com valor = 0.")
                                    valor = 0
                                    insere_moeda(coin['symbol'], coin['name'], coin['platforms'], valor, datetime.now(), coin['id'])
                                    print('>>getcoins-9.1 - INSERIU com valor = 0 - cont>' , cont, ' - contErro>' , count_erro, ' - ' , coin['id'])  
                                
                                #print('22value_coin_list tem id: ' + coin['id'] + ' e brl!')
                                if (valor):
                                    cont = cont+1
                                    print('33', coin['symbol'], coin['name'], coin['platforms'], valor, datetime.now(), coin['id'])
                                    insere_moeda(coin['symbol'], coin['name'], coin['platforms'], valor, datetime.now(), coin['id']) 
                                    print('44getcoins-7.1 - INSERIU - cont>' , cont, ' - contErro>' , count_erro, ' - ' , coin['id'])                                              
                            else:
                                count_erro = count_erro+1
                                #eerro no campo valor
                                #print('>>getcoins-7+7+7+8-Errro:::::', valor, ' - contErro>' , count_erro)
                                print('>>getcoins-7+7+7+8-Errro:::::', ' - contErro>' , count_erro)
                    
                        except Exception as e:
                            print('erro generico')
                            count_erro = count_erro+1
                            print('e:', e, ' - contErro>' , count_erro)
                            print(f">>getcoins-10-Não ecxiste preço BRL na def getcoins ERRO VÉI: {e} - ERRO TIO: {e.__cause__}")
                            return redirect('CCCCCCCCCCC')
                    else:
                        #Insere somente a moeda sem o preço
                        cont+=cont
                        valor = 0
                        #print('55', coin['symbol'], coin['name'], coin['platforms'], valor, datetime.now(), coin['id'])
                        insere_moeda(coin['symbol'], coin['name'], coin['platforms'], valor, datetime.now(), coin['id']) 

                #2 FIM
                if(coin_list):
                    print("getcoins-11-Incluiu!")
                    print('cont:', cont)
                    print('count_erro:', count_erro)
                    return redirect('moedas_list')
            
        except Exception as xe:
            print('Erro exception: ', xe)
            count_erro+=count_erro
            valor = 0
            plat = 0
            insere_moeda(coin['symbol'], coin['name'], plat, valor, datetime.now(), coin['id'])
            print('>>66 - INSERIU?  - cont>' , count_erro, ' - ' , coin['id'])
        
    else: # Se a requisição não for POST, redirecione ou faça outra coisa
        print ('passou8')
        return HttpResponse("Método <> POST --- não permitido!!!!!!!!!!", status=405)
#
#

#
#
def total_moeda() -> int | None:
    print('executa total_moeda()')
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    query = "select Count(*) from coins_moedas;"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    conn.close()

    try:
        count = int(count)
    except (ValueError, TypeError):
        return None
    
    print('executa total_moeda():', count)
    return count
#
#

#
#
def selectComCursor():
    #print ('total_moeda')
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    query = "select * from coins_moedas;"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
#
#

#
#Função para inserir os dados no banco de dados SQLite
def insere_moeda(symbol, name, platforms, currency, data, idn):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    name = name.replace("'", "''")
    query = "INSERT INTO coins_moedas (symbol, name, platforms, currency, data, idn) " \
            f"VALUES ('{symbol}', '{name}', '{json.dumps(platforms)}', {currency}, '{data}', '{idn}');"
    #print(query)
    cursor.execute(query)
    conn.commit()
    conn.close()
#
#

#
#
class MoedasListView(ListView):
    model = Moedas #Procura o nome da APP e o nome do modelo

    def post(self, request, *args, **kwargs):
        print('MoedasListView', request.POST)
        if 'importar_btn' in request.POST: # Usa o nome do seu botão como identificador
            try:
               print(">>>>>>>>>>>>>>>Abrindo form...")
               return redirect('moedas_importar')
            except Exception as e:
                # Trate erros
                print(f"Erro ao abrir form importar moedas: {e}")
                # Você pode adicionar uma mensagem de erro ao contexto, se desejar
                context = self.get_context_data(**kwargs)
                context['error_message'] = f"Erro: {e}"
                return self.render_to_response(context)
        
        # Se for outro tipo de POST, volte para a lógica padrão
        print("ERRO MoedasListView?...")
        return super().post(request, *args, **kwargs)
#
#

#
#
class MoedasImportListView(ListView):
    model = Moedas #Procura o nome da APP e o nome do modelo        

    def post(self, request, *args, **kwargs):
        print('MoedasImportListView', request.POST)
        if 'importar_btn' in request.POST: # Usa o nome do seu botão como identificador
            try:
               #print("EXECUTA getcoins...")
               #getcoins(request)
               print("REDIRECIONA para moedas_importar...")
               return redirect('moedas_importar') 
            except Exception as e:
                # Trate erros
                print(f"Erro ao importar moedas: {e}")
                # Você pode adicionar uma mensagem de erro ao contexto, se desejar
                context = self.get_context_data(**kwargs)
                context['error_message'] = f"Erro: {e}"
                return self.render_to_response(context)
      
        # Se for outro tipo de POST, volte para a lógica padrão
        print("ERRO MoedasImportListView?...")
        return super().post(request, *args, **kwargs)
#
#

#
#
class MoedasImportarListView(ListView):
    model = Moedas #Procura o nome da APP e o nome do modelo        

    def post(self, request, *args, **kwargs):
        print('MoedasImportarListView', request.POST)
        if 'getcoins_btn' in request.POST:
            try:
               print("EXECUTA getcoins...")
               getcoins(request)
               print("REDIRECIONA para moedas_list...")
               return redirect('moedas_list') 
            except Exception as e:
                # Trate erros
                print(f"Erro ao importar moedas: {e}")
                # Você pode adicionar uma mensagem de erro ao contexto, se desejar
                context = self.get_context_data(**kwargs)
                context['error_message'] = f"Erro: {e}"
                return self.render_to_response(context)
      
        # Se for outro tipo de POST, volte para a lógica padrão
        print("ERRO MoedasImportarListView?...")
        return super().post(request, *args, **kwargs)

    



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