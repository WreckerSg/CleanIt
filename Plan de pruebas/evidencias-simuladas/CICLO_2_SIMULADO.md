# Evidencia simulada - Ciclo 2

## Identificación

| Campo | Valor hipotético |
|---|---|
| Naturaleza | Simulación académica sin ejecución real |
| Versión | `0.3.0-rc2-simulada` |
| Rama | `qa` |
| Alcance | Reprueba de cinco defectos y regresión de siete casos |

## Reprueba simulada

| Defecto | Caso | Resultado simulado |
|---|---|---|
| D-SIM-001 | PU-04 | Aprobado: conserva el día ancla mensual |
| D-SIM-002 | PI-04 | Aprobado: el servidor rechaza personas inactivas |
| D-SIM-003 | PI-06 | Aprobado: una repetición no duplica el historial |
| D-SIM-004 | PSN-03 | Aprobado: la vista funciona a 360 px |
| D-SIM-005 | PD-01 | Aprobado: todos los casos indican evidencia requerida |

## Regresión simulada

| Caso | Motivo | Resultado simulado |
|---|---|---|
| PU-03 | Verificar que la corrección mensual no afecte recurrencias diaria y semanal | Aprobado |
| PI-02 | Comprobar que el filtro de usuarios no afecte su administración | Aprobado |
| PI-05 | Confirmar finalización normal y siguiente fecha | Aprobado |
| PSF-05 | Confirmar desactivación y conservación de relaciones | Aprobado |
| PSF-09 | Confirmar asignación normal a persona activa | Aprobado |
| PSF-11 | Confirmar finalización e historial | Aprobado |
| PSN-01 | Confirmar que los permisos no cambiaron | Aprobado |

## Consolidado hipotético

| Estado | Cantidad | Porcentaje |
|---|---:|---:|
| Aprobado | 30 | 100 % |
| Fallido | 0 | 0 % |
| Bloqueado | 0 | 0 % |
| **Total aplicable** | **30** | **100 %** |

## Decisión simulada

El incremento podría considerarse candidato para `pre-main`, condicionado a ejecutar allí la regresión completa, seguridad, rendimiento, recuperación y aceptación. Esta decisión no representa una promoción real ni una comprobación de CleanIt.

