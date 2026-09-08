# Modelo de casos de prueba de CleanIt

> [!IMPORTANT]
> **Estado:** 30 casos diseñados. La ejecución del MVP y los casos condicionados por ambiente se detallan en [`evidencias-reales/`](evidencias-reales/README.md); las fichas siguientes conservan el diseño original.

## Control del documento

| Campo | Valor |
|---|---|
| Proyecto | CleanIt - Organizador de tareas de limpieza |
| Versión | 1.1 |
| Responsable de verificación | Rol Calidad y DevOps |
| Autor | Estudiante responsable del proyecto |
| Estado | Diseño completo; ejecución registrada por versión |

## Resumen

| Nivel | Cantidad | Identificadores |
|---|---:|---|
| Unitarias | 5 | PU-01 a PU-05 |
| Integración | 6 | PI-01 a PI-06 |
| Sistema funcional | 11 | PSF-01 a PSF-11 |
| Sistema no funcional | 6 | PSN-01 a PSN-06 |
| Documentales | 2 | PD-01 a PD-02 |
| **Total** | **30** | |

La [matriz de trazabilidad](05_Matriz_de_trazabilidad.md) relaciona estos casos con historias, riesgos y atributos de calidad. Cada ejecución futura utilizará la [plantilla de registro](plantillas/Plantilla_registro_de_ejecucion.md).

## Procedimiento general de integración

1. Identificar componentes, versiones y commit.
2. Preparar la base aislada y aplicar migraciones.
3. Ejecutar unitarias y casos de integración aplicables.
4. Si existe un error crítico o alto, detener la promoción y corregir en `dev`.
5. Si no existen bloqueos, registrar evidencias y continuar con pruebas del sistema en `qa`.

## 1. Casos y procedimientos de pruebas unitarias

Pruebas automatizadas y aisladas de reglas del dominio.

### PU-01 - Validar datos obligatorios y frecuencia de una tarea

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-17, SCRUM-19 |
| Nivel/tipo | Unitaria - funcional |
| Componente o subsistema | Tareas / validadores |
| Prioridad | Alta |
| Responsable previsto | Backend y datos |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Comprobar que una tarea solo acepte nombre, zona, fecha y frecuencia pertenecientes al dominio definido.

**Precondiciones y entorno:** Validadores del modelo o formulario disponibles en un ambiente aislado.

| Entrada o condición | Salida esperada |
|---|---|
| Caso válido; nombre vacío; nombre superior al límite; fecha inválida; frecuencia fuera de única, diaria, semanal o mensual. | La tarea válida supera la validación. Cada entrada inválida se rechaza de forma específica y no deja un objeto considerado válido. |

**Procedimiento**

1. Construir una tarea válida y ejecutar sus validaciones.
2. Repetir la validación con cada dato inválido.
3. Comprobar los errores asociados a cada campo.

**Poscondición:** No se modifica información persistente.

**Evidencia requerida:** Salida automatizada con una aserción por partición válida e inválida.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PU-02 - Rechazar responsables inactivos

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-20 |
| Nivel/tipo | Unitaria - regla de negocio |
| Componente o subsistema | Asignaciones |
| Prioridad | Alta |
| Responsable previsto | Backend y datos |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Verificar que la regla de asignación solo permita personas activas.

**Precondiciones y entorno:** Servicio o validador de asignación disponible; objetos de usuario ficticios activo e inactivo.

| Entrada o condición | Salida esperada |
|---|---|
| `ana.prueba` activa y `maria.inactiva` inactiva. | La persona activa es aceptada y la inactiva produce un error controlado antes de guardar la asignación. |

**Procedimiento**

1. Evaluar una asignación con la persona activa.
2. Evaluar la misma tarea con la persona inactiva.
3. Comparar los resultados y mensajes de validación.

**Poscondición:** La tarea conserva su responsable anterior o permanece sin asignar.

**Evidencia requerida:** Reporte unitario y aserción de que no se acepta el estado inactivo.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PU-03 - Calcular recurrencias diaria y semanal

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-19 |
| Nivel/tipo | Unitaria - valores de dominio |
| Componente o subsistema | Servicio de recurrencia |
| Prioridad | Alta |
| Responsable previsto | Backend y datos |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Comprobar el cálculo de la siguiente fecha para frecuencias diaria y semanal.

**Precondiciones y entorno:** Función de cálculo disponible y zona horaria definida.

