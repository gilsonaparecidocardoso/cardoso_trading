from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from produto.forms import DetalheProdutoForm
from .models import Produto

# View para listar produtos
class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/produto_list.html'

# View para criar um novo produto
class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco']
    template_name = 'produtos/produto_form.html'
    success_url = reverse_lazy('produto_list')

# View para atualizar um produto existente
class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco']
    template_name = 'produtos/produto_form.html'
    success_url = reverse_lazy('produto_list')
    def get_success_url(self):
        print("ei")
        # Acessa o objeto (self.object) para obter o valor do argumento
        return reverse_lazy('produto_list', kwargs={'pk': self.produto.pk})

# View para deletar um produto
class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produtos/produto_confirm_delete.html'
    success_url = reverse_lazy('produto_list')

class ProdutoDetailView(DetailView):
#     model = Produto
#     template_name = 'produtos/produto_detail.html' # O template que será renderizado
#     context_object_name = 'produto' # O nome da variável no template
      model = Produto
      template_name = 'produtos/produto_detail.html'

      def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          # If you want to display data using a form:
          #context['form'] = DetalheProdutoForm(instance=self.object)

          context['form'] = DetalheProdutoForm(pk=self.kwargs['pk'])
          return context