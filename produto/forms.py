from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.urls import reverse_lazy

from produto.models import Produto

class DetalheProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto  # Replace MyModel with your actual model
        fields = ['nome', 'descricao', 'preco']

    def __init__(self, *args, pk, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = reverse_lazy('produto_list', kwargs={'pk': pk})
        self.helper.layout = Layout(
            'nome',
            'descricao',
            'preco',
            Submit('submit', 'Salvar', css_class='btn-primary') # Example submit button
        )