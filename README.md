# 🏪 TechHouse Eletrônicos

Uma loja online completa desenvolvida em Django para venda de produtos eletrônicos.

## 🚀 Funcionalidades

- ✅ **Sistema de Usuários**: Registro, login e logout
- ✅ **Catálogo de Produtos**: Lista com imagens e detalhes
- ✅ **Carrinho de Compras**: Adicionar, remover e atualizar quantidades
- ✅ **Checkout**: Finalização de compra com validação de estoque
- ✅ **Sistema de Filtros**: Pesquisa por nome, preço e disponibilidade
- ✅ **Design Responsivo**: Funciona em desktop, tablet e mobile
- ✅ **Interface Moderna**: Design elegante com animações

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.2.6
- **Frontend**: HTML5, CSS3, JavaScript
- **Banco de Dados**: SQLite
- **Estilização**: CSS customizado com gradientes e animações
- **Ícones**: Font Awesome
- **Fontes**: Google Fonts (Poppins)

## 📦 Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/techhouse-eletronicos.git
cd techhouse-eletronicos
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
```

### 3. Ative o ambiente virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instale as dependências
```bash
pip install -r requirements.txt
```

### 5. Execute as migrações
```bash
python manage.py migrate
```

### 6. Crie um superusuário (opcional)
```bash
python manage.py createsuperuser
```

### 7. Execute o servidor
```bash
python manage.py runserver
```

### 8. Acesse a aplicação
Abra seu navegador em: `http://127.0.0.1:8000/`

## 📱 Como Usar

### Para Usuários
1. **Registre-se** ou faça **login**
2. **Navegue** pelos produtos
3. **Adicione** itens ao carrinho
4. **Finalize** sua compra

### Para Administradores
1. Acesse `/admin/`
2. Use as credenciais do superusuário
3. Gerencie produtos, usuários e pedidos

## 🎨 Páginas Disponíveis

- **Home** (`/`) - Lista de produtos
- **Produtos** (`/`) - Catálogo completo
- **Detalhes** (`/produto/<id>/`) - Informações do produto
- **Pesquisar** (`/filtrados/`) - Filtros e busca
- **Carrinho** (`/carrinho/`) - Itens selecionados
- **Checkout** (`/carrinho/checkout/`) - Finalizar compra
- **Login** (`/conta/login/`) - Acesso à conta
- **Registro** (`/conta/registrar/`) - Criar conta
- **Sobre** (`/sobre/`) - Informações da empresa
- **Contato** (`/contato/`) - Dados de contato

## 🏢 Sobre a TechHouse Eletrônicos

**TechHouse Eletrônicos** é uma loja especializada em produtos eletrônicos de alta qualidade, localizada em Fraiburg - SC.

### Informações de Contato
- **Proprietária**: Yonara Adelita Ribeiro Ogliari
- **Telefone**: (47) 99644-9933
- **E-mail**: contato@techhouse.com.br
- **Localização**: Fraiburg - SC

## 📋 Estrutura do Projeto

```
techhouse-eletronicos/
├── core/                   # Configurações do Django
├── loja/                   # App principal da loja
├── conta/                  # App de usuários
├── carrinho/               # App do carrinho de compras
├── templates/              # Templates HTML
├── static/                 # Arquivos estáticos (CSS, JS)
├── media/                  # Imagens e uploads
└── manage.py              # Script de gerenciamento
```

## 🔧 Comandos Úteis

```bash
# Executar servidor
python manage.py runserver

# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Coletar arquivos estáticos
python manage.py collectstatic
```

## 📸 Screenshots

### Página Inicial
![Home](media/screenshots/home.png)

### Detalhes do Produto
![Produto](media/screenshots/produto.png)

### Carrinho de Compras
![Carrinho](media/screenshots/carrinho.png)

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Desenvolvedor

Desenvolvido com ❤️ para a TechHouse Eletrônicos

---

**TechHouse Eletrônicos: conectando você ao futuro! ⚡**

