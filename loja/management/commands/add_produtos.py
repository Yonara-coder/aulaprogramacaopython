from django.core.management.base import BaseCommand
from loja.models import Produto
from decimal import Decimal
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Adiciona produtos de exemplo à loja'

    def handle(self, *args, **options):
        # Criar diretório de imagens se não existir
        media_dir = os.path.join(settings.MEDIA_ROOT, 'produtos')
        os.makedirs(media_dir, exist_ok=True)

        produtos_data = [
            {
                'nome': 'Smartphone Samsung Galaxy S24',
                'preco': Decimal('2999.99'),
                'quantidade': 15,
                'imagem': 'produtos/smartphone.jpg'
            },
            {
                'nome': 'Notebook Dell Inspiron 15',
                'preco': Decimal('2499.99'),
                'quantidade': 8,
                'imagem': 'produtos/notebook.jpg'
            },
            {
                'nome': 'Fone de Ouvido Sony WH-1000XM4',
                'preco': Decimal('899.99'),
                'quantidade': 20,
                'imagem': 'produtos/fone.jpg'
            },
            {
                'nome': 'Smartwatch Apple Watch Series 9',
                'preco': Decimal('1899.99'),
                'quantidade': 12,
                'imagem': 'produtos/smartwatch.jpg'
            },
            {
                'nome': 'Tablet iPad Air 5ª Geração',
                'preco': Decimal('3299.99'),
                'quantidade': 6,
                'imagem': 'produtos/tablet.jpg'
            },
            {
                'nome': 'Câmera Canon EOS R6 Mark II',
                'preco': Decimal('8999.99'),
                'quantidade': 4,
                'imagem': 'produtos/camera.jpg'
            },
            {
                'nome': 'Console PlayStation 5',
                'preco': Decimal('3999.99'),
                'quantidade': 10,
                'imagem': 'produtos/ps5.jpg'
            },
            {
                'nome': 'Monitor LG UltraWide 34"',
                'preco': Decimal('1299.99'),
                'quantidade': 7,
                'imagem': 'produtos/monitor.jpg'
            },
            {
                'nome': 'Teclado Mecânico Logitech MX Keys',
                'preco': Decimal('299.99'),
                'quantidade': 25,
                'imagem': 'produtos/teclado.jpg'
            },
            {
                'nome': 'Mouse Gamer Razer DeathAdder V3',
                'preco': Decimal('199.99'),
                'quantidade': 30,
                'imagem': 'produtos/mouse.jpg'
            }
        ]

        created_count = 0
        for produto_data in produtos_data:
            produto, created = Produto.objects.get_or_create(
                nome=produto_data['nome'],
                defaults={
                    'preco': produto_data['preco'],
                    'quantidade': produto_data['quantidade'],
                    'disponivel': True
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Produto criado: {produto.nome}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Produto já existe: {produto.nome}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Processo concluído! {created_count} produtos criados.')
        )

