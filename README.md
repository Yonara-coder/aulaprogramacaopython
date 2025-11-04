# 🛒 TechHouse Eletrônicos - E-commerce Django

Sistema completo de e-commerce desenvolvido em Django com funcionalidades modernas de carrinho de compras, autenticação de usuários e administração de produtos.

## ✨ Funcionalidades

### 🛍️ **E-commerce Completo**

* ✅ Listagem de produtos com design responsivo
* ✅ Página de detalhes do produto com galeria de imagens
* ✅ Carrinho de compras funcional com sessões
* ✅ Sistema de checkout com verificação de estoque
* ✅ Cálculo automático de parcelas

### 👤 **Sistema de Usuários**

* ✅ Cadastro de usuários com validação
* ✅ Login e logout seguros
* ✅ Páginas de "Sobre" e "Contato"
* ✅ Interface de usuário moderna

### 🛠️ **Administração de Produtos**

* ✅ Cadastro de produtos com upload de imagem
* ✅ Edição completa de produtos existentes
* ✅ Exclusão de produtos com confirmação
* ✅ Listagem com busca e filtros
* ✅ Interface de administração unificada

### 🎨 **Design Moderno**

* ✅ Interface responsiva (mobile-first)
* ✅ Design heurístico profissional
* ✅ Gradientes e animações suaves
* ✅ Ícones Font Awesome
* ✅ Paleta de cores harmoniosa

## 🛠️ Tecnologias Utilizadas

* **Backend:** Django 5.2.6
* **Frontend:** HTML5, CSS3, JavaScript
* **Banco de Dados:** SQLite (desenvolvimento)
* **Imagens:** Sistema de upload com Django
* **Estilização:** CSS Grid, Flexbox, Gradientes
* **Ícones:** Font Awesome 6

## 📦 Estrutura do Projeto

```
aulaprogramacaopython-master/
├── core/                    # Configurações do Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── loja/                    # App principal da loja
│   ├── models.py           # Modelo de Produto
│   ├── views.py            # Views do e-commerce
│   ├── urls.py             # URLs da loja
│   ├── forms.py            # Formulários
│   └── management/         # Comandos personalizados
├── carrinho/               # Sistema de carrinho
│   ├── carrinho.py         # Lógica do carrinho
│   └── context_processor.py
├── conta/                  # Sistema de usuários
│   ├── views.py
│   └── forms.py
├── templates/              # Templates HTML
│   ├── base.html
│   ├── lista_produtos.html
│   ├── produto_detail.html
│   ├── carrinho.html
│   ├── cadastrar_produto.html
│   └── partials/
├── static/                 # Arquivos estáticos
│   └── loja/
│       └── style.css
├── media/                  # Uploads de imagens
└── manage.py

```

## 🚀 Como Executar

### **1. Clonar o Repositório**

```bash
git clone https://github.com/Yonara-coder/Loja-da-kika-.git
cd Loja-da-kika-
```

### **2. Criar Ambiente Virtual**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### **3. Instalar Dependências**

```bash
pip install django pillow django-filter
```

### **4. Configurar Banco de Dados**

```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Criar Superusuário**

```bash
python manage.py createsuperuser
```

### **6. Adicionar Produtos de Exemplo**

```bash
python manage.py add_produtos
```

### **7. Executar Servidor**

```bash
python manage.py runserver
```

### **8. Acessar o Sistema**

* **Loja:** http://127.0.0.1:8000/
* **Admin:** http://127.0.0.1:8000/admin/
* **Cadastrar Produtos:** http://127.0.0.1:8000/cadastrar-produto/

## 📱 Páginas do Sistema

### **🛒 E-commerce**

* **Página Inicial:** Lista de produtos com filtros
* **Detalhes do Produto:** Informações completas e adicionar ao carrinho
* **Carrinho:** Gerenciar itens e finalizar compra
* **Checkout:** Processo de finalização da compra

### **👤 Usuários**

* **Login:** Autenticação de usuários
* **Registro:** Cadastro de novos usuários
* **Sobre:** Informações sobre a empresa
* **Contato:** Formulário de contato

### **🛠️ Administração**

* **Cadastrar Produto:** Formulário + listagem completa
* **Meus Produtos:** Gerenciar produtos cadastrados
* **Editar Produto:** Modificar informações
* **Excluir Produto:** Remover com confirmação

## 🎨 Características do Design

### **Design Heurístico**

* ✅ Layout intuitivo e familiar
* ✅ Navegação clara e consistente
* ✅ Feedback visual para todas as ações
* ✅ Hierarquia visual bem definida

### **Responsividade**

* ✅ Mobile-first design
* ✅ Breakpoints para tablet e desktop
* ✅ Grid system flexível
* ✅ Componentes adaptáveis

### **Interatividade**

* ✅ Hover effects suaves
* ✅ Transições animadas
* ✅ Busca em tempo real
* ✅ Filtros dinâmicos

## 🔧 Funcionalidades Técnicas

### **Sistema de Carrinho**

* Sessões Django para persistência
* Cálculo automático de totais
* Verificação de estoque
* Atualização de quantidades

### **Upload de Imagens**

* Suporte a múltiplos formatos
* Redimensionamento automático
* Placeholder para produtos sem imagem
* Otimização para web

### **Validação de Formulários**

* Validação client-side e server-side
* Mensagens de erro contextuais
* Campos obrigatórios marcados
* Sanitização de dados

## 📊 Banco de Dados

### **Modelo Produto**

* `nome`: Nome do produto
* `descricao`: Descrição detalhada
* `preco`: Preço em decimal
* `quantidade`: Estoque disponível
* `disponivel`: Status de disponibilidade
* `imagem`: Upload de imagem

## 🚀 Deploy

### **Configurações para Produção**

1. Configurar `DEBUG = False`
2. Configurar `ALLOWED_HOSTS`
3. Configurar banco de dados PostgreSQL
4. Configurar arquivos estáticos
5. Configurar servidor web (Nginx + Gunicorn)

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👨‍💻 Desenvolvedor

**Yonara-coder**

* GitHub: @Yonara-coder
* Projeto: Sistema de E-commerce Django

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:

* Reportar bugs
* Sugerir melhorias
* Enviar pull requests
* Compartilhar o projeto

---

**⭐ Se este projeto te ajudou, considere dar uma estrela no repositório!**