| Entrada o condición | Salida esperada |
|---|---|
| 10/09/2026 con frecuencia diaria y 10/09/2026 con frecuencia semanal. | Los resultados son 11/09/2026 y 17/09/2026; el cambio de mes no altera el intervalo esperado. |

**Procedimiento**

1. Calcular la siguiente fecha para la tarea diaria.
2. Calcular la siguiente fecha para la tarea semanal.
3. Repetir cerca de un cambio de mes.

**Poscondición:** La fecha original utilizada como entrada no cambia.

**Evidencia requerida:** Salida automatizada con fechas de entrada y resultado de cada aserción.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PU-04 - Conservar el día ancla en recurrencias mensuales

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-19 |
| Nivel/tipo | Unitaria - valores límite |
| Componente o subsistema | Servicio de recurrencia |
| Prioridad | Alta |
| Responsable previsto | Backend y datos |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Validar meses con diferente cantidad de días y años bisiestos sin perder el día de referencia.

**Precondiciones y entorno:** Función de recurrencia mensual disponible.

| Entrada o condición | Salida esperada |
|---|---|
| 31/01/2026, 31/01/2028, 30/11/2026 y día ancla asociado. | Se usa el último día válido de febrero y luego se recupera el día ancla: 28/02/2026 y 31/03/2026; 29/02/2028 y 31/03/2028; 30/12/2026. |

**Procedimiento**

1. Calcular dos ocurrencias desde el 31/01/2026.
2. Repetir para el año bisiesto 2028.
3. Calcular la ocurrencia posterior al 30/11/2026.

**Poscondición:** El día ancla permanece almacenado para cálculos posteriores.

**Evidencia requerida:** Reporte unitario con la tabla de fechas esperadas y obtenidas.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PU-05 - Determinar estado pendiente y vencido

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-21 |
| Nivel/tipo | Unitaria - transición de estados |
| Componente o subsistema | Seguimiento |
| Prioridad | Alta |
| Responsable previsto | Backend y datos |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Comprobar que el estado visible dependa de la próxima fecha, la finalización y el retiro lógico.

**Precondiciones y entorno:** Reloj controlado en 10/09/2026 y objetos sin dependencia de la fecha del equipo.

| Entrada o condición | Salida esperada |
|---|---|
| Fechas 09/09, 10/09 y 11/09; tarea completada; tarea retirada. | La fecha anterior se clasifica vencida; la actual y futura, pendientes; una ocurrencia completada no queda pendiente; una tarea retirada no se ofrece para ejecución. |

**Procedimiento**

1. Evaluar una tarea con cada fecha.
2. Evaluar una tarea completada para la ocurrencia actual.
3. Evaluar una tarea retirada.

**Poscondición:** No se crean finalizaciones ni nuevas ocurrencias.

**Evidencia requerida:** Salida automatizada con una aserción por estado.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

## 2. Casos y procedimientos de pruebas de integración

Interacción entre componentes, subsistemas y persistencia.

### PI-01 - Integrar autenticación, sesión y permisos

| Campo | Valor |
|---|---|
| Requisito/Jira | Acceso, RNF seguridad |
| Nivel/tipo | Integración |
| Componente o subsistema | Cuentas, vistas y sesiones |
| Prioridad | Alta |
| Responsable previsto | Backend y datos / QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Confirmar que Django autentique cuentas activas y aplique permisos al acceder a vistas protegidas.

**Precondiciones y entorno:** Base de QA con administrador, participante activo e inactivo; cliente de pruebas disponible.

| Entrada o condición | Salida esperada |
|---|---|
| Credenciales válidas, inválidas e identificadores de vistas administrativas y personales. | El administrador obtiene acceso; el participante recibe denegación controlada; las sesiones anónima e inactiva son redirigidas al acceso sin revelar datos. |

**Procedimiento**

1. Iniciar sesión como administrador y solicitar una vista administrativa.
2. Repetir como participante y solicitar la misma vista.
3. Intentar acceso anónimo y con cuenta inactiva.

**Poscondición:** No cambia información de negocio y ninguna sesión inválida permanece activa.

**Evidencia requerida:** Salida del cliente de Django con códigos de respuesta y permisos evaluados.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PI-02 - Persistir el ciclo de vida de una persona

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-15, SCRUM-16 |
| Nivel/tipo | Integración |
| Componente o subsistema | Personas, formularios y ORM |
| Prioridad | Alta |
| Responsable previsto | Backend y datos / QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Verificar registro, edición y desactivación a través de formulario, vista y base de datos.

**Precondiciones y entorno:** Administrador autenticado y correo ficticio no registrado.

