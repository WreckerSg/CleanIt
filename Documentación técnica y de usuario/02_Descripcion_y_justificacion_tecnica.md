# Descripción y justificación técnica de CleanIt

## 1. Estado técnico

CleanIt ya no es solo una propuesta documental. La versión candidata 1.0.0 contiene una aplicación Django ejecutable con autenticación, roles, panel diferenciado, administración de cuentas, zonas, tareas, pendientes, vencimientos, cumplimiento, recurrencias, filtros e historial.

## 2. Tecnologías utilizadas

| Área | Tecnología versionada | Uso real en la versión 1.0.0 |
|---|---|---|
| Lenguaje | Python 3.10 o superior | Configuración, modelos, vistas y pruebas; Docker utiliza Python 3.12 |
| Framework web | Django 5.2.17 LTS | Autenticación, autorización, ORM, migraciones, plantillas, administración y pruebas |
| Interfaz | Plantillas Django, HTML5 y CSS3 | Acceso, panel, formularios y tablas adaptables |
| Base de datos local | SQLite | Ejecución y pruebas rápidas sin servicios externos |
| Base de datos integrada | PostgreSQL 16 | Servicio persistente definido en Docker Compose |
| Servidor de aplicación | Gunicorn 23.0.0 | Ejecución WSGI dentro del contenedor web |
| Contenedores | Docker y Docker Compose | Reproducción de Django y PostgreSQL |
| Versionamiento | Git y GitHub | Flujo `dev` → `qa` → `pre-main` → `main` |

Bootstrap continúa como alternativa del stack aprobado, pero no se incorporó todavía. La interfaz actual utiliza una hoja CSS propia y no depende de recursos externos para mostrar el acceso, los formularios ni los listados. Si se adopta Bootstrap más adelante, el cambio deberá simplificar estilos existentes y quedar registrado.

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
- `chores`: zonas, tareas, responsables, frecuencias, formularios y permisos de administración;
- `core`: panel principal y presentación según permisos;
- `config`: configuración, rutas globales y entrada WSGI/ASGI;
- `templates`: vistas HTML compartidas;
- `static`: estilos de la interfaz.

## 5. Seguridad implementada

- Todas las páginas funcionales requieren sesión.
- Django gestiona el hash de las contraseñas.
- Las cuentas inactivas no pueden autenticarse.
- El panel cambia según el rol evaluado en el servidor.
- Las rutas de zonas y tareas vuelven a comprobar el rol en el servidor.
- Un participante recibe un error 403 aunque escriba directamente una URL administrativa.
- Zonas y responsables inactivos no pueden utilizarse en tareas nuevas.
- El cierre de sesión exige `POST` y token CSRF.
- Se habilitaron protección CSRF, `X-Frame-Options: DENY` y `nosniff`.
- Las cookies de sesión y CSRF están marcadas como `HttpOnly`.
- En producción se activan redirección HTTPS, cookies seguras y HSTS mediante variables de entorno.
- Cada cumplimiento se limita a la persona asignada y a una fecha programada única.
- Los secretos y bases locales están excluidos de Git; fuera de `DEBUG`, la clave secreta es obligatoria.

La configuración candidata superó `check --deploy` con `DEBUG=False`. El ambiente de alojamiento aún deberá suministrar la clave real, dominio, terminación HTTPS y credenciales de base de datos.

## 6. Persistencia y migraciones

El modelo `accounts.User` amplía `AbstractUser` e incorpora:

- correo electrónico único;
- rol `ADMIN` o `PARTICIPANT`;
- estado activo heredado de Django;
- reconocimiento de superusuarios como administradores funcionales.

La migración `accounts/0001_initial.py` crea el esquema de usuarios. Las migraciones de `chores` incorporan:

- `Zone`: nombre único, descripción, estado y fechas de control;
- `Chore`: nombre, descripción, zona, responsable, frecuencia, día ancla, próxima fecha, estado y autor del registro.
- `Completion`: tarea, responsable que la realizó, fecha programada única, fecha y hora y observación opcional.

Las relaciones con zona y responsable utilizan `PROTECT` para impedir eliminaciones que rompan la integridad. La interfaz aplica retiro o desactivación lógica mediante `is_active`.

