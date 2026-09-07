# Casos de prueba detallados

## Convenciones

- **Estado actual:** diseñado, pendiente de ejecución real.
- **Prioridad alta:** flujo esencial, seguridad o integridad de datos.
- **Prioridad media:** comportamiento importante con alternativa temporal.
- **Resultado:** solo se asignará durante una ejecución. Los estados de `03_RESULTADOS_SIMULADOS.md` son ejemplos académicos.

## Resumen de cobertura

| ID | Título | Requisito | Tipo | Prioridad |
|---|---|---|---|---|
| CP-01 | Inicio de sesión válido | Acceso | Integración/seguridad | Alta |
| CP-02 | Rechazo de credenciales inválidas | Acceso | Seguridad | Alta |
| CP-03 | Registrar una persona válida | SCRUM-15 | Funcional | Alta |
| CP-04 | Validar persona duplicada o incompleta | SCRUM-15 | Funcional/negativa | Alta |
| CP-05 | Editar una persona | SCRUM-16 | Funcional | Media |
| CP-06 | Desactivar una persona con asignaciones | SCRUM-16 | Integración | Alta |
| CP-07 | Crear una tarea válida | SCRUM-17 | Funcional | Alta |
| CP-08 | Validar campos de una tarea | SCRUM-17 | Funcional/negativa | Alta |
| CP-09 | Editar una tarea pendiente | SCRUM-18 | Funcional | Media |
| CP-10 | Retirar una tarea conservando historial | SCRUM-18 | Integración | Alta |
| CP-11 | Finalizar una tarea única | SCRUM-19, SCRUM-22 | Integración | Alta |
| CP-12 | Calcular recurrencia diaria y semanal | SCRUM-19 | Unitaria/integración | Alta |
| CP-13 | Calcular recurrencia mensual en fechas límite | SCRUM-19 | Unitaria/límites | Alta |
| CP-14 | Asignar una tarea a persona activa | SCRUM-20 | Funcional | Alta |
| CP-15 | Rechazar asignación a persona inactiva | SCRUM-20 | Seguridad de negocio | Alta |
| CP-16 | Mostrar solo los pendientes del usuario | SCRUM-21 | Seguridad/funcional | Alta |
| CP-17 | Ordenar pendientes y destacar vencidos | SCRUM-21 | Funcional | Media |
| CP-18 | Marcar una tarea como completada | SCRUM-22 | Integración | Alta |
| CP-19 | Evitar una finalización duplicada | SCRUM-22 | Concurrencia/integridad | Alta |
| CP-20 | Consultar y filtrar el historial | SCRUM-23 | Funcional | Alta |
| CP-21 | Conservar integridad del historial al cambiar datos | SCRUM-23 | Integración | Alta |
| CP-22 | Usar los flujos principales desde móvil | RNF usabilidad | Usabilidad | Media |
| CP-23 | Aplicar permisos por rol | RNF seguridad | Seguridad | Alta |
| CP-24 | Respaldar y restaurar la base de datos | RNF continuidad | Recuperación | Alta |

---

## CP-01 - Inicio de sesión válido

| Campo | Detalle |
|---|---|
| Objetivo | Confirmar que una cuenta activa pueda iniciar sesión y sea dirigida a su vista autorizada. |
| Precondiciones | Aplicación disponible; usuarios `admin.cleanit` y `ana.prueba` activos. |
| Datos | Credenciales válidas almacenadas mediante el sistema de autenticación de Django. |

**Pasos**

1. Abrir la página de acceso.
2. Escribir el usuario y la contraseña válidos.
3. Seleccionar **Iniciar sesión**.
4. Repetir con una cuenta administradora y una participante.

**Resultado esperado:** la sesión se crea, la contraseña no se muestra ni aparece en la URL, cada persona llega a su página inicial y solo visualiza las opciones permitidas para su rol.

## CP-02 - Rechazo de credenciales inválidas

| Campo | Detalle |
|---|---|
| Objetivo | Evitar el acceso con contraseña incorrecta, cuenta inexistente o inactiva. |
| Precondiciones | Existe `maria.inactiva` y se conoce un usuario activo. |
| Datos | Contraseña incorrecta, usuario inexistente y cuenta inactiva. |

