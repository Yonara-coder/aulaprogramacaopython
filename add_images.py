import os
import sys
import django

# Adicionar o diretório do projeto ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from loja.models import Produto

def add_sample_images():
    # Atualizar produtos para ter imagens placeholder
    produtos = Produto.objects.all()
    
    for produto in produtos:
        if not produto.imagem:
            # Criar um nome de arquivo baseado no ID do produto
            filename = f"produto_{produto.id}.jpg"
            # Definir um caminho de imagem placeholder
            produto.imagem = f"produtos/{filename}"
            produto.save()
            print(f"Imagem placeholder definida para: {produto.nome}")
        else:
            print(f"Produto {produto.nome} já tem imagem")

if __name__ == "__main__":
    add_sample_images()
