# Evidencia simulada - Ciclo 1

## Identificación

| Campo | Valor hipotético |
|---|---|
| Naturaleza | Simulación académica sin ejecución real |
| Versión | `0.3.0-rc1-simulada` |
| Rama | `qa` |
| Ambiente | `qa-simulado` |
| Casos considerados | PU-01 a PD-02 (30 casos) |

## Resumen

| Estado | Cantidad | Porcentaje |
|---|---:|---:|
| Aprobado | 25 | 83,3 % |
| Fallido | 5 | 16,7 % |
| Bloqueado | 0 | 0,0 % |
| **Total** | **30** | **100 %** |

La versión hipotética no podría pasar a `pre-main`: su tasa de aprobación es inferior al 95 % y conserva defectos altos.

## Matriz de resultados simulados

| Grupo | Casos | Aprobados | Fallidos |
|---|---:|---:|---:|
| Unitarias | 5 | 4 | 1 |
| Integración | 6 | 4 | 2 |
| Sistema funcional | 11 | 11 | 0 |
| Sistema no funcional | 6 | 5 | 1 |
| Documentales | 2 | 1 | 1 |
| **Total** | **30** | **25** | **5** |

## Fallos simulados

| Defecto | Caso | Severidad | Observación simulada |
|---|---|---|---|
| D-SIM-001 | PU-04 | Media | La recurrencia mensual pierde el día ancla después de febrero |
| D-SIM-002 | PI-04 | Alta | Una solicitud manipulada permite asignar una tarea a una persona inactiva |
| D-SIM-003 | PI-06 | Alta | Dos solicitudes simultáneas crean dos registros de cumplimiento |
| D-SIM-004 | PSN-03 | Baja | El historial desborda horizontalmente en una vista de 360 px |
| D-SIM-005 | PD-01 | Media | Dos casos no indicaban inicialmente la evidencia requerida |

## Decisión simulada

**No promover a `pre-main`.** Los defectos D-SIM-002 y D-SIM-003 bloquean la promoción por su severidad alta. Los cinco hallazgos deben corregirse en `dev`, integrarse nuevamente en `qa` y someterse a reprueba y regresión.