**Pasos**

1. Enviar cada combinación inválida desde el formulario de acceso.
2. Observar el mensaje y la URL resultante.
3. Intentar abrir directamente una página privada.

**Resultado esperado:** no se crea una sesión, se muestra un mensaje genérico que no revela si la cuenta existe y la página privada redirige al acceso. El intento queda disponible para monitoreo sin registrar la contraseña.

## CP-03 - Registrar una persona válida

| Campo | Detalle |
|---|---|
| Objetivo | Verificar la historia SCRUM-15 para datos válidos. |
| Precondiciones | Sesión de administrador; correo no registrado. |
| Datos | Nombre `Ana Prueba`, correo `ana.prueba@example.test`, rol participante. |

**Pasos**

1. Entrar en **Personas** y seleccionar **Nueva persona**.
2. Completar los campos obligatorios.
3. Guardar el formulario.
4. Buscar el registro en la lista.

**Resultado esperado:** se crea un único registro activo, aparece un mensaje de confirmación y la persona queda disponible para recibir tareas. La contraseña inicial, si se genera, no se almacena ni muestra en texto plano.

## CP-04 - Validar persona duplicada o incompleta

| Campo | Detalle |
|---|---|
| Objetivo | Comprobar reglas negativas de SCRUM-15. |
| Precondiciones | Existe `ana.prueba@example.test`; sesión de administrador. |
| Datos | Correo repetido, nombre vacío y correo con formato inválido. |

**Pasos**

1. Intentar registrar una persona con el correo ya existente.
2. Repetir dejando vacío un campo obligatorio.
3. Repetir con un correo mal formado.
4. Consultar la cantidad de personas después de cada intento.

**Resultado esperado:** cada envio inválido se rechaza con un mensaje asociado al campo; no se crean registros parciales ni duplicados y los valores no sensibles permanecen en el formulario para corregirlos.

## CP-05 - Editar una persona

| Campo | Detalle |
|---|---|
| Objetivo | Verificar que un administrador actualice datos permitidos sin perder relaciones. |
| Precondiciones | `ana.prueba` activa y con al menos una tarea asignada. |
| Datos | Cambiar nombre visible a `Ana P. Prueba`. |

**Pasos**

1. Abrir el detalle de la persona.
2. Seleccionar **Editar**.
3. Modificar el nombre y guardar.
4. Abrir la tarea previamente asignada.

**Resultado esperado:** el nombre se actualiza, la asignación conserva el mismo identificador de usuario y el cambio no crea una cuenta nueva ni modifica el historial anterior.

## CP-06 - Desactivar una persona con asignaciones

| Campo | Detalle |
|---|---|
| Objetivo | Validar la desactivación definida en SCRUM-16 y evitar pérdida de trazabilidad. |
| Precondiciones | Persona activa con una tarea pendiente y un cumplimiento histórico. |
| Datos | Usuario `ana.prueba`. |

**Pasos**

1. Desactivar la persona desde administración.
2. Intentar iniciar sesión con esa cuenta.
3. Abrir la asignación pendiente como administrador.
4. Consultar un registro histórico de la persona.

**Resultado esperado:** la cuenta no puede iniciar sesión ni recibir nuevas asignaciones; el sistema advierte sobre la tarea pendiente para permitir su reasignación; el historial conserva la identidad de quien completó actividades anteriores.

## CP-07 - Crear una tarea válida

| Campo | Detalle |
|---|---|
| Objetivo | Verificar el flujo positivo de SCRUM-17. |
| Precondiciones | Administrador autenticado y zona `Cocina` disponible. |
| Datos | `Trapear cocina`, descripción breve, zona Cocina, fecha futura. |

**Pasos**

1. Abrir **Tareas** y seleccionar **Nueva tarea**.
2. Completar nombre, descripción, zona, fecha y frecuencia.
3. Guardar.
4. Consultar el listado y el detalle.

**Resultado esperado:** se crea una sola tarea activa con los datos suministrados, se registra quién la creó y puede asignarse posteriormente.

## CP-08 - Validar campos de una tarea

| Campo | Detalle |
|---|---|
| Objetivo | Impedir tareas incompletas o con valores no permitidos. |
| Precondiciones | Administrador autenticado. |
| Datos | Nombre vacío, nombre por encima del límite, frecuencia no permitida y fecha inválida. |

