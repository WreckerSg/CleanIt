# Resultados simulados de las pruebas

> [!WARNING]
> **SIMULACIÓN ACADÉMICA.** CleanIt no tiene una versión ejecutable. Las cifras, tiempos, defectos y salidas de este documento fueron construidos para demostrar el procedimiento de registro esperado. No corresponden a mediciones reales.

## 1. Objetivo de la simulación

Representar dos ciclos hipotéticos de ejecución: un primer ciclo que descubre defectos y un segundo ciclo posterior a las correcciones. El ejemplo permite evidenciar la relación entre caso, hallazgo, corrección y regresión.

## 2. Identificación del escenario

| Campo | Valor simulado |
|---|---|
| Versión evaluada | `0.3.0-rc1-simulada` |
| Ambiente | `qa-simulado` |
| Navegador principal | Chrome, resoluciones de escritorio y móvil |
| Base de datos | PostgreSQL con datos ficticios |
| Ejecutores | Rol Calidad y DevOps |
| Casos previstos | 24 |

## 3. Ciclo 1 simulado

| Estado | Cantidad | Porcentaje |
|---|---:|---:|
| Aprobado | 20 | 83.3 % |
| Fallido | 4 | 16.7 % |
| Bloqueado | 0 | 0.0 % |
| No ejecutado | 0 | 0.0 % |
| **Total** | **24** | **100 %** |

El ciclo no cumpliría el criterio de salida porque el porcentaje aprobado sería inferior al 95 % y permanecerían defectos de severidad alta y media.

### Hallazgos simulados

| Defecto | Caso | Severidad | Resultado observado simulado | Tratamiento propuesto |
|---|---|---|---|---|
| D-SIM-001 | CP-13 | Media | Una tarea mensual creada el 31 de enero queda programada para el 28 de marzo después de pasar por febrero | Conservar el día ancla y utilizar el último día válido de cada mes |
| D-SIM-002 | CP-15 | Alta | El selector permite asignar tareas a una persona inactiva | Filtrar usuarios activos en formulario y validar nuevamente en el servidor |
| D-SIM-003 | CP-19 | Alta | Un doble clic rápido crea dos registros de cumplimiento | Ejecutar la operación en transacción, usar restricción de unicidad e inhabilitar el botón al enviar |
| D-SIM-004 | CP-22 | Baja | La tabla de historial desborda horizontalmente a 360 px | Aplicar contenedor responsivo y adaptar columnas secundarias |

## 4. Cambios hipotéticos antes del ciclo 2

- Servicio de recurrencia actualizado para preservar el día de referencia mensual.
- Consulta de responsables limitada a usuarios activos y validación en `clean()`.
- Registro de finalización protegido contra solicitudes duplicadas.
- Vista de historial ajustada con componentes responsivos de Bootstrap.
- Pruebas unitarias agregadas para cada defecto.

Estos cambios son parte de la simulación; no representan commits existentes.

## 5. Ciclo 2 simulado

Se reejecutarian los cuatro casos fallidos y seis casos críticos de regresión. En el escenario simulado los diez finalizan satisfactoriamente.

| Grupo | Casos | Aprobados | Fallidos |
|---|---:|---:|---:|
| Reprueba de defectos | 4 | 4 | 0 |
| Regresión seleccionada | 6 | 6 | 0 |
| **Ejecución del ciclo 2** | **10** | **10** | **0** |

Estado consolidado simulado de la versión:

| Estado | Cantidad | Porcentaje |
|---|---:|---:|
| Aprobado | 24 | 100 % |
| Fallido | 0 | 0 % |
| Bloqueado | 0 | 0 % |
| **Total aplicable** | **24** | **100 %** |

## 6. Simulación de rendimiento

Perfil propuesto: 50 usuarios virtuales durante 10 minutos, crecimiento gradual de 5 usuarios por minuto y una base con 1,000 tareas y 5,000 registros de historial.

| Operación | Objetivo p95 | Resultado simulado | Estado simulado |
|---|---:|---:|---|
| Consultar pendientes | <= 2.0 s | 1.20 s | Aprobado |
| Crear y asignar tarea | <= 2.0 s | 1.48 s | Aprobado |
| Marcar como completada | <= 2.0 s | 1.35 s | Aprobado |
| Consultar historial | <= 2.0 s | 1.74 s | Aprobado |

- Tasa de error simulada: 0.3 %.
- Disponibilidad durante el escenario simulado: 100 %.
- Conclusión hipotética: el sistema cumpliría el objetivo para grupos pequeños, pero las cifras deben reemplazarse por mediciones reales.

## 7. Simulación de usabilidad

Escenario propuesto con cinco participantes representativos y cuatro tareas: iniciar sesión, localizar una tarea, marcarla como completada y consultar su historial.

| Indicador | Meta | Resultado simulado |
|---|---:|---:|
| Flujos completados sin ayuda | >= 85 % | 95 % (19 de 20) |
| Tiempo promedio del recorrido | <= 3 min | 2 min 10 s |
| Valoración de claridad | >= 4/5 | 4.3/5 |

Observación simulada: una persona no identificó inicialmente el filtro de historial. La mejora propuesta es aumentar el contraste del botón y agregar una etiqueta explícita.

## 8. Simulación de seguridad y recuperación

| Control | Resultado simulado |
|---|---|
| Páginas privadas rechazan sesiones anónimas | Aprobado |
| Participante no accede a administración de personas | Aprobado |
| Participante no modifica tareas de otro usuario | Aprobado |
| Formularios rechazan solicitud sin token CSRF | Aprobado |
| Clave secreta y contraseña de base de datos no están en Git | Aprobado |
| Respaldo se restaura y conserva conteos de registros | Aprobado |

## 9. Conclusión de la simulación

El ejemplo muestra que una versión con 20 de 24 casos aprobados no debería liberarse. Después de corregir y reprobar los cuatro hallazgos, el escenario consolidado alcanzaría los criterios definidos. La conclusión no autoriza un despliegue real: primero debe implementarse el MVP y sustituirse toda esta evidencia por resultados reproducibles.

Los registros narrativos de cada ciclo están disponibles en [`docs/evidencias/`](evidencias/README.md).
