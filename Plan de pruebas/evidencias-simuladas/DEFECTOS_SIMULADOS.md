# Registro de defectos simulados

Todos los hallazgos de este documento son ejemplos académicos.

## D-SIM-001 - Recurrencia mensual pierde el día ancla

| Campo | Valor simulado |
|---|---|
| Caso | PU-04 |
| Severidad | Media |
| Precondición | Tarea mensual con fecha ancla 31/01/2026 |
| Pasos | Calcular la siguiente fecha dos veces |
| Esperado | 28/02/2026 y luego 31/03/2026 |
| Observado | 28/02/2026 y luego 28/03/2026 |
| Corrección propuesta | Conservar el día ancla y usar el último día válido del mes |

## D-SIM-002 - Asignación a persona inactiva

| Campo | Valor simulado |
|---|---|
| Caso | PI-04 |
| Severidad | Alta |
| Precondición | `maria.inactiva` existe y una tarea está sin responsable |
| Pasos | Enviar manualmente el identificador inactivo en la solicitud |
| Esperado | Rechazo sin modificar la asignación |
| Observado | La asignación queda guardada |
| Corrección propuesta | Filtrar personas activas y validar nuevamente en el servidor |

## D-SIM-003 - Cumplimiento duplicado

| Campo | Valor simulado |
|---|---|
| Caso | PI-06 |
| Severidad | Alta |
| Precondición | Una ocurrencia pendiente para `ana.prueba` |
| Pasos | Enviar dos solicitudes de finalización casi simultáneas |
| Esperado | Un cumplimiento y un solo avance de fecha |
| Observado | Dos cumplimientos y doble avance |
| Corrección propuesta | Transacción, restricción de unicidad e idempotencia |

## D-SIM-004 - Desbordamiento móvil

| Campo | Valor simulado |
|---|---|
| Caso | PSN-03 |
| Severidad | Baja |
| Precondición | Historial con varias columnas a 360 px |
| Pasos | Abrir historial y completar el recorrido definido |
| Esperado | Contenido legible sin desplazar toda la página |
| Observado | La tabla supera el ancho de la ventana |
| Corrección propuesta | Contenedor responsivo y priorización de columnas |

## D-SIM-005 - Evidencia no especificada

| Campo | Valor simulado |
|---|---|
| Caso | PD-01 |
| Severidad | Media |
| Precondición | Revisión documental del modelo 1.0 |
| Pasos | Comprobar campos obligatorios de todos los casos |
| Esperado | Cada caso define evidencia requerida |
| Observado | Dos casos no especifican cómo comprobar el resultado |
| Corrección propuesta | Agregar el campo y revisar nuevamente los 30 casos |

