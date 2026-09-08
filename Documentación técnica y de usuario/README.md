# Paso 2. Documentación técnica y de usuario

Esta carpeta reúne los dos entregables solicitados en el Paso 2 y se actualiza junto con cada incremento funcional de CleanIt.

## Contenido

| Archivo | Propósito |
|---|---|
| [`01_Manual_basico_de_usuario.md`](01_Manual_basico_de_usuario.md) | Explica las funciones disponibles y el procedimiento para utilizarlas |
| [`02_Descripcion_y_justificacion_tecnica.md`](02_Descripcion_y_justificacion_tecnica.md) | Describe la arquitectura, las tecnologías y la justificación de cada decisión |
| [`03_Guia_de_instalacion_y_ejecucion.md`](03_Guia_de_instalacion_y_ejecucion.md) | Permite instalar, comprobar y ejecutar el sistema en un equipo local |
| [`04_Registro_de_validacion.md`](04_Registro_de_validacion.md) | Conserva los resultados reales por versión y ambiente |

## Estado del Paso 2

| Incremento | Contenido | Estado |
|---|---|---|
| 2.1 | Base Django, autenticación, roles, panel inicial y administración de cuentas | Validado localmente: 8/8 pruebas y recorridos por rol aprobados |
| 2.2 | Gestión de personas, zonas y tareas | Implementado en `dev`; pendiente de validación en Windows |
| 2.3 | Asignaciones, frecuencias y consulta de pendientes | Pendiente |
| 2.4 | Cumplimiento, historial y evidencias visuales del manual | Pendiente |

La documentación solo identifica como operativas las funciones comprobadas en el código. Los apartados futuros se incorporarán a medida que pasen por `dev`, `qa`, `pre-main` y `main`.

## Criterio de cierre

El Paso 2 quedará listo cuando:

- el manual cubra todos los flujos del producto mínimo viable;
- la descripción técnica coincida con el código y las dependencias versionadas;
- los comandos de instalación y prueba puedan repetirse desde un clon limpio;
- las capturas y evidencias correspondan a la aplicación real;
- el contenido haya sido revisado en `qa` y aceptado antes de llegar a `main`.