Las tareas recurrentes avanzan su próxima fecha después de registrar un cumplimiento. Las mensuales conservan el día ancla incluso al pasar por febrero. La restricción `one_completion_per_occurrence` y la transacción impiden duplicar una misma ocurrencia. Las tareas únicas quedan fuera de pendientes una vez que tienen un registro, pero conservan su tarea y su cumplimiento para consulta histórica.

## 7. Pruebas automatizadas actuales

La suite de la versión 1.0.0 contiene treinta y ocho verificaciones. Doce cubren cuentas y panel:

| Grupo | Verificación |
|---|---|
| Modelo | Un usuario nuevo recibe el rol Participante |
| Modelo | El rol Administrador se reconoce correctamente |
| Modelo | Un superusuario recibe automáticamente el rol Administrador |
| Autenticación | Una cuenta inactiva no puede ingresar |
| Acceso | El panel redirige a quien no tiene sesión |
| Autorización | El participante no ve la administración |
| Autorización | El administrador sí ve su opción de gestión |
| Presentación | El superusuario se identifica visualmente como Administrador |
| Autenticación | Las credenciales válidas crean una sesión |
| Autenticación | Las credenciales inválidas muestran un mensaje genérico |
| Modelo | Un correo duplicado se rechaza |
| Ciclo de vida | La edición y desactivación conservan la identidad del usuario |

Diez verificaciones cubren la gestión administrativa:

| Grupo | Verificación |
|---|---|
| Modelo | Una tarea rechaza zonas inactivas |
| Formulario | Una tarea rechaza responsables inactivos |
| Acceso | Un visitante es enviado al inicio de sesión |
| Autorización | Un participante no abre la gestión de tareas |
| Autorización | Un participante no crea zonas mediante una solicitud directa |
| Interfaz | Los cuatro listados y formularios administrativos se renderizan |
| CRUD | El administrador crea una zona |
| CRUD | El administrador crea una tarea con autor y responsable |
| Retiro lógico | Una tarea solo se retira mediante `POST` |
| Integridad | Una zona con tareas activas no puede desactivarse |

Las ocho verificaciones adicionales cubren el flujo del participante:

| Grupo | Verificación |
|---|---|
| Consulta | El participante solo ve tareas activas asignadas a su cuenta |
| Acceso | Un visitante es enviado al inicio de sesión al consultar pendientes |
| Interfaz | El participante puede abrir el formulario de cumplimiento |
| Cumplimiento | Una tarea única crea un registro y sale de pendientes |
| Recurrencia | Una tarea semanal calcula su próxima fecha |
| Autorización | Un participante no puede completar la tarea de otra persona |
| Historial | El participante consulta únicamente sus propios cumplimientos |
| Historial | El administrador puede consultar el historial completo |

Ocho verificaciones finales cubren robustez, filtros y seguridad:

| Grupo | Verificación |
|---|---|
| Recurrencia | La frecuencia mensual conserva el día 31 después de febrero |
| Integridad | Un envío repetido no duplica la ocurrencia |
| Consulta | Los pendientes se filtran por zona y vencimiento |
| Historial | El administrador filtra el historial por zona |
| Recurrencia | La frecuencia diaria avanza un día |
| Recurrencia | El año bisiesto utiliza el 29 de febrero y recupera el día ancla |
| Autorización | El modelo rechaza un cumplimiento de otra persona |
| Seguridad | Una escritura sin token CSRF se rechaza |

Comandos de control:

```bash
python manage.py test
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py check --deploy
```

La validación del incremento 2.1 en Windows produjo **8 pruebas aprobadas, 0 fallidas**. El incremento 2.2 produjo **18 pruebas aprobadas, 0 fallidas** y fue comprobado manualmente en Windows. La versión candidata produjo **38 pruebas aprobadas, 0 fallidas**, sin problemas de sistema, despliegue ni migraciones sin registrar. Los resultados se conservan en las evidencias reales del plan de pruebas.

## 8. Limitaciones actuales

- Docker no pudo ejecutarse dentro del ambiente de edición actual; su configuración debe comprobarse en un equipo con Docker Desktop o Docker Engine.
- Las pruebas formales de usabilidad móvil, carga, estrés y restauración PostgreSQL requieren un ambiente especializado y permanecen registradas como condicionadas, no aprobadas.
- No existe un despliegue público.