| Entrada o condición | Salida esperada |
|---|---|
| Ana Prueba, `ana.prueba@example.test`, rol participante. | Se crea un único registro, la edición conserva su identificador y la cuenta desactivada no puede iniciar sesión ni recibir nuevas tareas. |

**Procedimiento**

1. Enviar el formulario de registro válido.
2. Consultar el objeto almacenado y editar el nombre.
3. Desactivar la cuenta e intentar autenticarla.

**Poscondición:** La identidad permanece disponible para relaciones históricas.

**Evidencia requerida:** Salida de pruebas y consulta controlada del registro antes y después de cada operación.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PI-03 - Persistir creación, edición y retiro lógico de tareas

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-17, SCRUM-18, SCRUM-23 |
| Nivel/tipo | Integración |
| Componente o subsistema | Tareas, formularios, ORM e historial |
| Prioridad | Alta |
| Responsable previsto | Backend y datos / QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Comprobar que el ciclo de vida de la tarea preserve su identidad y la trazabilidad histórica.

**Precondiciones y entorno:** Administrador autenticado; zona Cocina y un cumplimiento histórico disponibles.

| Entrada o condición | Salida esperada |
|---|---|
| Tarea `Trapear cocina`, cambio de descripción y orden de retiro. | La tarea se persiste una sola vez, conserva el identificador al editarse, deja de admitir nuevas asignaciones al retirarse y mantiene el historial consultable. |

**Procedimiento**

1. Crear la tarea desde el formulario.
2. Editar descripción y zona, y consultar el mismo identificador.
3. Retirar la tarea y consultar el historial relacionado.

**Poscondición:** El registro queda inactivo o retirado, no eliminado físicamente si tiene historial.

**Evidencia requerida:** Reporte de integración y consultas de estado, identificador y relaciones.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PI-04 - Integrar asignación con el estado de la persona

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-20 |
| Nivel/tipo | Integración |
| Componente o subsistema | Tareas, personas y asignaciones |
| Prioridad | Alta |
| Responsable previsto | Backend y datos / QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Confirmar que interfaz y servidor coincidan al permitir solamente responsables activos.

**Precondiciones y entorno:** Administrador autenticado; tarea sin responsable; una persona activa y una inactiva.

| Entrada o condición | Salida esperada |
|---|---|
| Identificadores de `ana.prueba` y `maria.inactiva`. | Solo la persona activa aparece y puede guardarse. La solicitud manipulada se rechaza también en el servidor y no altera la asignación válida. |

**Procedimiento**

1. Consultar las opciones del selector de responsables.
2. Asignar la tarea a la persona activa.
3. Enviar manualmente una solicitud con la persona inactiva.

**Poscondición:** Existe una única asignación vigente a una persona activa.

**Evidencia requerida:** Salida de integración, respuesta HTTP y consulta de la asignación persistida.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PI-05 - Completar una tarea recurrente y actualizar el historial

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-19, SCRUM-22, SCRUM-23 |
| Nivel/tipo | Integración |
| Componente o subsistema | Seguimiento, recurrencia y ORM |
| Prioridad | Alta |
| Responsable previsto | Backend y datos / QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Verificar la operación transaccional que registra un cumplimiento y programa la siguiente ocurrencia.

**Precondiciones y entorno:** Tarea semanal pendiente asignada a `ana.prueba`.

| Entrada o condición | Salida esperada |
|---|---|
| Tarea `Limpiar baño` con próxima fecha 10/09/2026. | Se crea un cumplimiento con usuario y fecha del servidor, desaparece la ocurrencia actual de pendientes y la próxima fecha queda en 17/09/2026. |

**Procedimiento**

1. Autenticar a la responsable y ejecutar la finalización.
2. Consultar el historial de la tarea.
3. Consultar la nueva próxima fecha y la lista de pendientes.

**Poscondición:** La tarea continúa activa con una sola nueva ocurrencia pendiente.

**Evidencia requerida:** Salida de integración y consulta de cumplimiento, responsable y próxima fecha.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PI-06 - Evitar finalizaciones duplicadas

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-22 |
| Nivel/tipo | Integración - concurrencia |
| Componente o subsistema | Seguimiento y base de datos |
| Prioridad | Alta |
| Responsable previsto | Backend y datos / QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Proteger la integridad cuando se reciben dos solicitudes casi simultáneas para la misma ocurrencia.

**Precondiciones y entorno:** Una sola ocurrencia pendiente y mecanismo de transacción o unicidad previsto.

