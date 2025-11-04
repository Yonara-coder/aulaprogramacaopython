# 🧪 Como Testar o Projeto TechHouse Eletrônicos

## ⚠️ Pré-requisitos

Antes de testar, você precisa ter o **Python instalado** no seu computador.

### 📥 Instalar Python

**Opção 1 - Microsoft Store (Recomendado):**
1. Abra a Microsoft Store
2. Procure por "Python 3.11" ou "Python 3.12"
3. Clique em "Instalar"

**Opção 2 - Site Oficial:**
1. Acesse: https://www.python.org/downloads/
2. Baixe a versão mais recente
3. **IMPORTANTE:** Durante a instalação, marque ✅ "Add Python to PATH"

### ✅ Verificar Instalação

Abra um novo terminal (PowerShell ou CMD) e digite:
```bash
python --version
```

Se aparecer algo como `Python 3.11.x` ou `Python 3.12.x`, está funcionando! ✅

---

## 🚀 Passos para Testar

### 1️⃣ **Navegar para a Pasta do Projeto**

```bash
cd "C:\Users\Micro\Desktop\Bkp yonara\aulaprogramacaopython"
```

### 2️⃣ **Criar Ambiente Virtual (Recomendado)**

```bash
python -m venv venv
```

### 3️⃣ **Ativar Ambiente Virtual**

```bash
# Windows PowerShell
venv\Scripts\Activate.ps1

# Windows CMD
venv\Scripts\activate.bat
```

### 4️⃣ **Instalar Dependências**

```bash
pip install django pillow django-filter
```

### 5️⃣ **Configurar Banco de Dados**

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ **Criar Superusuário (Opcional)**

```bash
python manage.py createsuperuser
```

Siga as instruções na tela para criar um usuário admin.

### 7️⃣ **Executar Servidor**

```bash
python manage.py runserver
```

Você verá uma mensagem como:
```
Starting development server at http://127.0.0.1:8000/
```

### 8️⃣ **Abrir no Navegador**

Abra seu navegador e acesse:

- 🏠 **Página Principal:** http://127.0.0.1:8000/
- 👤 **Admin Django:** http://127.0.0.1:8000/admin/
- 📝 **Cadastrar Produto:** http://127.0.0.1:8000/cadastrar-produto/

---

## ✅ Checklist de Testes

### 🧪 Testes Básicos

- [ ] **Página inicial carrega** sem erros
- [ ] **Navegação funciona** - todos os links do menu
- [ ] **Design responsivo** - teste redimensionando a janela
- [ ] **Cores e estilos** aparecem corretamente

### 🛍️ Testes de Produtos

- [ ] **Lista de produtos** exibe corretamente
- [ ] **Detalhes do produto** abre ao clicar
- [ ] **Imagens** aparecem (ou placeholder)
- [ ] **Botão "Adicionar ao Carrinho"** funciona

### 🛒 Testes de Carrinho

- [ ] **Adicionar produto** ao carrinho
- [ ] **Ver carrinho** mostra itens adicionados
- [ ] **Aumentar/Diminuir quantidade** funciona
- [ ] **Remover item** do carrinho
- [ ] **Finalizar compra** funciona

### 👤 Testes de Usuário

- [ ] **Registrar nova conta** funciona
- [ ] **Login** funciona
- [ ] **Logout** funciona
- [ ] **Menu do usuário** abre e fecha

### 🛠️ Testes de Administração

- [ ] **Cadastrar produto** funciona
- [ ] **Editar produto** funciona
- [ ] **Excluir produto** funciona
- [ ] **Busca e filtros** funcionam

### 📱 Testes de Responsividade

- [ ] **Mobile** (< 640px) - layout adapta corretamente
- [ ] **Tablet** (768px) - layout intermediário
- [ ] **Desktop** (> 1024px) - layout completo

### ♿ Testes de Acessibilidade

- [ ] **Navegação por teclado** funciona (Tab, Enter, ESC)
- [ ] **Foco visível** em todos os elementos
- [ ] **Menu dropdown** fecha com ESC
- [ ] **Mensagens** são lidas por leitores de tela

---

## 🐛 Solução de Problemas

### ❌ Erro: "Python não foi encontrado"

**Solução:**
1. Instale o Python seguindo os passos acima
2. Reinicie o terminal após instalar
3. Verifique com `python --version`

### ❌ Erro: "No module named 'django'"

**Solução:**
```bash
pip install django pillow django-filter
```

### ❌ Erro: "ModuleNotFoundError"

**Solução:**
Certifique-se de estar na pasta correta do projeto e que o ambiente virtual está ativado.

### ❌ Erro: "Port already in use"

**Solução:**
```bash
# Use outra porta
python manage.py runserver 8001
```

### ❌ Erro: "Database is locked"

**Solução:**
Feche qualquer programa que esteja usando o banco de dados (SQLite Browser, etc.)

---

## 📊 Comandos Úteis

```bash
# Ver rotas disponíveis
python manage.py show_urls

# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Coletar arquivos estáticos (produção)
python manage.py collectstatic

# Executar testes
python manage.py test
```

---

## 🎯 Testes Avançados

### Testar com Dados de Exemplo

```bash
# Adicionar produtos de exemplo (se houver comando)
python manage.py add_produtos
```

### Testar Performance

- Abra o DevTools (F12)
- Vá na aba "Network"
- Recarregue a página
- Verifique o tempo de carregamento

### Testar em Diferentes Navegadores

- ✅ Chrome
- ✅ Firefox
- ✅ Edge
- ✅ Safari (se tiver Mac)

---

## 📝 Notas Importantes

1. **Sempre ative o ambiente virtual** antes de trabalhar
2. **Não feche o terminal** enquanto o servidor estiver rodando
3. **Use Ctrl+C** para parar o servidor
4. **Mantenha o Python atualizado** para segurança

---

## 🎉 Pronto para Testar!

Siga os passos acima e você terá o projeto rodando em minutos!

**Precisa de ajuda?** Verifique os logs de erro no terminal para identificar problemas específicos.

---

**Última atualização:** 2025


