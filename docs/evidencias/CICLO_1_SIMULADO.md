# Evidencia simulada - Ciclo 1

**Naturaleza:** simulación académica, sin ejecución real.  
**Versión hipotética:** `0.3.0-rc1-simulada`.  
**Casos considerados:** CP-01 a CP-24.  

## Resumen

- 20 casos aprobados.
- 4 casos fallidos.
- 0 casos bloqueados.
- Tasa simulada de aprobación: 83.3 %.

## Registro de fallos

### D-SIM-001 - Recurrencia mensual pierde el día ancla

- **Caso:** CP-13.
- **Esperado:** 31 de enero -> 28 de febrero -> 31 de marzo en un año no bisiesto.
- **Observado simulado:** 31 de enero -> 28 de febrero -> 28 de marzo.
- **Severidad:** media.
- **Estado hipotético:** corregir antes de liberar.

### D-SIM-002 - Asignación a usuario inactivo

- **Caso:** CP-15.
- **Esperado:** el usuario inactivo no aparece y el servidor rechaza su identificador.
- **Observado simulado:** `maria.inactiva` aparece en el selector y puede recibir la tarea.
- **Severidad:** alta.
- **Estado hipotético:** bloquea la liberación.

### D-SIM-003 - Cumplimiento duplicado

- **Caso:** CP-19.
- **Esperado:** una sola finalización por ocurrencia.
- **Observado simulado:** un doble clic genera dos filas de historial con segundos de diferencia.
- **Severidad:** alta.
- **Estado hipotético:** bloquea la liberación.

### D-SIM-004 - Desbordamiento en pantalla móvil

- **Caso:** CP-22.
- **Esperado:** contenido legible a 360 px sin desplazar toda la página.
- **Observado simulado:** la tabla de historial supera el ancho de la pantalla.
- **Severidad:** baja.
- **Estado hipotético:** corregir en la versión candidata.

## Decisión simulada

**No liberar.** El resultado no cumple el umbral del 95 % y mantiene dos defectos de severidad alta.