| Entrada o condición | Salida esperada |
|---|---|
| Dos solicitudes equivalentes de finalización. | Solo se crea un cumplimiento y la recurrencia avanza una vez. La solicitud repetida responde de forma idempotente o informa que ya fue completada. |

**Procedimiento**

1. Preparar la ocurrencia y registrar su identificador.
2. Enviar dos solicitudes concurrentes o inmediatamente consecutivas.
3. Contar cumplimientos y revisar la siguiente fecha.

**Poscondición:** Una ocurrencia completada, un registro histórico y una siguiente fecha.

**Evidencia requerida:** Salida concurrente, conteo de filas y respuesta de ambas solicitudes.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

## 3. Casos funcionales del sistema

Recorridos completos observados desde la perspectiva de los roles.

### PSF-01 - Iniciar sesión con una cuenta válida

| Campo | Valor |
|---|---|
| Requisito/Jira | Acceso |
| Nivel/tipo | Sistema - funcional |
| Componente o subsistema | Acceso e interfaz |
| Prioridad | Alta |
| Responsable previsto | QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Validar el recorrido de inicio de sesión y la redirección según el rol.

**Precondiciones y entorno:** Aplicación disponible; cuentas activas de administrador y participante.

| Entrada o condición | Salida esperada |
|---|---|
| Credenciales ficticias válidas. | Se crea la sesión, la contraseña no aparece en URL ni pantalla y cada rol llega a su vista autorizada. |

**Procedimiento**

1. Abrir la pantalla de acceso.
2. Ingresar credenciales válidas y seleccionar Iniciar sesión.
3. Repetir con ambos roles y observar las opciones visibles.

**Poscondición:** La sesión queda activa hasta cierre o expiración.

**Evidencia requerida:** Registro de ejecución y captura sin contraseña de la página inicial por rol.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PSF-02 - Rechazar acceso inválido o inactivo

| Campo | Valor |
|---|---|
| Requisito/Jira | Acceso, SCRUM-16 |
| Nivel/tipo | Sistema - funcional negativa |
| Componente o subsistema | Acceso e interfaz |
| Prioridad | Alta |
| Responsable previsto | QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Evitar sesiones con contraseña incorrecta, usuario inexistente o cuenta inactiva.

**Precondiciones y entorno:** Existe `maria.inactiva` y se conoce una cuenta activa.

| Entrada o condición | Salida esperada |
|---|---|
| Contraseña incorrecta, usuario inexistente y cuenta inactiva. | No se crea sesión; el mensaje no confirma si la cuenta existe; la página privada redirige al acceso o devuelve una denegación controlada. |

**Procedimiento**

1. Enviar cada combinación desde el formulario.
2. Observar el mensaje mostrado.
3. Intentar abrir directamente una página privada.

**Poscondición:** Todas las sesiones inválidas permanecen cerradas.

**Evidencia requerida:** Registro de respuestas y captura del mensaje genérico.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PSF-03 - Registrar una persona válida

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-15 |
| Nivel/tipo | Sistema - funcional |
| Componente o subsistema | Administración de personas |
| Prioridad | Alta |
| Responsable previsto | QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Comprobar el recorrido administrativo para crear una persona participante.

**Precondiciones y entorno:** Administrador autenticado y correo no registrado.

| Entrada o condición | Salida esperada |
|---|---|
| Ana Prueba, `ana.prueba@example.test`, rol participante. | Se crea un único registro activo, aparece confirmación y la persona queda disponible para recibir tareas. |

**Procedimiento**

1. Abrir Personas y seleccionar Nueva persona.
2. Completar los campos obligatorios y guardar.
3. Buscar la persona en la lista y abrir su detalle.

**Poscondición:** La nueva persona permanece activa y sin tareas asignadas.

**Evidencia requerida:** Capturas del formulario sin credenciales y del registro creado.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PSF-04 - Validar persona duplicada o incompleta

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-15 |
| Nivel/tipo | Sistema - funcional negativa |
| Componente o subsistema | Administración de personas |
| Prioridad | Alta |
| Responsable previsto | QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Confirmar que la interfaz y el servidor rechacen datos incompletos, inválidos o duplicados.

**Precondiciones y entorno:** Administrador autenticado y correo de Ana ya registrado.

| Entrada o condición | Salida esperada |
|---|---|
| Correo repetido, nombre vacío y correo con formato inválido. | Cada intento se rechaza con indicación del campo; no se crean registros parciales ni duplicados. |

**Procedimiento**

