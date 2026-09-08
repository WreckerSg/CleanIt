# Estrategia de seguimiento y soporte tras la entrega

## 1. Objetivo y alcance

Mantener CleanIt disponible, seguro y verificable después de entregar el MVP. La estrategia cubre autenticación, cuentas, zonas, tareas, frecuencias, pendientes, cumplimiento, historial, datos y documentación.

Sus objetivos son:

- recibir y clasificar incidentes sin perder trazabilidad;
- resolver primero los problemas de mayor impacto;
- proteger credenciales y datos personales;
- comprobar respaldos y recuperación;
- actualizar código y dependencias sin introducir regresiones;
- convertir la retroalimentación en cambios priorizados.

## 2. Responsabilidades de soporte

| Nivel | Responsable | Funciones |
|---|---|---|
| L1 | Administrador funcional | Dudas de uso, revisión de cuentas, asignaciones y recopilación inicial |
| L2 | Calidad y soporte | Reproducir, clasificar, reunir evidencia segura y comprobar correcciones |
| L3 | Desarrollo y DevOps | Corregir código o datos, desplegar, restaurar y atender seguridad |
| Producto | Product Owner | Priorizar mejoras, aceptar riesgos y aprobar liberaciones |

Una persona puede asumir más de un nivel en un equipo pequeño, pero cada incidencia debe tener un responsable y una fecha de seguimiento.

## 3. Canales y registro mínimo

- Los defectos se registran en GitHub Issues mediante **Reporte de error**.
- Las mejoras se registran mediante **Solicitud de mejora**.
- Jira conserva prioridad, sprint y relación con la historia correspondiente.
- La documentación y las decisiones técnicas quedan versionadas en Git.
- Los secretos, respaldos y datos personales no se publican en incidencias.

Cada reporte debe contener versión o commit, ambiente, pasos para reproducir, resultado esperado, resultado observado, severidad, evidencia revisada y responsable.

## 4. Prioridad y tiempos objetivo

| Prioridad | Criterio | Confirmación inicial | Solución o plan |
|---|---|---:|---:|
| P1 crítica | Servicio inutilizable, pérdida de datos o riesgo grave de seguridad | 4 horas | 24 horas |
| P2 alta | Función esencial bloqueada o datos visibles para una cuenta incorrecta | 1 día hábil | 3 días hábiles |
| P3 media | Función degradada con alternativa temporal | 2 días hábiles | 10 días hábiles |
| P4 baja | Problema visual, documental o mejora | 5 días hábiles | Próxima versión |

Los tiempos son metas iniciales en horario hábil. Un incidente de seguridad exige contención inmediata antes de la corrección definitiva.

## 5. Flujo de atención

1. Registrar el reporte sin información sensible.
2. Verificar si puede reproducirse y solicitar datos seguros si falta información.
3. Asignar prioridad y responsable.
4. Aplicar contención cuando exista riesgo para disponibilidad, datos o seguridad.
5. Corregir desde `dev` con una clave de Jira.
6. Ejecutar pruebas relacionadas y regresión completa.
7. Promover en orden por `qa`, `pre-main` y `main`.
8. Confirmar el resultado con quien reportó y cerrar con versión de solución.

## 6. Mantenimiento y monitoreo

| Frecuencia | Actividad |
|---|---|
| Continua | Revisar disponibilidad, errores críticos y eventos de seguridad |
| Diaria | Confirmar el resultado del respaldo automático |
| Semanal | Clasificar incidencias, revisar errores repetidos y tareas vencidas |
| Mensual | Restaurar un respaldo aislado, revisar dependencias y cuentas activas |
| Trimestral | Revisar permisos, riesgos, rendimiento, documentación y retención |
| Por versión | Ejecutar 100 % de la suite, `check --deploy`, migraciones y actualización del manual |

Indicadores iniciales: disponibilidad, respuestas 5xx, tiempo de respuesta p95, respaldos correctos, restauraciones aprobadas, casos de prueba aprobados, defectos reabiertos y tareas vencidas.

## 7. Respaldo y continuidad

- Respaldo diario y retención inicial de siete copias diarias y cuatro semanales.
- Una copia debe permanecer fuera del servicio principal y con acceso restringido.
- Los respaldos con datos personales deben cifrarse.
- Debe ejecutarse una restauración mensual en un ambiente aislado.
- RPO inicial: 24 horas. RTO inicial: 4 horas.

Ante una falla grave se detienen escrituras si hay riesgo de corrupción, se identifica la última copia válida, se restaura de forma aislada, se comprueban usuarios, tareas y cumplimientos, y se documenta la autorización de retorno.

## 8. Seguridad y privacidad

- Desactivar cuentas que ya no pertenezcan al grupo.
- Mantener `DEBUG=False`, HTTPS, cookies seguras y secretos externos en producción.
- Revisar dependencias y aplicar correcciones críticas oportunamente.
- No compartir bases, logs o capturas sin revisar información personal.
- Rotar credenciales ante sospecha de exposición.
- Conservar únicamente los datos necesarios para la operación.

Los reportes de seguridad se gestionan según [`SECURITY.md`](../SECURITY.md).

## 9. Gestión de cambios y versiones

Cada cambio debe identificar necesidad, stakeholders, criterios de aceptación, impacto, esfuerzo, riesgos, pruebas y reversa. El Product Owner decide si se incorpora al backlog.

Se utiliza versionamiento semántico:

- `MAJOR`: cambios incompatibles;
- `MINOR`: funcionalidades compatibles;
- `PATCH`: correcciones compatibles.

Las liberaciones avanzan `dev → qa → pre-main → main` y actualizan pruebas, migraciones, manual, documentación técnica y `CHANGELOG.md`.

## 10. Primeros 90 días

- Días 1 a 30: estabilización, revisión diaria y correcciones bloqueantes.
- Días 31 a 60: análisis de uso, rendimiento y preguntas frecuentes.
- Días 61 a 90: retrospectiva, revisión de riesgos y priorización de la versión siguiente.

## 11. Criterio de cierre y transferencia

La entrega se considera transferida cuando existen acceso autorizado al repositorio, inventario técnico, instrucciones de instalación, variables requeridas sin secretos, respaldo y restauración documentados, manual vigente, incidencias y riesgos conocidos, responsables de soporte y aceptación registrada.
