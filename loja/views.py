# loja/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Produto
import django_filters
from .filters import ProdutoFilter
from django.contrib.auth.decorators import login_required
<<<<<<< HEAD
# CORREÇÃO: Importando 'messages' de uma forma segura para evitar conflitos
from django.contrib.messages import api as messages_api
=======
from django.contrib import messages
from carrinho.carrinho import Carrinho
>>>>>>> a73ac93 (codigo finalizado)

# ----- Class-Based View para lista -----
class ListaProdutosView(ListView):
    model = Produto
    template_name = 'lista_produtos.html'
    context_object_name = 'produtos'

# ----- Class-Based View para detalhe -----
class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produto_detail.html'
    context_object_name = 'produto'

def lista_produtos_filtrada(request):
    f = ProdutoFilter(request.GET, queryset=Produto.objects.all())
    return render(request, 'lista_produtos_filtrada.html', {'filter': f})

<<<<<<< HEAD

=======
@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if not produto.disponivel or produto.quantidade <= 0:
        messages.error(request, f'O produto "{produto.nome}" não está disponível')
        return redirect(request.META.get('HTTP_REFERER', 'lista_produtos'))

    carrinho = Carrinho(request)
    
    # Verificar se foi enviada uma quantidade específica
    quantidade = 1
    if request.method == 'POST' and 'quantidade' in request.POST:
        try:
            quantidade = int(request.POST['quantidade'])
            if quantidade <= 0:
                quantidade = 1
        except (ValueError, TypeError):
            quantidade = 1
    
    # Verificar se há estoque suficiente
    if quantidade > produto.quantidade:
        messages.error(request, f'Quantidade solicitada ({quantidade}) maior que o estoque disponível ({produto.quantidade})')
        return redirect(request.META.get('HTTP_REFERER', 'lista_produtos'))
    
    # Adicionar a quantidade especificada ao carrinho
    for _ in range(quantidade):
        carrinho.adicionar(produto=produto)
    
    messages.success(request, f'"{produto.nome}" (x{quantidade}) foi adicionado com sucesso')
    return redirect('ver_carrinho')

@login_required
def ver_carrinho(request):
    carrinho = Carrinho(request)
    return render(request, 'carrinho.html', {'carrinho': carrinho})

@login_required
def remover_do_carrinho(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho.remover(produto)
    messages.success(request, f'"{produto.nome}" foi removido do carrinho')
    return redirect('ver_carrinho')

@login_required
def checkout(request):
    carrinho = Carrinho(request)
    
    if not carrinho:
        messages.error(request, 'Seu carrinho está vazio')
        return redirect('ver_carrinho')
    
    # Verificar estoque antes de finalizar
    for item in carrinho:
        produto = item['produto']
        quantidade_comprada = item['quantidade']

        if produto.quantidade < quantidade_comprada:
            messages.error(request, f'O produto "{produto.nome}" não tem estoque suficiente')
            return redirect('ver_carrinho')
    
    # Atualizar estoque
    for item in carrinho:
        produto = item['produto']
        quantidade_comprada = item['quantidade']
        produto.quantidade -= quantidade_comprada
        produto.save()
    
    carrinho.limpar()
    messages.success(request, 'Compra realizada com sucesso!')
    return render(request, 'checkout_concluido.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')
>>>>>>> a73ac93 (codigo finalizado)