1. Intentar registrar el correo repetido.
2. Repetir dejando vacío el nombre.
3. Repetir con correo mal formado y consultar la lista.

**Poscondición:** La cantidad de personas se mantiene sin cambios.

**Evidencia requerida:** Captura de validaciones y conteo antes y después.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PSF-05 - Editar y desactivar una persona conservando relaciones

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-16 |
| Nivel/tipo | Sistema - funcional |
| Componente o subsistema | Administración de personas |
| Prioridad | Alta |
| Responsable previsto | QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Comprobar que el administrador actualice una persona y pueda desactivarla sin borrar su historial.

**Precondiciones y entorno:** Persona activa con una tarea pendiente y un cumplimiento histórico.

| Entrada o condición | Salida esperada |
|---|---|
| Cambio de nombre y acción de desactivación sobre `ana.prueba`. | El nombre cambia sin crear otra identidad; la cuenta no vuelve a iniciar sesión ni recibe nuevas asignaciones; el historial anterior permanece visible. |

**Procedimiento**

1. Editar el nombre visible y guardar.
2. Comprobar la asignación existente.
3. Desactivar la cuenta, intentar acceso y consultar el historial.

**Poscondición:** La persona queda inactiva y sus relaciones históricas se conservan.

**Evidencia requerida:** Capturas del estado y consulta del historial asociada.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PSF-06 - Crear una tarea válida

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-17 |
| Nivel/tipo | Sistema - funcional |
| Componente o subsistema | Administración de tareas |
| Prioridad | Alta |
| Responsable previsto | QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Validar el flujo completo de creación de una tarea de limpieza.

**Precondiciones y entorno:** Administrador autenticado y zona Cocina disponible.

| Entrada o condición | Salida esperada |
|---|---|
| `Trapear cocina`, descripción, zona, próxima fecha y frecuencia única. | Se crea una sola tarea activa con los datos suministrados y queda disponible para asignación. |

**Procedimiento**

1. Abrir Tareas y seleccionar Nueva tarea.
2. Completar los campos y guardar.
3. Consultar la lista y el detalle.

**Poscondición:** Tarea activa, sin cumplimiento y con identificador único.

**Evidencia requerida:** Captura del detalle y registro del identificador creado.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PSF-07 - Editar y retirar una tarea sin perder historial

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-18 |
| Nivel/tipo | Sistema - funcional |
| Componente o subsistema | Administración de tareas |
| Prioridad | Alta |
| Responsable previsto | QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Comprobar edición y retiro lógico preservando cumplimientos anteriores.

**Precondiciones y entorno:** Tarea activa con al menos un cumplimiento histórico.

| Entrada o condición | Salida esperada |
|---|---|
| Cambio de descripción, zona y acción Retirar. | La edición se refleja sin duplicar la tarea; al retirarla deja de aparecer para nuevas ejecuciones y su historial se conserva. |

**Procedimiento**

1. Editar los campos permitidos y guardar.
2. Verificar el mismo identificador.
3. Retirar la tarea y consultar pendientes e historial.

**Poscondición:** Tarea retirada y registros históricos intactos.

**Evidencia requerida:** Capturas de antes/después y del historial conservado.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PSF-08 - Configurar todas las frecuencias

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-19 |
| Nivel/tipo | Sistema - funcional |
| Componente o subsistema | Tareas y recurrencia |
| Prioridad | Alta |
| Responsable previsto | QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Validar desde la interfaz las frecuencias única, diaria, semanal y mensual.

**Precondiciones y entorno:** Administrador autenticado y cuatro tareas de prueba.

| Entrada o condición | Salida esperada |
|---|---|
| Una frecuencia por tarea, incluida una mensual con día 31. | La tarea única termina sin nueva ocurrencia; las demás calculan la fecha diaria, semanal o mensual según su regla y día ancla. |

**Procedimiento**

1. Configurar y guardar cada frecuencia.
2. Completar una ocurrencia de cada tarea.
3. Consultar la próxima fecha o finalización definitiva.

**Poscondición:** Cada tarea conserva su frecuencia y estado coherente.

**Evidencia requerida:** Tabla de fechas esperadas/observadas y capturas de cada configuración.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PSF-09 - Asignar una tarea solo a una persona activa

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-20 |
| Nivel/tipo | Sistema - funcional y negativa |
| Componente o subsistema | Tareas y personas |
| Prioridad | Alta |
| Responsable previsto | QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Comprobar el flujo de asignación y el rechazo de cuentas inactivas.