**Pasos**

1. Enviar el formulario con cada valor inválido.
2. Intentar alterar manualmente la frecuencia enviada.
3. Consultar la lista de tareas.

**Resultado esperado:** Django valida tanto en el formulario como en el servidor; se explica el campo por corregir, no se guarda información parcial y un valor manipulado fuera del catálogo también se rechaza.

## CP-09 - Editar una tarea pendiente

| Campo | Detalle |
|---|---|
| Objetivo | Confirmar la edición de SCRUM-18. |
| Precondiciones | Tarea pendiente sin cumplimiento registrado. |
| Datos | Cambiar descripción, zona y próxima fecha. |

**Pasos**

1. Abrir el detalle de la tarea.
2. Seleccionar **Editar**.
3. Cambiar los datos permitidos y guardar.
4. Consultar la vista pendiente del responsable.

**Resultado esperado:** los cambios aparecen en el detalle y en la vista del responsable; el identificador se conserva y la modificación no crea un cumplimiento ni duplica la tarea.

## CP-10 - Retirar una tarea conservando historial

| Campo | Detalle |
|---|---|
| Objetivo | Validar que retirar una tarea no destruya la evidencia de cumplimiento. |
| Precondiciones | Tarea con al menos un registro histórico. |
| Datos | Tarea `Sacar basura`. |

**Pasos**

1. Seleccionar la opción de retirar o desactivar la tarea.
2. Confirmar la acción.
3. Consultar las tareas activas.
4. Consultar el historial administrativo.

**Resultado esperado:** la tarea deja de generar pendientes y no aparece entre las activas, pero sus cumplimientos anteriores permanecen consultables. Se prefiere baja lógica frente a eliminación física cuando exista historial.

## CP-11 - Finalizar una tarea única

| Campo | Detalle |
|---|---|
| Objetivo | Verificar el comportamiento final de una actividad sin recurrencia. |
| Precondiciones | Tarea única asignada y pendiente. |
| Datos | `Barrer sala`, frecuencia única. |

**Pasos**

1. Iniciar sesión como responsable.
2. Marcar la tarea como completada.
3. Volver a cargar la lista de pendientes.
4. Consultar el historial.

**Resultado esperado:** se crea un registro de cumplimiento, la tarea sale de pendientes y no genera una siguiente fecha. El historial muestra tarea, responsable y marca temporal.

## CP-12 - Calcular recurrencia diaria y semanal

| Campo | Detalle |
|---|---|
| Objetivo | Verificar el cálculo regular de SCRUM-19. |
| Precondiciones | Tareas diaria y semanal asignadas. |
| Datos | Diaria con vencimiento 2026-09-07; semanal con vencimiento 2026-09-07. |

**Pasos**

1. Completar la tarea diaria.
2. Verificar su nueva fecha.
3. Completar la tarea semanal.
4. Verificar su nueva fecha.

**Resultado esperado:** la diaria queda para 2026-09-08 y la semanal para 2026-09-14. Cada finalización crea un registro histórico y una sola ocurrencia futura.

## CP-13 - Calcular recurrencia mensual en fechas límite

| Campo | Detalle |
|---|---|
| Objetivo | Comprobar meses de distinta duración y años bisiestos. |
| Precondiciones | Servicio de recurrencia disponible; tarea mensual con día ancla. |
| Datos | 31 de enero de 2026, 31 de enero de 2028 y 30 de noviembre de 2026. |

**Pasos**

1. Calcular la fecha siguiente desde cada dato.
2. Calcular una segunda recurrencia después de pasar por febrero.
3. Comparar con el día ancla original.

**Resultado esperado:** 31/01/2026 -> 28/02/2026 -> 31/03/2026; 31/01/2028 -> 29/02/2028 -> 31/03/2028; 30/11/2026 -> 30/12/2026. Cuando el día no exista se usa el último del mes sin perder el ancla para meses posteriores.

## CP-14 - Asignar una tarea a persona activa

