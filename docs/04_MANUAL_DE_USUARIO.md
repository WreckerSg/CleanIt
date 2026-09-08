# Manual básico de usuario de CleanIt

> [!WARNING]
> Documento de planificación conservado como antecedente. El manual vigente y sincronizado con la aplicación se encuentra en [`Documentación técnica y de usuario/01_Manual_basico_de_usuario.md`](../Documentaci%C3%B3n%20t%C3%A9cnica%20y%20de%20usuario/01_Manual_basico_de_usuario.md).

## Acerca de este manual

CleanIt se encuentra en fase de planificación. Este manual describe la experiencia propuesta para la primera versión y servirá como criterio de diseño y aceptación durante la implementación. Los nombres o la ubicación exacta de algunos controles podrán ajustarse después de las pruebas de usabilidad.

No existe todavía una URL de acceso ni capturas de una aplicación funcional.

## 1. Propósito del sistema

CleanIt permite que un grupo pequeño organice las tareas necesarias para mantener limpio un espacio. Un administrador registra personas y actividades, define responsables y frecuencias, y consulta el cumplimiento. Cada participante puede revisar sus pendientes y marcar lo que ya realizó.

## 2. Perfiles

| Perfil | Acciones principales |
|---|---|
| Administrador | Gestionar personas, zonas, tareas, frecuencias y asignaciones; consultar el estado general y el historial |
| Participante | Consultar sus propias tareas, revisar vencimientos y registrar el cumplimiento |

Una persona participante no debe acceder a las funciones administrativas ni a las tareas privadas de otros integrantes.

## 3. Acceso al sistema

Cuando exista un despliegue, el equipo publicará la dirección en la portada del repositorio.

1. Abra CleanIt desde un navegador actualizado.
2. Escriba su nombre de usuario y contraseña.
3. Seleccione **Iniciar sesión**.
4. Si los datos son correctos, el sistema mostrará la página inicial correspondiente a su rol.

Si las credenciales no son válidas, se mostrará un mensaje genérico. Después de varios intentos fallidos, espere y solicite ayuda al administrador; no comparta su contraseña.

## 4. Página inicial

La página principal mostrará información resumida:

- tareas vencidas;
- tareas para hoy;
- próximas tareas;
- actividades completadas recientemente;
- accesos directos autorizados para el perfil.

Las tareas vencidas tendrán texto e indicador visual. El color no será el único medio para reconocer su estado.

## 5. Administración de personas

### Registrar una persona

1. Entre en **Personas**.
2. Seleccione **Nueva persona**.
3. Ingrese nombre, correo o usuario y rol.
4. Revise que los datos sean correctos.
5. Seleccione **Guardar**.

El sistema no permitirá duplicar un identificador o correo definido como único. Los datos obligatorios se identificarán en el formulario.

### Editar una persona

1. Busque la persona en la lista.
2. Abra su detalle y seleccione **Editar**.
3. Cambie los datos permitidos.
4. Seleccione **Guardar cambios**.

Las tareas y cumplimientos existentes continuarán vinculados con la misma persona.

### Desactivar una persona

1. Abra el detalle de la persona.
2. Seleccione **Desactivar**.
3. Revise las tareas pendientes que deberán reasignarse.
4. Confirme la acción.

Una persona inactiva no podrá iniciar sesión ni recibir asignaciones nuevas. Sus registros históricos no se eliminarán.

## 6. Gestión de tareas

### Crear una tarea

1. Entre en **Tareas**.
2. Seleccione **Nueva tarea**.
3. Ingrese un nombre claro, por ejemplo `Limpiar el baño`.
4. Agregue una descripción breve y seleccione la zona.
5. Defina la primera fecha y la frecuencia.
6. Asigne una persona activa o deje la tarea temporalmente sin responsable.
7. Seleccione **Guardar**.

### Editar una tarea

1. Abra la tarea desde el listado.
2. Seleccione **Editar**.
3. Modifique los campos necesarios.
4. Revise si el cambio afecta una asignación o fecha cercana.
5. Guarde los cambios.

Editar una tarea no debe marcarla como realizada ni eliminar su historial.

### Retirar una tarea

Cuando una actividad deja de ser necesaria, utilice **Retirar** o **Desactivar**. Si ya tiene cumplimientos, no se eliminará físicamente: dejará de producir pendientes, pero continuará en el historial.

## 7. Asignaciones y frecuencias

### Asignar un responsable