**Precondiciones y entorno:** Administrador autenticado; tarea sin responsable; Ana activa y María inactiva.

| Entrada o condición | Salida esperada |
|---|---|
| Selección de Ana y solicitud manipulada con el identificador de María. | Ana queda asignada y ve la tarea; María no aparece y la solicitud manipulada es rechazada sin cambiar la asignación. |

**Procedimiento**

1. Abrir el selector y asignar la tarea a Ana.
2. Confirmar que aparezca en sus pendientes.
3. Intentar sustituirla por María mediante una solicitud manipulada.

**Poscondición:** Una sola asignación vigente a Ana.

**Evidencia requerida:** Captura de la asignación, respuesta negativa y consulta posterior.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PSF-10 - Mostrar pendientes propios, ordenados y vencidos

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-21 |
| Nivel/tipo | Sistema - funcional y autorización |
| Componente o subsistema | Seguimiento |
| Prioridad | Alta |
| Responsable previsto | QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Confirmar el aislamiento entre participantes y la priorización por vencimiento y fecha.

**Precondiciones y entorno:** Ana y Luis poseen tareas diferentes con fechas pasada, actual y futura.

| Entrada o condición | Salida esperada |
|---|---|
| Dos tareas de Ana, una de Luis y una sin asignar. | Cada persona observa solo sus pendientes; una tarea ajena no revela datos; las vencidas aparecen primero y su estado también se expresa mediante texto. |

**Procedimiento**

1. Abrir Mis pendientes como Ana y registrar los identificadores.
2. Repetir como Luis.
3. Intentar abrir por URL una tarea ajena y revisar orden y etiquetas.

**Poscondición:** No se modifica ninguna tarea.

**Evidencia requerida:** Capturas por usuario, lista de identificadores y respuesta al acceso ajeno.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PSF-11 - Completar una tarea y consultar su historial

| Campo | Valor |
|---|---|
| Requisito/Jira | SCRUM-22, SCRUM-23 |
| Nivel/tipo | Sistema - funcional |
| Componente o subsistema | Seguimiento e historial |
| Prioridad | Alta |
| Responsable previsto | QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Validar el recorrido principal desde pendientes hasta la consulta administrativa del cumplimiento.

**Precondiciones y entorno:** Tarea semanal asignada a Ana y administrador disponible.

| Entrada o condición | Salida esperada |
|---|---|
| `Limpiar baño`, fecha actual y filtros por persona, tarea y rango. | Se registra un cumplimiento con Ana y fecha del servidor; se calcula la siguiente ocurrencia; el historial encuentra exactamente el registro al aplicar los filtros. |

**Procedimiento**

1. Abrir la tarea como Ana y marcarla completada.
2. Comprobar que sale de la ocurrencia pendiente.
3. Abrir Historial como administrador y aplicar los filtros.

**Poscondición:** Una ocurrencia completada y una siguiente ocurrencia pendiente.

**Evidencia requerida:** Capturas del mensaje, la próxima fecha y el historial filtrado.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

## 4. Casos no funcionales del sistema

Seguridad, usabilidad, rendimiento, estrés y recuperación.

### PSN-01 - Aplicar autorización por rol y por objeto

| Campo | Valor |
|---|---|
| Requisito/Jira | RNF seguridad |
| Nivel/tipo | Sistema - seguridad |
| Componente o subsistema | Autorización |
| Prioridad | Alta |
| Responsable previsto | QA / Seguridad |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Impedir que un participante acceda a administración o a objetos pertenecientes a otra persona.

**Precondiciones y entorno:** Cuentas de administrador, Ana y Luis; tareas separadas por responsable.

| Entrada o condición | Salida esperada |
|---|---|
| Menús, URL administrativas e identificador de una tarea ajena. | La interfaz oculta opciones no permitidas y el servidor rechaza cada solicitud directa sin revelar información del objeto. |

**Procedimiento**

1. Comparar las opciones visibles por rol.
2. Solicitar una URL administrativa como participante.
3. Solicitar el detalle y la acción de completar de una tarea ajena.

**Poscondición:** No se modifica ningún usuario, tarea ni cumplimiento.

**Evidencia requerida:** Matriz de acceso con código de respuesta y capturas sin datos sensibles.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PSN-02 - Proteger formularios, entradas y secretos

| Campo | Valor |
|---|---|
| Requisito/Jira | RNF seguridad |
| Nivel/tipo | Sistema - seguridad |
| Componente o subsistema | Aplicación y configuración |
| Prioridad | Alta |
| Responsable previsto | QA / Seguridad |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Comprobar controles CSRF, validación de entradas y ausencia de secretos versionados.

