# Registro inicial y transferencia del MVP

## Inventario entregado

| Componente | Estado |
|---|---|
| Aplicación Django | Implementada |
| Usuarios y roles | Implementados |
| Zonas y tareas | Implementadas |
| Pendientes y vencimientos | Implementados |
| Cumplimiento y recurrencia | Implementados |
| Historial y filtros | Implementados |
| SQLite local | Implementado |
| PostgreSQL con Docker Compose | Configurado; requiere validación en un host con Docker |
| Pruebas automatizadas | Implementadas y aprobadas |
| Manual y documentación técnica | Actualizados |
| Integración continua | Configurada para las cuatro ramas |

## Responsabilidades iniciales

| Responsabilidad | Rol asignado |
|---|---|
| Priorización y aceptación | Product Owner |
| Coordinación del proceso | Scrum Master |
| Interfaz y experiencia | Frontend/UX |
| Código, datos y migraciones | Backend/Datos |
| Pruebas, repositorio y operación | QA/DevOps |

## Riesgos y limitaciones conocidos

- No existe un proveedor de alojamiento seleccionado ni una URL pública del sistema.
- La configuración PostgreSQL debe ejecutarse en un equipo con Docker antes de un despliegue real.
- No se implementan recuperación de contraseña por correo, notificaciones ni múltiples sedes.
- El respaldo automático depende de la plataforma de alojamiento futura.
- Las evidencias simuladas del Paso 1 se conservan como antecedente y están claramente rotuladas.

## Información para operación

- Código y documentación: repositorio GitHub de CleanIt.
- Gestión del trabajo: Jira y claves `SCRUM-*`.
- Configuración: `.env.example`, sin secretos reales.
- Instalación: `Documentación técnica y de usuario/03_Guia_de_instalacion_y_ejecucion.md`.
- Incidentes: plantillas dentro de `.github/ISSUE_TEMPLATE/`.
- Seguridad: `SECURITY.md`.
- Cambios: `CHANGELOG.md`.

## Aceptación

La plantilla `docs/09_PLANTILLA_ACTA_DE_ACEPTACION.md` debe completarse con la versión, commit, resultado de pruebas, riesgos aceptados y responsables antes de operar con datos reales.
