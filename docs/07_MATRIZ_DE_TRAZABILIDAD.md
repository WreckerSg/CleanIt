# Matriz de trazabilidad

## Historias de usuario

| Jira | Historia | Casos relacionados | Cobertura |
|---|---|---|---|
| SCRUM-15 | Como administrador, quiero registrar personas para poder asignarles tareas de limpieza. | CP-03, CP-04 | Flujo positivo, obligatoriedad, formato y duplicidad |
| SCRUM-16 | Como administrador, quiero editar o desactivar usuarios para mantener actualizada la lista de responsables. | CP-05, CP-06 | Edición, relaciones, desactivación, acceso e historial |
| SCRUM-17 | Como administrador, quiero crear tareas de limpieza para organizar las actividades que deben realizarse. | CP-07, CP-08 | Creación y validaciones del formulario/servidor |
| SCRUM-18 | Como administrador, quiero editar o eliminar tareas para corregir o retirar actividades de limpieza. | CP-09, CP-10 | Edición y baja lógica con preservación del historial |
| SCRUM-19 | Como administrador, quiero definir la frecuencia de una tarea para programar su realización periódica. | CP-11, CP-12, CP-13 | Única, diaria, semanal, mensual y fechas límite |
| SCRUM-20 | Como administrador, quiero asignar una tarea a una persona para establecer quién debe realizarla. | CP-14, CP-15 | Asignación válida y rechazo de persona inactiva |
| SCRUM-21 | Como usuario, quiero consultar mis tareas pendientes para saber qué actividades debo realizar. | CP-16, CP-17, CP-22 | Aislamiento, orden, vencimiento y uso móvil |
| SCRUM-22 | Como usuario, quiero marcar una tarea como completada para registrar que la actividad fue realizada. | CP-11, CP-18, CP-19 | Finalización, historial, recurrencia e idempotencia |
| SCRUM-23 | Como administrador, quiero consultar el estado y el historial de las tareas para supervisar su cumplimiento. | CP-20, CP-21, CP-24 | Filtros, trazabilidad e integridad tras restauración |

## Requisitos no funcionales y riesgos

| Requisito o riesgo | Verificación | Evidencia futura |
|---|---|---|
| Acceso no autorizado | CP-01, CP-02, CP-16, CP-23 | Salidas, capturas sin datos sensibles e incidencias |
| Frecuencia incorrecta | CP-11, CP-12, CP-13 | Pruebas unitarias y registro de fechas |
| Falta de actualización | CP-18, CP-19 | Historial y prueba de finalización |
| Baja adopción | CP-17, CP-22 y prueba de usabilidad | Tasa de éxito, tiempos y observaciones anónimas |
| Pérdida de información | CP-10, CP-21, CP-24 | Archivo de respaldo, log de restauración y conteos |
| Rendimiento para grupos pequeños | Escenario de carga del plan | Reporte original de la herramienta de carga |
| Interfaz adaptable | CP-22 | Matriz de dispositivos y capturas revisadas |

## Tareas técnicas de cierre

| Jira | Tarea | Documentos o casos que la soportan |
|---|---|---|
| SCRUM-33 | Pruebas de integración y usabilidad | Plan, CP-01 a CP-24 y evidencias por ciclo |
| SCRUM-34 | Correcciones, permisos y revisión de seguridad | CP-02, CP-15, CP-16, CP-19, CP-23 y `SECURITY.md` |
| SCRUM-35 | Despliegue, respaldo y elaboración del manual básico | CP-24, manual, documentación técnica y gestión postproyecto |
| SCRUM-36 | Validación con Product Owner y demostración final | Criterios de salida, checklist de aceptación y acta futura |

## Estado de trazabilidad

- Historias cubiertas por al menos un caso: **9 de 9 (100 % del diseño)**.
- Casos disenados: **24**.
- Casos ejecutados realmente: **0**, porque no existe una versión funcional.
- Evidencia disponible: simulación académica identificada en cada archivo.