1. Abra el detalle de una tarea.
2. Seleccione **Asignar responsable**.
3. Elija una persona activa.
4. Indique desde qué fecha aplica la asignación.
5. Guarde.

Si la persona anterior ya completó actividades, sus registros históricos permanecerán sin cambios.

### Tipos de frecuencia

| Frecuencia | Comportamiento propuesto |
|---|---|
| Única | Al completarse no genera otra fecha |
| Diaria | Programa la siguiente ocurrencia para el día siguiente |
| Semanal | Programa la siguiente ocurrencia siete días después |
| Mensual | Conserva el día de referencia; si no existe en un mes usa su último día válido |

Ejemplo mensual: una tarea programada el 31 de enero pasará al 28 o 29 de febrero y volverá al 31 en marzo.

## 8. Consultar mis pendientes

1. Inicie sesión como participante.
2. Abra **Mis pendientes**.
3. Revise primero las tareas vencidas y luego las próximas.
4. Utilice los filtros disponibles para fecha, zona o estado.
5. Seleccione una tarea para consultar sus detalles.

Cada participante verá solo las actividades que le corresponden. Si una tarea esperada no aparece, verifique con el administrador que esté activa, tenga fecha y se encuentre asignada correctamente.

## 9. Marcar una tarea como completada

1. Abra la actividad desde **Mis pendientes**.
2. Confirme que corresponde a la ocurrencia actual.
3. Seleccione **Marcar como completada**.
4. Agregue una observación opcional si el formulario la ofrece.
5. Confirme una sola vez y espere el mensaje de éxito.

El sistema registrará la fecha y el usuario autenticado. Si la tarea es recurrente, calculará una nueva fecha. Una misma ocurrencia no podrá completarse dos veces.

## 10. Consultar el historial

El administrador podrá entrar en **Historial** y filtrar por:

- tarea;
- persona responsable;
- zona;
- estado;
- rango de fechas.

El historial servirá para supervisar el cumplimiento, no para eliminar registros válidos. Los filtros activos y la cantidad de resultados deben permanecer visibles.

## 11. Cerrar sesión

1. Abra el menu del perfil.
2. Seleccione **Cerrar sesión**.
3. Compruebe que el sistema regrese a la página de acceso.

En un dispositivo compartido, cierre también el navegador y no permita que guarde la contraseña.

## 12. Mensajes frecuentes

| Mensaje o situación | Significado | Acción recomendada |
|---|---|---|
| Credenciales no válidas | Usuario, contraseña o estado de cuenta no permiten el acceso | Reintentar una vez y solicitar ayuda si persiste |
| Campo obligatorio | Falta información necesaria | Completar el campo indicado |
| Correo o usuario existente | El identificador ya está registrado | Buscar la cuenta o usar otro identificador válido |
| Responsable no disponible | La persona está inactiva o no existe | Elegir otra persona activa |
| Tarea ya completada | La ocurrencia fue registrada previamente | Actualizar la página y consultar el historial |
| Acceso denegado | El perfil no tiene permiso para esa operación | Regresar o contactar al administrador si considera que es un error |
| Servicio temporalmente no disponible | La aplicación o base de datos no responde | Esperar, usar el procedimiento de contingencia y reportar la hora |

## 13. Recomendaciones de uso

- Use nombres de tareas concretos y faciles de distinguir.
- Mantenga actualizados responsables, fechas y estados.
- Marque la tarea solo después de realizarla.
- No comparta cuentas ni contraseñas.
- Revise las tareas vencidas al iniciar la jornada.
- No incluya información personal innecesaria en las descripciones.
- Informe los errores mediante la plantilla de incidencias del repositorio.

## 14. Solicitar soporte

Al reportar un problema incluya:

- acción que intentaba realizar;
- fecha y hora aproximada;
- página o función afectada;
- pasos para repetirlo;
- mensaje mostrado;
- navegador y dispositivo;
- captura revisada para que no contenga datos sensibles.

La prioridad y los tiempos objetivo se explican en la [estrategia de gestión postproyecto](06_GESTION_POST_PROYECTO.md).

## 15. Glosario

| Término | Definición |
|---|---|
| Tarea | Actividad de limpieza definida por el administrador |
| Ocurrencia | Realización esperada de una tarea para una fecha concreta |
| Pendiente | Ocurrencia que aún no ha sido registrada como completada |
| Vencida | Ocurrencia pendiente cuya fecha ya paso |
| Frecuencia | Regla utilizada para programar la siguiente ocurrencia |
| Historial | Registro de actividades completadas y sus responsables |