**Precondiciones y entorno:** Ambiente de QA y acceso de solo lectura al contenido del repositorio.

| Entrada o condición | Salida esperada |
|---|---|
| Solicitud sin token CSRF; texto con HTML; frecuencia manipulada; búsqueda de claves y contraseñas. | La escritura sin token y los valores inválidos se rechazan; el contenido se escapa; no existen secretos reales en Git. |

**Procedimiento**

1. Enviar una operación de escritura sin token CSRF.
2. Enviar texto y valores fuera del dominio permitido.
3. Revisar el repositorio y la respuesta renderizada para detectar secretos o HTML ejecutado.

**Poscondición:** No se crean registros inválidos y las credenciales permanecen fuera del repositorio.

**Evidencia requerida:** Respuestas HTTP, capturas sanitizadas y salida del escaneo de secretos.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PSN-03 - Completar recorridos en escritorio y móvil

| Campo | Valor |
|---|---|
| Requisito/Jira | RNF usabilidad y compatibilidad |
| Nivel/tipo | Sistema - usabilidad |
| Componente o subsistema | Interfaz |
| Prioridad | Media |
| Responsable previsto | Frontend/UX / QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Verificar adaptabilidad, comprensión y finalización de los cuatro recorridos principales.

**Precondiciones y entorno:** Chrome, Firefox y Edge; anchos 360, 390 y 430 px; cinco participantes representativos.

| Entrada o condición | Salida esperada |
|---|---|
| Iniciar sesión, localizar pendiente, completar tarea y consultar historial. | Al menos 85 % de los recorridos termina sin ayuda, el promedio no supera tres minutos y ninguna vista impide operar por desbordamiento o controles inaccesibles. |

**Procedimiento**

1. Ejecutar cada recorrido en los navegadores y tamaños definidos.
2. Registrar necesidad de ayuda, tiempo y errores de interacción.
3. Comprobar texto, foco, botones y ausencia de desbordamiento general.

**Poscondición:** Los datos creados se identifican como prueba y pueden limpiarse.

**Evidencia requerida:** Matriz de dispositivos, tiempos anónimos, observaciones y capturas revisadas.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PSN-04 - Mantener rendimiento bajo la carga objetivo

| Campo | Valor |
|---|---|
| Requisito/Jira | RNF eficiencia |
| Nivel/tipo | Sistema - rendimiento |
| Componente o subsistema | Aplicación y base de datos |
| Prioridad | Media |
| Responsable previsto | QA / DevOps |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Medir las operaciones principales con una carga representativa para grupos pequeños.

**Precondiciones y entorno:** Ambiente equivalente a preproducción con 1.000 tareas y 5.000 registros históricos.

| Entrada o condición | Salida esperada |
|---|---|
| 50 usuarios virtuales durante 10 minutos, crecimiento de 5 usuarios por minuto. | El p95 de cada operación principal es menor o igual a 2,0 s y la tasa de error permanece por debajo de 1 %. |

**Procedimiento**

1. Preparar los datos y verificar una prueba de humo.
2. Ejecutar consultas de pendientes e historial, creación/asignación y finalización.
3. Calcular p50, p95, p99 y tasa de errores por operación.

**Poscondición:** El ambiente conserva integridad y queda disponible para comprobaciones posteriores.

**Evidencia requerida:** Reporte original de la herramienta, configuración de carga y resumen de percentiles.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PSN-05 - Identificar el límite y recuperar el sistema después de estrés

| Campo | Valor |
|---|---|
| Requisito/Jira | RNF fiabilidad y eficiencia |
| Nivel/tipo | Sistema - estrés |
| Componente o subsistema | Aplicación, servidor y base de datos |
| Prioridad | Media |
| Responsable previsto | QA / DevOps |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Observar degradación al superar la carga objetivo y confirmar recuperación sin corrupción.

**Precondiciones y entorno:** Ambiente descartable con monitoreo y respaldo previo.

| Entrada o condición | Salida esperada |
|---|---|
| Carga creciente por etapas por encima de 50 usuarios virtuales. | El límite queda documentado, los errores son controlados, el servicio se recupera y no aparecen registros parciales o duplicados. |

**Procedimiento**

1. Aumentar la carga gradualmente y registrar recursos, latencia y errores.
2. Detener al alcanzar el límite seguro o una degradación definida.
3. Retirar la carga, ejecutar una prueba de humo y verificar conteos críticos.

