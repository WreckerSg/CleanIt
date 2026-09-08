# Acta de aceptación de versión

## Identificación

| Campo | Información |
|---|---|
| Proyecto | CleanIt |
| Versión o etiqueta | 1.0.0 |
| Commit | Versión estable de la rama `main` |
| Fecha | 8 de septiembre de 2026 |
| Ambiente | Django 5.2.17, Python 3.10 o superior y SQLite de pruebas |
| Product Owner | Responsable del proyecto académico |
| Responsable técnico | Rol Backend/Datos y QA/DevOps |

## Alcance evaluado

Historias, defectos y cambios incluidos:

- SCRUM-15 a SCRUM-23: usuarios, tareas y seguimiento.
- SCRUM-33: plan y ejecución de pruebas.
- SCRUM-34 a SCRUM-36: seguridad, documentación, entrega y soporte.

## Resultado de pruebas

| Indicador | Resultado |
|---|---:|
| Casos aplicables | 26 |
| Aprobados | 26 |
| Fallidos | 0 |
| Condicionados por ambiente | 4 |
| Verificaciones automatizadas | 38 de 38 aprobadas |
| Defectos críticos abiertos | 0 |
| Defectos altos abiertos | 0 |
| Restauración PostgreSQL verificada | No; requiere host con Docker |

Enlace al informe y evidencias: [`Plan de pruebas/evidencias-reales/`](../Plan%20de%20pruebas/evidencias-reales/README.md).

## Riesgos u observaciones aceptados

- No existe despliegue público ni proveedor de alojamiento seleccionado.
- Usabilidad móvil formal, carga, estrés y restauración PostgreSQL deberán ejecutarse antes de operar con datos reales.

## Decisión

- [ ] Aprobada para despliegue.
- [x] Aprobada con condiciones documentadas para versión estable del repositorio.
- [ ] Rechazada; requiere correcciones y nueva revisión.

Justificación: el MVP funcional, la documentación y los controles automatizados cumplen el alcance académico. La aprobación no autoriza aún un despliegue con datos reales.

## Aprobaciones

| Rol | Nombre | Aprobación/fecha |
|---|---|---|
| Product Owner | Responsable del proyecto | Aprobación académica registrada el 08/09/2026 |
| Calidad | Rol QA/DevOps | 38 verificaciones aprobadas el 08/09/2026 |
| Responsable técnico | Rol Backend/Datos | Configuración y migraciones verificadas el 08/09/2026 |
