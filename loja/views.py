# loja/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Produto
from .forms import ProdutoForm
import django_filters
from .filters import ProdutoFilter
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from carrinho.carrinho import Carrinho

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

@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if not produto.disponivel or produto.quantidade <= 0:
        messages.error(request, f'O produto "{produto.nome}" não está disponível')
        return redirect(request.META.get('HTTP_REFERER', 'lista_produtos'))

    carrinho = Carrinho(request)
    carrinho.adicionar(produto=produto)
    messages.success(request, f'"{produto.nome}" foi adicionado com sucesso')
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

@login_required
def cadastrar_produto(request):
    # Buscar todos os produtos para exibir na listagem
    produtos = Produto.objects.all().order_by('-id')
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            produto = form.save()
            messages.success(request, f'Produto "{produto.nome}" cadastrado com sucesso!')
            return redirect('cadastrar_produto')
    else:
        form = ProdutoForm()
    
    return render(request, 'cadastrar_produto.html', {
        'form': form,
        'produtos': produtos
    })

@login_required
def meus_produtos(request):
    produtos = Produto.objects.all().order_by('-id')
    return render(request, 'meus_produtos.html', {'produtos': produtos})

@login_required
def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, f'Produto "{produto.nome}" atualizado com sucesso!')
            return redirect('meus_produtos')
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'editar_produto.html', {'form': form, 'produto': produto})

@login_required
def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    
    if request.method == 'POST':
        nome_produto = produto.nome
        produto.delete()
        messages.success(request, f'Produto "{nome_produto}" excluído com sucesso!')
        return redirect('meus_produtos')
    
    return render(request, 'excluir_produto_confirm.html', {'produto': produto})