| Campo | Detalle |
|---|---|
| Objetivo | Verificar el flujo positivo de SCRUM-20. |
| Precondiciones | Tarea activa sin responsable; `ana.prueba` activa. |
| Datos | Tarea `Limpiar baño`, responsable `ana.prueba`. |

**Pasos**

1. Abrir la tarea como administrador.
2. Seleccionar **Asignar responsable**.
3. Elegir la persona activa y guardar.
4. Iniciar sesión como la persona elegida.

**Resultado esperado:** la asignación aparece en el detalle y la tarea se muestra entre los pendientes de `ana.prueba`, sin aparecer en la lista personal de otro participante.

## CP-15 - Rechazar asignación a persona inactiva

| Campo | Detalle |
|---|---|
| Objetivo | Evitar responsables que no puedan ingresar al sistema. |
| Precondiciones | Existe `maria.inactiva`; administrador autenticado. |
| Datos | Identificador de la persona inactiva enviado desde interfaz y mediante solicitud manipulada. |

**Pasos**

1. Abrir el selector de responsables.
2. Comprobar si aparece la persona inactiva.
3. Enviar manualmente su identificador al servidor.
4. Consultar la tarea y las asignaciones.

**Resultado esperado:** la persona inactiva no se ofrece en la interfaz y el servidor también rechaza la solicitud manipulada. La tarea conserva su responsable anterior o permanece sin asignar.

## CP-16 - Mostrar solo los pendientes del usuario

| Campo | Detalle |
|---|---|
| Objetivo | Validar la funcionalidad y el aislamiento requeridos por SCRUM-21. |
| Precondiciones | Ana y Luis tienen tareas diferentes; ambas cuentas activas. |
| Datos | Dos tareas de Ana, una de Luis y una tarea sin asignar. |

**Pasos**

1. Iniciar sesión como `ana.prueba` y abrir **Mis pendientes**.
2. Registrar los identificadores visibles.
3. Repetir como `luis.prueba`.
4. Intentar consultar por URL el detalle de una tarea ajena.

**Resultado esperado:** cada participante observa solo sus pendientes; las tareas sin asignar no aparecen; una URL ajena devuelve acceso denegado o recurso no encontrado sin revelar sus datos.

## CP-17 - Ordenar pendientes y destacar vencidos

| Campo | Detalle |
|---|---|
| Objetivo | Facilitar que el usuario identifique que debe realizar primero. |
| Precondiciones | Usuario con tareas vencida, actual y futura. |
| Datos | Fechas anterior, igual y posterior al día de prueba. |

**Pasos**

1. Abrir **Mis pendientes**.
2. Revisar el orden de las tareas.
3. Aplicar los filtros de estado disponibles.
4. Verificar el tratamiento visual de la tarea vencida.

**Resultado esperado:** se ordenan primero las vencidas y luego por próxima fecha; el estado no depende solo del color y conserva una etiqueta textual accesible.

## CP-18 - Marcar una tarea como completada

| Campo | Detalle |
|---|---|
| Objetivo | Verificar el flujo principal de SCRUM-22. |
| Precondiciones | Tarea pendiente asignada al usuario autenticado. |
| Datos | Tarea semanal `Limpiar baño`. |

**Pasos**

1. Abrir la tarea desde los pendientes.
2. Seleccionar **Marcar como completada**.
3. Confirmar la operación.
4. Revisar los pendientes y el historial.

**Resultado esperado:** se registra una sola finalización con el usuario y la fecha del servidor; la ocurrencia sale de pendientes; la tarea recurrente calcula su próxima fecha y se muestra confirmación.

## CP-19 - Evitar una finalización duplicada

| Campo | Detalle |
|---|---|
| Objetivo | Proteger la integridad ante doble clic o solicitudes concurrentes. |
| Precondiciones | Una sola ocurrencia pendiente para `ana.prueba`. |
| Datos | Dos solicitudes de finalización casi simultaneas. |

**Pasos**

1. Enviar dos veces la acción de completar con poca diferencia.
2. Consultar el historial de la tarea.
3. Consultar su siguiente fecha.

**Resultado esperado:** solo se crea un cumplimiento y solo se avanza una vez la fecha. La segunda solicitud devuelve una respuesta controlada e idempotente o informa que la ocurrencia ya fue completada.

## CP-20 - Consultar y filtrar el historial

