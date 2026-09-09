# Registro de cambios

Los cambios relevantes de CleanIt se documentan en este archivo.

## [1.0.1] - 2026-09-09

### Corregido

- La interfaz CSS se sirve correctamente al ejecutar Django con Gunicorn en Docker.
- El contenedor reúne los archivos estáticos antes de iniciar la aplicación.
- El puerto web externo puede configurarse con `WEB_PORT` y utiliza `8081` por defecto.

### Verificado

- Recorrido funcional desde un teléfono conectado por Wi-Fi.
- Ejecución integrada con PostgreSQL 16 mediante Docker Compose.
- Respaldo y restauración de PostgreSQL en una base aislada.

## [1.0.0] - 2026-09-08

### Agregado

- Aplicación ejecutable con Python 3.10 o superior y Django 5.2.17 LTS.
- Usuario personalizado con roles Administrador y Participante.
- Inicio y cierre de sesión, panel diferenciado y administración de cuentas.
- Configuración para SQLite local y PostgreSQL mediante Docker Compose.
- Ocho pruebas automatizadas de modelo, autenticación, acceso, autorización y presentación del rol.
- Carpeta del Paso 2 con manual, descripción técnica y guía de instalación.
- Gestión de zonas con creación, edición y desactivación controlada.
- Gestión de tareas con responsable, frecuencia, próxima fecha y retiro lógico.
- Consulta de tareas pendientes para cada responsable.
- Registro de cumplimiento con observación opcional e historial por rol.
- Cálculo de próxima fecha para frecuencias diarias, semanales y mensuales.
- Permisos de servidor para impedir el acceso administrativo de participantes.
- Dieciocho pruebas automatizadas aprobadas en el incremento 2.2.
- Veintiséis pruebas automatizadas aprobadas en el incremento 2.3.
- Filtros de zona, vencimiento, responsable y rango de fechas.
- Prevención de cumplimientos duplicados por tarea y fecha programada.
- Conservación del día ancla en recurrencias mensuales y años bisiestos.
- Configuración de seguridad para producción e integración continua en cuatro ramas.
- Treinta y ocho pruebas automatizadas aprobadas para la versión 1.0.0.

## [0.2.0] - 2026-09-07

### Agregado

- Plan de pruebas y 30 casos detallados.
- Matriz de trazabilidad con las historias SCRUM-15 a SCRUM-23.
- Dos ciclos de resultados simulados claramente identificados.
- Manual básico de usuario propuesto.
- Documentación técnica del stack Django, Bootstrap y PostgreSQL.
- Estrategia de gestión postproyecto.
- Plantillas para incidencias, solicitudes de cambio y pull requests.

### Aclarado

- El producto se encuentra en fase de planificación.
- No existen pruebas ejecutadas ni un despliegue funcional a la fecha.

## [0.1.0] - 2026-08-31

### Agregado

- Definición del proyecto, alcance, stakeholders y riesgos.
- Planificación Scrum de cuatro sprints.
- Backlog y roles en Jira.
- Selección del stack tecnológico.
