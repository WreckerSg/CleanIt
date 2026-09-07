# Política de seguridad

## Alcance actual

CleanIt está en fase de planificación y no tiene una versión ejecutable. Esta política define el procedimiento que se aplicará desde el inicio de la implementación.

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

## Controles minimos propuestos

- HTTPS en producción.
- `DEBUG=False` fuera del ambiente local.
- `SECRET_KEY` y credenciales fuera del repositorio.
- autorización por rol en cada operación sensible.
- protección CSRF y validación de formularios de Django.
- contraseñas administradas por el sistema de autenticación de Django.
- dependencias revisadas y actualizadas periódicamente.
- respaldos cifrados y restauraciones verificadas.
- registros sin contraseñas ni datos personales innecesarios.
