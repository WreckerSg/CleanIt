# Guía de instalación y ejecución

## Opción A. Python local

### Requisitos

- Python 3.10 o superior.
- Git.
- Terminal PowerShell, Bash o equivalente.

### Instalación

Desde la raíz del repositorio:

```bash
python -m venv .venv
```

Active el entorno.

Linux o macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instale las dependencias y prepare SQLite:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

Inicie el servidor:

```bash
python manage.py runserver
```

Abra `http://127.0.0.1:8000/`.

## Opción B. Docker Compose

### Requisitos

- Docker Desktop o Docker Engine con Compose.

Copie las variables de ejemplo y cambie los valores locales:

Linux o macOS:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Construya e inicie Django y PostgreSQL. El contenedor ejecuta las migraciones,
reúne los archivos estáticos y los sirve mediante WhiteNoise y Gunicorn:

```bash
docker compose up --build -d
```

Cree el administrador inicial:

```bash
docker compose exec web python manage.py createsuperuser
```

Abra `http://127.0.0.1:8081/`. Puede cambiar el puerto externo con `WEB_PORT`
en `.env`; el puerto interno del contenedor permanece en `8000`.

Para detener los servicios sin borrar los datos:

```bash
docker compose down
```

## Verificación

Antes de proponer un cambio para `qa`:

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py collectstatic --noinput
python manage.py test
```

El resultado esperado para la versión 1.0.1 es:

- 38 pruebas ejecutadas;
- 38 pruebas aprobadas;
- 0 fallos;
- 0 problemas reportados por `check`;
- archivos estáticos recopilados correctamente;
- ninguna migración pendiente de crear.

## Solución de problemas

| Problema | Acción |
|---|---|
| `python` no se reconoce | Instale Python 3.10 o superior y habilite su acceso desde la terminal |
| `No module named django` | Active `.venv` y ejecute `pip install -r requirements.txt` |
| Migraciones pendientes | Ejecute `python manage.py migrate` |
| El puerto 8000 está ocupado | Use `python manage.py runserver 8001` |
| Docker no conecta con PostgreSQL | Revise `docker compose logs db` y los valores de `.env` |
| No puede abrir `/admin/` | Compruebe que la cuenta sea superusuario o tenga permiso de personal |

Si el puerto 8000 no está disponible en Windows, puede ejecutar:

```powershell
.\.venv\Scripts\python.exe manage.py runserver 127.0.0.1:8081
```
