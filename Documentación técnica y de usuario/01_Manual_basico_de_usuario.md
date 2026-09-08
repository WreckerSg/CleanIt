# Manual básico de usuario de CleanIt

## 1. Estado de esta versión

Este manual corresponde a la versión candidata **1.0.0**. Actualmente funcionan:

- inicio de sesión;
- rechazo de credenciales incorrectas y cuentas inactivas;
- cierre de sesión seguro mediante una solicitud `POST`;
- panel inicial para participantes;
- panel inicial para administradores;
- administración de cuentas mediante el panel de Django para usuarios autorizados;
- creación, consulta, edición y desactivación de zonas;
- creación, consulta, edición y retiro lógico de tareas;
- asignación de responsable, frecuencia y próxima fecha.
- consulta de tareas pendientes por responsable;
- registro de cumplimiento con observación opcional;
- cálculo de próxima fecha para tareas recurrentes;
- consulta del historial según el rol.

Las funciones de pendientes, cumplimiento e historial están disponibles y cubiertas por la suite de regresión.

## 2. Perfiles de usuario

| Perfil | Funciones disponibles en 2.3 |
|---|---|
| Administrador | Iniciar sesión, administrar cuentas autorizadas, zonas y tareas |
| Participante | Iniciar sesión, consultar pendientes, registrar cumplimientos, revisar su historial y cerrar sesión |

El rol funcional y el permiso de acceso al panel técnico son controles distintos. Un usuario con rol **Administrador** solo podrá abrir `/admin/` si además tiene habilitado el atributo de personal de Django.

## 3. Requisitos para acceder

- Aplicación iniciada por el responsable técnico.
- Navegador web actualizado.
- Usuario y contraseña creados por un administrador.
- Dirección local predeterminada: `http://127.0.0.1:8000/`; puede utilizar otro puerto disponible, como `8081`.

No comparta su contraseña ni la almacene en documentos del repositorio.

## 4. Iniciar sesión

1. Abra la dirección indicada por el responsable técnico, por ejemplo `http://127.0.0.1:8081/`.
2. El sistema lo redirigirá a **Iniciar sesión**.
3. Escriba su nombre de usuario.
4. Escriba su contraseña.
5. Seleccione **Ingresar**.

Si las credenciales son válidas y la cuenta está activa, se mostrará el panel principal. Si existe un error, aparecerá el mensaje **El usuario o la contraseña no son correctos** sin revelar cuál dato falló.

## 5. Panel del participante

Después de ingresar, el participante verá:

- su nombre de usuario o nombre personal;
- la insignia **Participante**;
- las tarjetas de pendientes, cumplimiento e historial;
- el botón **Cerrar sesión**.

Las tarjetas **Mis tareas pendientes**, **Registrar cumplimiento** e **Historial** permiten abrir las funciones correspondientes. El participante no verá **Administrar usuarios**, **Gestionar tareas** ni **Gestionar zonas**.

## 6. Panel del administrador

El administrador verá las opciones generales y las tarjetas **Gestionar tareas**, **Gestionar zonas** y **Administrar usuarios**.

Si su cuenta tiene permiso de personal:

1. Seleccione **Abrir administración**.
2. Ingrese a la sección **Usuarios**.
3. Cree o edite una cuenta.
4. Asigne el rol **Administrador** o **Participante**.
5. Mantenga la cuenta activa para permitir el ingreso.
6. Guarde los cambios.

No elimine una cuenta con información histórica. Cuando exista ese historial, la operación correcta será desactivarla.

## 7. Gestionar zonas

### Crear una zona

1. Ingrese como administrador.
2. Seleccione **Abrir zonas**.
3. Seleccione **Nueva zona**.
4. Escriba un nombre único, por ejemplo `Cocina`.
5. Agregue una descripción opcional.
6. Seleccione **Guardar**.

### Editar o desactivar una zona

Desde el listado seleccione **Editar** para cambiar el nombre o la descripción. Seleccione **Desactivar** cuando el espacio deje de utilizarse. El sistema rechazará la desactivación si la zona todavía contiene tareas activas; primero deberá retirar o mover esas tareas.

## 8. Gestionar tareas

