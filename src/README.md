# Código fuente

Esta carpeta contiene la aplicación web ejecutable de CleanIt.

Los incrementos 2.1 y 2.2 del Paso 2 incluyen:

- Configuración base en Django.
- Usuarios con roles de administrador y participante.
- Inicio y cierre de sesión.
- Panel inicial adaptado al rol autenticado.
- Panel administrativo de Django.
- Gestión web de zonas y tareas para el administrador.
- Responsable, frecuencia, próxima fecha y retiro lógico.
- Pruebas automatizadas de acceso, permisos, validaciones y CRUD.

## Ejecución local

Desde la raíz del repositorio:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

En Windows PowerShell, activa el entorno con:

```powershell
.venv\Scripts\Activate.ps1
```

La aplicación quedará disponible en `http://127.0.0.1:8000/`.
