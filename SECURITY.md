# Política de seguridad

## Alcance actual

CleanIt se encuentra en desarrollo y dispone de un primer incremento ejecutable en `dev`. Todavía no existe una versión productiva ni una URL pública. Esta política se aplica desde la implementación y deberá revisarse antes de promover cambios a `main`.

## Reporte responsable

No se deben publicar credenciales, datos personales ni detalles explotables en una incidencia pública. Un reporte deberá enviarse inicialmente al responsable del repositorio y contener:

- componente afectado;
- descripción del riesgo;
- pasos de reproducción sin datos sensibles;
- impacto estimado;
- evidencia disponible;
- recomendación, si existe.

## Prioridades de respuesta

| Severidad | Ejemplo | Confirmación inicial | Objetivo de corrección |
|---|---|---:|---:|
| Crítica | Acceso total no autorizado o exposición de credenciales | 4 horas | 24 horas |
| Alta | Lectura o modificación indebida de tareas de otros usuarios | 1 día hábil | 3 días hábiles |
| Media | Validación incompleta sin exposición inmediata | 2 días hábiles | 10 días hábiles |
| Baja | Mejora preventiva o hallazgo de bajo impacto | 5 días hábiles | Siguiente versión planificada |

Los tiempos son objetivos del plan académico y deberán ajustarse a la capacidad real del equipo.

## Controles mínimos

- HTTPS en producción.
- `DEBUG=False` fuera del ambiente local.
- `SECRET_KEY` y credenciales fuera del repositorio.
- autorización por rol en cada operación sensible; iniciada en el incremento 2.1.
- protección CSRF y validación de formularios de Django; habilitadas en 2.1.
- contraseñas administradas por el sistema de autenticación de Django; implementado en 2.1.
- dependencias revisadas y actualizadas periódicamente.
- respaldos cifrados y restauraciones verificadas.
- registros sin contraseñas ni datos personales innecesarios.