| Campo | Detalle |
|---|---|
| Objetivo | Validar la consulta administrativa de SCRUM-23. |
| Precondiciones | Existen cumplimientos de varias tareas, personas y fechas. |
| Datos | Filtros por responsable, tarea, zona y rango de fechas. |

**Pasos**

1. Abrir **Historial** como administrador.
2. Aplicar cada filtro por separado.
3. Combinar responsable y rango de fechas.
4. Limpiar filtros.

**Resultado esperado:** cada resultado cumple todos los filtros activos; se indican filtros y cantidad; un conjunto vacío muestra un mensaje claro y no un error; al limpiar se recupera la consulta general.

## CP-21 - Conservar integridad del historial al cambiar datos

| Campo | Detalle |
|---|---|
| Objetivo | Evitar que una modificación posterior vuelva ambiguo un cumplimiento anterior. |
| Precondiciones | Tarea completada por una persona activa. |
| Datos | Cambiar nombre de tarea y desactivar a la persona después del cumplimiento. |

**Pasos**

1. Registrar un cumplimiento.
2. Editar el nombre de la tarea.
3. Desactivar a la persona.
4. Consultar el registro histórico.

**Resultado esperado:** el cumplimiento permanece asociado a identificadores válidos y conserva la información necesaria para auditoría. Las decisiones de mostrar nombre actual o una instantánea histórica deben ser consistentes y estar documentadas.

## CP-22 - Usar los flujos principales desde móvil

| Campo | Detalle |
|---|---|
| Objetivo | Verificar el requisito de interfaz adaptable y el riesgo de baja adopción. |
| Precondiciones | Interfaz disponible; vista de 360 px y dispositivo móvil cuando sea posible. |
| Datos | Acceso, pendientes, finalización e historial. |

**Pasos**

1. Ejecutar los cuatro flujos con ancho de 360 px.
2. Cambiar orientación y repetir los elementos principales.
3. Comprobar etiquetas, foco, botones y desplazamiento.
4. Verificar que no sea necesario ampliar para leer o actuar.

**Resultado esperado:** no hay contenido cortado ni desplazamiento horizontal de toda la página; los controles tienen etiquetas comprensibles, el foco es visible y las acciones principales pueden completarse sin depender del color.

## CP-23 - Aplicar permisos por rol

| Campo | Detalle |
|---|---|
| Objetivo | Evitar acceso no autorizado a funciones administrativas. |
| Precondiciones | Cuentas administradora y participante activas. |
| Datos | Rutas de personas, creación/edición de tareas e historial general. |

**Pasos**

1. Acceder como participante a cada ruta administrativa desde menús y URL directa.
2. Intentar enviar solicitudes de creación, edición y desactivación.
3. Repetir las operaciones autorizadas como administrador.
4. Revisar que el rechazo no modifique datos.

**Resultado esperado:** el participante recibe 403 o una redirección segura y no altera datos; ocultar un botón no sustituye la validación en el servidor; el administrador puede completar los flujos permitidos.

## CP-24 - Respaldar y restaurar la base de datos

| Campo | Detalle |
|---|---|
| Objetivo | Validar el control de continuidad y el procedimiento postproyecto. |
| Precondiciones | Base de pruebas con conteos conocidos y almacenamiento de respaldo disponible. |
| Datos | Personas, tareas, asignaciones y cumplimientos ficticios. |

**Pasos**

1. Registrar conteos y una muestra de relaciones.
2. Generar un respaldo consistente.
3. Crear una base vacía y restaurar el respaldo.
4. Aplicar verificaciones de integridad y comparar conteos.
5. Iniciar la aplicación contra la base restaurada y consultar un historial.

**Resultado esperado:** la restauración termina sin errores; los conteos y relaciones coinciden; el usuario puede consultar la información esperada y se registra duración, versión y ubicación protegida del respaldo.

---

## Plantilla para una ejecución real

Copiar este bloque por cada caso ejecutado:

```text
Caso:
Versión/commit:
Fecha y hora:
Ambiente:
Ejecutor:
Datos utilizados:
Resultado observado:
Estado: Aprobado | Fallido | Bloqueado | No ejecutado
Defecto relacionado:
Evidencia:
Observaciones:
```
