from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'quantidade', 'imagem']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Digite o nome do produto'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Digite a descrição do produto',
                'rows': 4
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Digite o preço',
                'step': '0.01',
                'min': '0'
            }),
            'quantidade': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Digite a quantidade',
                'min': '0'
            }),
            'imagem': forms.FileInput(attrs={
                'class': 'form-input',
                'accept': 'image/*'
            })
        }
        labels = {
            'nome': 'Nome do Produto',
            'descricao': 'Descrição',
            'preco': 'Preço (R$)',
            'quantidade': 'Quantidade em Estoque',
            'imagem': 'Imagem do Produto'
        }
