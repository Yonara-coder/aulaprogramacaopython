@echo off
echo ========================================
echo   TECHHOUSE ELETRONICOS - INICIAR SERVIDOR
echo ========================================
echo.

REM Verificar se Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado!
    echo.
    echo Por favor, instale o Python primeiro:
    echo 1. Abra a Microsoft Store
    echo 2. Procure por "Python 3.11" ou "Python 3.12"
    echo 3. Instale e reinicie este script
    echo.
    pause
    exit /b 1
)

echo [OK] Python encontrado!
python --version
echo.

REM Verificar se existe ambiente virtual
if not exist "venv\" (
    echo [INFO] Criando ambiente virtual...
    python -m venv venv
    if errorlevel 1 (
        echo [ERRO] Falha ao criar ambiente virtual!
        pause
        exit /b 1
    )
    echo [OK] Ambiente virtual criado!
    echo.
    
    echo [INFO] Instalando dependencias...
    call venv\Scripts\activate.bat
    pip install django pillow django-filter
    if errorlevel 1 (
        echo [ERRO] Falha ao instalar dependencias!
        pause
        exit /b 1
    )
    echo [OK] Dependencias instaladas!
    echo.
) else (
    echo [INFO] Ambiente virtual encontrado!
    call venv\Scripts\activate.bat
)

REM Verificar se banco de dados esta configurado
if not exist "db.sqlite3" (
    echo [INFO] Configurando banco de dados...
    python manage.py makemigrations
    python manage.py migrate
    echo [OK] Banco de dados configurado!
    echo.
)

echo ========================================
echo   INICIANDO SERVIDOR...
echo ========================================
echo.
echo O servidor sera iniciado em:
echo   http://127.0.0.1:8000/
echo.
echo Pressione Ctrl+C para parar o servidor
echo.
echo ========================================
echo.

python manage.py runserver

pause


