# loja/urls.py
from django.urls import path
from .views import (
    ListaProdutosView,
    ProdutoDetailView,
    lista_produtos_filtrada,
    adicionar_ao_carrinho,
    remover_do_carrinho,
    ver_carrinho,
    checkout,
    sobre,
    contato,
    cadastrar_produto,
    meus_produtos,
    editar_produto,
    excluir_produto,
    )

urlpatterns = [
    path('', ListaProdutosView.as_view(), name='lista_produtos'),
    path('produto/<int:pk>/', ProdutoDetailView.as_view(), name='produto_detail'),
    path('filtrados/', lista_produtos_filtrada, name='produtos_filtrados'),
    path('adicionar/<int:produto_id>/', adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('remover/<int:produto_id>/', remover_do_carrinho, name='remover_do_carrinho'),
    path('carrinho/', ver_carrinho, name='ver_carrinho'),
    path('carrinho/checkout/', checkout, name='checkout'),
    path('sobre/', sobre, name='sobre'),
    path('contato/', contato, name='contato'),
    path('cadastrar-produto/', cadastrar_produto, name='cadastrar_produto'),
    path('meus-produtos/', meus_produtos, name='meus_produtos'),
    path('editar-produto/<int:produto_id>/', editar_produto, name='editar_produto'),
    path('excluir-produto/<int:produto_id>/', excluir_produto, name='excluir_produto'),
    ]