### Crear una tarea

1. Desde el panel seleccione **Abrir tareas**.
2. Seleccione **Nueva tarea**.
3. Ingrese un nombre claro, por ejemplo `Trapear el piso`.
4. Agregue una descripción opcional.
5. Seleccione una zona activa.
6. Seleccione un responsable activo.
7. Defina la frecuencia: única, diaria, semanal o mensual.
8. Indique la próxima fecha.
9. Seleccione **Guardar**.

La zona debe crearse antes de registrar la tarea. Una cuenta inactiva no puede seleccionarse como responsable.

### Editar o retirar una tarea

Desde el listado seleccione **Editar** para modificar sus datos. Utilice **Retirar** cuando la actividad deje de ser necesaria. El retiro es lógico: la tarea queda inactiva y sus datos permanecen disponibles para el historial futuro.

## 9. Consultar pendientes y registrar cumplimiento

### Consultar tareas pendientes

1. Ingrese con la cuenta del responsable asignado.
2. En el panel seleccione **Mis tareas pendientes**.
3. Revise el nombre, la zona, la frecuencia y la próxima fecha.
4. Si lo necesita, filtre por zona o por estado pendiente/vencido.
5. Seleccione **Completar** en la actividad que haya realizado.

Solo aparecen tareas activas asignadas a la cuenta autenticada. Las tareas retiradas y las tareas únicas ya completadas no vuelven a aparecer como pendientes.

### Registrar cumplimiento

1. Revise el resumen de la actividad.
2. Escriba una observación opcional, por ejemplo `Se limpió completamente`.
3. Seleccione **Confirmar cumplimiento**.

El sistema conserva la tarea, la persona responsable, la fecha y hora del registro y la observación. En una tarea diaria, semanal o mensual se calcula automáticamente la próxima fecha. Una tarea única sale de la lista de pendientes después de completarse.

## 10. Consultar el historial

1. En el panel seleccione **Historial**.
2. Revise la tarea, zona, responsable, fecha programada, fecha de cumplimiento y observación.
3. Filtre por zona o rango de fechas; el administrador también puede filtrar por responsable.

Un participante solo consulta sus propios cumplimientos. El administrador puede consultar los cumplimientos de todo el equipo.

## 11. Cerrar sesión

1. Seleccione **Cerrar sesión** en el encabezado.
2. Compruebe que el sistema regrese a la página de acceso.
3. En un dispositivo compartido, cierre también el navegador.

Después de cerrar sesión no se podrá volver al panel sin autenticarse nuevamente.

## 12. Mensajes y situaciones frecuentes

| Situación | Causa probable | Acción recomendada |
|---|---|---|
| Usuario o contraseña incorrectos | Datos inválidos o cuenta inactiva | Revise los datos una vez y contacte al administrador si persiste |
| Redirección a la página de acceso | No existe una sesión activa | Inicie sesión con una cuenta válida |
| No aparece Administrar usuarios | La cuenta es participante | Solicite al responsable que verifique el rol |
| Aparece la tarjeta, pero no el botón de administración | El rol es administrador, pero no tiene permiso de personal | El superusuario debe revisar `is_staff` |
| La zona ya existe | El nombre debe ser único | Utilice la zona existente o cambie el nombre |
| No aparece una zona o responsable | El registro está inactivo | Active el registro correcto o seleccione otro |
| No se puede desactivar una zona | Todavía contiene tareas activas | Retire o cambie de zona esas tareas |
| La aplicación no abre | El servidor no está iniciado o usa otro puerto | Contacte al responsable técnico |
| No aparece una tarea pendiente | No está asignada a la cuenta, está retirada o ya fue completada | Consulte al administrador o revise el historial |
| La próxima fecha cambió | Se registró un cumplimiento de una tarea recurrente | Compruebe la nueva fecha calculada |

## 13. Mejoras posteriores al MVP

Las notificaciones, la recuperación de contraseña por correo, las múltiples sedes y la aplicación móvil no forman parte de la versión 1.0.0. Cualquier incorporación deberá registrarse, priorizarse y pasar nuevamente por las cuatro ramas.

El manual se ampliará únicamente después de comprobar cada función.