**Poscondición:** El ambiente vuelve a responder y sus relaciones críticas son consistentes.

**Evidencia requerida:** Reporte de carga, métricas de recursos, tiempos de recuperación y conteos posteriores.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PSN-06 - Respaldar y restaurar PostgreSQL

| Campo | Valor |
|---|---|
| Requisito/Jira | RNF continuidad, SCRUM-23, SCRUM-35 |
| Nivel/tipo | Sistema - recuperación |
| Componente o subsistema | PostgreSQL y almacenamiento |
| Prioridad | Alta |
| Responsable previsto | DevOps / QA |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Comprobar que un respaldo permita recuperar usuarios, tareas, asignaciones e historial.

**Precondiciones y entorno:** Base de QA con conteos conocidos y destino de restauración vacío.

| Entrada o condición | Salida esperada |
|---|---|
| Conjunto ficticio con usuarios activos/inactivos, tareas y cumplimientos. | La restauración termina sin errores y el 100 % de las comprobaciones críticas coincide con la base de origen. |

**Procedimiento**

1. Registrar conteos y relaciones de referencia.
2. Generar el respaldo y restaurarlo en una base vacía.
3. Comparar conteos, claves y relaciones, y ejecutar una consulta funcional.

**Poscondición:** La base restaurada queda aislada y disponible para validación, sin reemplazar producción.

**Evidencia requerida:** Log original de respaldo/restauración, checksums cuando apliquen y tabla comparativa.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

## 5. Procedimientos de prueba de documentos

Formato, completitud, correctitud y entendibilidad.

### PD-01 - Verificar el plan y el modelo de casos

| Campo | Valor |
|---|---|
| Requisito/Jira | Paso 1 de la actividad |
| Nivel/tipo | Documental |
| Componente o subsistema | Plan de pruebas |
| Prioridad | Media |
| Responsable previsto | QA / Revisor académico |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Evaluar formato, completitud, correctitud, trazabilidad y entendibilidad de los documentos del Paso 1.

**Precondiciones y entorno:** Versión candidata de todos los archivos de `Plan de pruebas/`.

| Entrada o condición | Salida esperada |
|---|---|
| Lista de campos obligatorios, historias SCRUM-15 a SCRUM-23 y enlaces internos. | Los 30 casos están completos, las cifras son coherentes, las historias tienen cobertura y el lector distingue claramente metas, resultados simulados y resultados reales. |

**Procedimiento**

1. Revisar que cada caso contenga todos los campos de la plantilla adaptada.
2. Comprobar cálculos, cantidades, identificadores y enlaces.
3. Solicitar a otra persona seguir una muestra de casos y registrar dudas.

**Poscondición:** Las observaciones se corrigen o quedan registradas con responsable.

**Evidencia requerida:** Checklist firmado o comentado, informe de enlaces y observaciones de revisión.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

### PD-02 - Verificar manual y documentación técnica

| Campo | Valor |
|---|---|
| Requisito/Jira | Paso 2 de la actividad |
| Nivel/tipo | Documental |
| Componente o subsistema | Manual y descripción técnica |
| Prioridad | Media |
| Responsable previsto | QA / Product Owner |
| Versión objetivo | MVP 1.0.0 |
| Estado | Diseñado; ejecución registrada por versión |

**Objetivo:** Confirmar que la documentación futura corresponda al alcance, versión y comportamiento del sistema.

**Precondiciones y entorno:** Manual y documentación técnica en versión candidata.

| Entrada o condición | Salida esperada |
|---|---|
| Historias, arquitectura, pasos de usuario, tecnologías y restricciones. | La documentación es completa para la versión, técnicamente coherente, comprensible y no atribuye funciones inexistentes al producto. |

**Procedimiento**

1. Comparar funciones documentadas con el alcance y la versión.
2. Comprobar formato, enlaces, términos, requisitos y tecnologías.
3. Seguir una muestra de procedimientos y registrar ambigüedades.

**Poscondición:** Las correcciones documentales quedan versionadas con la entrega correspondiente.

**Evidencia requerida:** Lista de comprobación, enlaces revisados y observaciones de lectura.

**Criterio de aprobación:** todas las salidas esperadas se cumplen y no se observan efectos secundarios no autorizados.

## Estado de ejecución

Los 30 casos se encuentran diseñados. Ninguno tiene una ejecución real porque todavía no existe una versión funcional de CleanIt. Los archivos de `evidencias-simuladas/` muestran únicamente el formato y el ciclo hipotético de resultados.
