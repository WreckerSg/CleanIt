# Descripción y justificación técnica de CleanIt

## 1. Estado técnico

CleanIt ya no es solo una propuesta documental. El incremento 2.1 contiene una aplicación Django ejecutable con autenticación, roles, panel diferenciado, administración y pruebas automatizadas. Se encuentra en `dev` hasta completar su revisión.

## 2. Tecnologías utilizadas

| Área | Tecnología versionada | Uso real en el incremento 2.1 |
|---|---|---|
| Lenguaje | Python 3.12 | Configuración, modelos, vistas y pruebas |
| Framework web | Django 5.2.17 LTS | Autenticación, autorización, ORM, migraciones, plantillas, administración y pruebas |
| Interfaz | Plantillas Django, HTML5 y CSS3 | Página de acceso, panel adaptable y controles por rol |
| Base de datos local | SQLite | Ejecución y pruebas rápidas sin servicios externos |
| Base de datos integrada | PostgreSQL 16 | Servicio persistente definido en Docker Compose |
| Servidor de aplicación | Gunicorn 23.0.0 | Ejecución WSGI dentro del contenedor web |
| Contenedores | Docker y Docker Compose | Reproducción de Django y PostgreSQL |
| Versionamiento | Git y GitHub | Flujo `dev` → `qa` → `pre-main` → `main` |

Bootstrap continúa dentro del stack aprobado para componentes posteriores. El incremento 2.1 usa una hoja CSS propia y pequeña para evitar incorporar componentes que aún no requiere. Su introducción se registrará cuando se implementen listados y formularios del producto.

## 3. Justificación de las decisiones

### Python y Django

El producto es principalmente transaccional y CRUD: usuarios, tareas, responsables, frecuencias e historial. Django reúne en un solo framework la autenticación, el hash de contraseñas, los permisos, las validaciones, las migraciones, el ORM, las plantillas y las pruebas. Esto reduce la cantidad de tecnologías que debe mantener el equipo.

Se eligió Django **5.2.17 LTS** para priorizar estabilidad y soporte extendido durante el desarrollo académico.

### Plantillas renderizadas en el servidor

CleanIt no necesita inicialmente un frontend independiente. Django genera el HTML y valida en el servidor quién puede consultar cada función. Esta arquitectura evita mantener dos proyectos, dos cadenas de compilación y una API pública antes de que sean necesarias.

### PostgreSQL y SQLite

PostgreSQL será la base integrada porque permite relaciones, restricciones y transacciones para proteger la coherencia entre usuarios, tareas y cumplimientos. SQLite se conserva como alternativa local predeterminada para iniciar el proyecto y ejecutar pruebas sin instalar un servidor de base de datos.

La selección se realiza automáticamente: si existe `DATABASE_HOST`, Django usa PostgreSQL; de lo contrario usa SQLite.

### Docker Compose

El archivo `compose.yaml` describe los servicios `web` y `db`, comprueba la disponibilidad de PostgreSQL antes de iniciar Django y conserva los datos en un volumen. De esta forma el equipo puede repetir el mismo ambiente sin instalar PostgreSQL directamente.

## 4. Arquitectura implementada

```mermaid
flowchart TD
    N["Navegador"] --> D["Django"]
    D --> T["Plantillas y CSS"]
    D --> O["Django ORM"]
    O --> B[("SQLite o PostgreSQL")]
```

Es un monolito modular. En este incremento existen:

- `accounts`: usuario personalizado, roles, administración y rutas de sesión;
- `core`: panel principal y presentación según permisos;
- `config`: configuración, rutas globales y entrada WSGI/ASGI;
- `templates`: vistas HTML compartidas;
- `static`: estilos de la interfaz.

## 5. Seguridad implementada

- Todas las páginas funcionales requieren sesión.
- Django gestiona el hash de las contraseñas.
- Las cuentas inactivas no pueden autenticarse.
- El panel cambia según el rol evaluado en el servidor.
- El cierre de sesión exige `POST` y token CSRF.
- Se habilitaron protección CSRF, `X-Frame-Options: DENY` y `nosniff`.
- Las cookies de sesión y CSRF están marcadas como `HttpOnly`.
- Los secretos y bases locales están excluidos de Git; fuera de `DEBUG`, la clave secreta es obligatoria.

Antes de producción aún será obligatorio desactivar `DEBUG`, definir una clave secreta real, configurar HTTPS y ejecutar `check --deploy`.

## 6. Persistencia y migraciones

El modelo `accounts.User` amplía `AbstractUser` e incorpora:

- correo electrónico único;
- rol `ADMIN` o `PARTICIPANT`;
- estado activo heredado de Django;
- reconocimiento de superusuarios como administradores funcionales.

La migración `accounts/0001_initial.py` crea el esquema de usuarios de forma repetible.

## 7. Pruebas automatizadas actuales

La suite contiene seis verificaciones:

| Grupo | Verificación |
|---|---|
| Modelo | Un usuario nuevo recibe el rol Participante |
| Modelo | El rol Administrador se reconoce correctamente |
| Autenticación | Una cuenta inactiva no puede ingresar |
| Acceso | El panel redirige a quien no tiene sesión |
| Autorización | El participante no ve la administración |
| Autorización | El administrador sí ve su opción de gestión |

Comandos de control:

```bash
python manage.py test
python manage.py check
python manage.py makemigrations --check --dry-run
```

La ejecución local del incremento 2.1 produjo **6 pruebas aprobadas, 0 fallidas** y **0 problemas en la comprobación de Django**. La evidencia formal se generará de nuevo al promover el cambio a `qa`.

## 8. Limitaciones actuales

- Todavía no existen modelos de zonas, tareas ni cumplimientos.
- No se ha ejecutado la validación formal en `qa`.
- Docker no pudo ejecutarse dentro del ambiente de edición actual; su configuración debe comprobarse en un equipo con Docker Desktop o Docker Engine.
- No existe un despliegue público.
- Las tarjetas funcionales del panel son informativas hasta los siguientes incrementos.
