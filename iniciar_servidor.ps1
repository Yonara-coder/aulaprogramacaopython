# Script PowerShell para iniciar o servidor Django
# TechHouse Eletrônicos

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  TECHHOUSE ELETRONICOS - INICIAR SERVIDOR" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Verificar se Python está instalado
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[OK] Python encontrado!" -ForegroundColor Green
    Write-Host $pythonVersion
    Write-Host ""
} catch {
    Write-Host "[ERRO] Python não encontrado!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Por favor, instale o Python primeiro:"
    Write-Host "1. Abra a Microsoft Store"
    Write-Host "2. Procure por 'Python 3.11' ou 'Python 3.12'"
    Write-Host "3. Instale e reinicie este script"
    Write-Host ""
    Read-Host "Pressione Enter para sair"
    exit 1
}

# Verificar se existe ambiente virtual
if (-not (Test-Path "venv")) {
    Write-Host "[INFO] Criando ambiente virtual..." -ForegroundColor Yellow
    python -m venv venv
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERRO] Falha ao criar ambiente virtual!" -ForegroundColor Red
        Read-Host "Pressione Enter para sair"
        exit 1
    }
    
    Write-Host "[OK] Ambiente virtual criado!" -ForegroundColor Green
    Write-Host ""
    
    Write-Host "[INFO] Instalando dependências..." -ForegroundColor Yellow
    & .\venv\Scripts\Activate.ps1
    pip install django pillow django-filter
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[ERRO] Falha ao instalar dependências!" -ForegroundColor Red
        Read-Host "Pressione Enter para sair"
        exit 1
    }
    
    Write-Host "[OK] Dependências instaladas!" -ForegroundColor Green
    Write-Host ""
} else {
    Write-Host "[INFO] Ambiente virtual encontrado!" -ForegroundColor Yellow
    & .\venv\Scripts\Activate.ps1
}

# Verificar se banco de dados está configurado
if (-not (Test-Path "db.sqlite3")) {
    Write-Host "[INFO] Configurando banco de dados..." -ForegroundColor Yellow
    python manage.py makemigrations
    python manage.py migrate
    Write-Host "[OK] Banco de dados configurado!" -ForegroundColor Green
    Write-Host ""
}

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  INICIANDO SERVIDOR..." -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "O servidor será iniciado em:" -ForegroundColor Yellow
Write-Host "  http://127.0.0.1:8000/" -ForegroundColor Green
Write-Host ""
Write-Host "Pressione Ctrl+C para parar o servidor" -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

python manage.py runserver

Read-Host "`nPressione Enter para sair"


