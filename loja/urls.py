# loja/urls.py
from django.urls import path
<<<<<<< HEAD
=======
from django.views.generic import TemplateView
>>>>>>> a73ac93 (codigo finalizado)
from .views import (
    ListaProdutosView, 
    ProdutoDetailView, 
    lista_produtos_filtrada,
<<<<<<< HEAD
=======
    adicionar_ao_carrinho,
    remover_do_carrinho,
    ver_carrinho,
    checkout,
    sobre,
    contato,
>>>>>>> a73ac93 (codigo finalizado)
    )

urlpatterns = [
    path('', ListaProdutosView.as_view(), name='lista_produtos'),
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('filtrados/', lista_produtos_filtrada, name='produtos_filtrados'),
<<<<<<< HEAD
=======
    path('adicionar/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:produto_id>/', remover_do_carrinho, name='remover_do_carrinho'),
    path('carrinho/', ver_carrinho, name='ver_carrinho'),
    path('carrinho/checkout/', checkout, name='checkout'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),
>>>>>>> a73ac93 (codigo finalizado)
    ]
