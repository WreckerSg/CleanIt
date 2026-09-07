# Evidencia simulada - Ciclo 2

**Naturaleza:** simulación académica, sin ejecución real.  
**Versión hipotética:** `0.3.0-rc2-simulada`.  
**Alcance:** reprueba de cuatro defectos y seis casos de regresión.  

## Reprueba

| Defecto | Caso | Resultado simulado |
|---|---|---|
| D-SIM-001 | CP-13 | Aprobado: se conserva el día mensual de referencia |
| D-SIM-002 | CP-15 | Aprobado: usuarios inactivos no se listan ni pueden enviarse manualmente |
| D-SIM-003 | CP-19 | Aprobado: una solicitud repetida no duplica el historial |
| D-SIM-004 | CP-22 | Aprobado: el historial se adapta a 360 px |

## Regresión seleccionada

| Caso | Motivo | Resultado simulado |
|---|---|---|
| CP-06 | Verificar desactivación después del cambio de responsables | Aprobado |
| CP-12 | Verificar recurrencia diaria | Aprobado |
| CP-14 | Confirmar asignación normal a usuario activo | Aprobado |
| CP-18 | Confirmar finalización e historial | Aprobado |
| CP-20 | Confirmar consulta del historial | Aprobado |
| CP-23 | Confirmar que los permisos no cambiaron | Aprobado |

## Decisión simulada

El escenario consolidado quedaría con 24 de 24 casos aprobados y sin defectos altos o críticos abiertos. Sería una versión candidata para aceptación, condicionada a respaldo, revisión del Product Owner y evidencia real.

