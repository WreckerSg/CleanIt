# Manual básico de usuario de CleanIt

## 1. Estado de esta versión

Este manual corresponde al incremento **2.1**, disponible inicialmente en la rama `dev`. Actualmente funcionan:

- inicio de sesión;
- rechazo de credenciales incorrectas y cuentas inactivas;
- cierre de sesión seguro mediante una solicitud `POST`;
- panel inicial para participantes;
- panel inicial para administradores;
- administración de cuentas mediante el panel de Django para usuarios autorizados.

Las tarjetas **Mis tareas pendientes**, **Registrar cumplimiento** e **Historial** muestran la etiqueta **Próximo incremento**. En la versión 2.1 todavía no ejecutan esos procesos.

## 2. Perfiles de usuario

| Perfil | Funciones disponibles en 2.1 |
|---|---|
| Administrador | Iniciar sesión, consultar su panel y, si posee permiso de personal, abrir la administración de cuentas |
| Participante | Iniciar sesión, consultar su panel personal y cerrar sesión |

El rol funcional y el permiso de acceso al panel técnico son controles distintos. Un usuario con rol **Administrador** solo podrá abrir `/admin/` si además tiene habilitado el atributo de personal de Django.

## 3. Requisitos para acceder

- Aplicación iniciada por el responsable técnico.
- Navegador web actualizado.
- Usuario y contraseña creados por un administrador.
- Dirección local predeterminada: `http://127.0.0.1:8000/`.

No comparta su contraseña ni la almacene en documentos del repositorio.

## 4. Iniciar sesión

1. Abra `http://127.0.0.1:8000/`.
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

En el incremento 2.1 las tres tarjetas anuncian funciones en preparación. El participante no verá la opción **Administrar usuarios**.

## 6. Panel del administrador

El administrador verá las opciones generales y la tarjeta **Administrar usuarios**.

Si su cuenta tiene permiso de personal:

1. Seleccione **Abrir administración**.
2. Ingrese a la sección **Usuarios**.
3. Cree o edite una cuenta.
4. Asigne el rol **Administrador** o **Participante**.
5. Mantenga la cuenta activa para permitir el ingreso.
6. Guarde los cambios.

No elimine una cuenta con información histórica. Cuando exista ese historial, la operación correcta será desactivarla.

## 7. Cerrar sesión

1. Seleccione **Cerrar sesión** en el encabezado.
2. Compruebe que el sistema regrese a la página de acceso.
3. En un dispositivo compartido, cierre también el navegador.

Después de cerrar sesión no se podrá volver al panel sin autenticarse nuevamente.

## 8. Mensajes y situaciones frecuentes

| Situación | Causa probable | Acción recomendada |
|---|---|---|
| Usuario o contraseña incorrectos | Datos inválidos o cuenta inactiva | Revise los datos una vez y contacte al administrador si persiste |
| Redirección a la página de acceso | No existe una sesión activa | Inicie sesión con una cuenta válida |
| No aparece Administrar usuarios | La cuenta es participante | Solicite al responsable que verifique el rol |
| Aparece la tarjeta, pero no el botón de administración | El rol es administrador, pero no tiene permiso de personal | El superusuario debe revisar `is_staff` |
| La aplicación no abre | El servidor no está iniciado o usa otro puerto | Contacte al responsable técnico |

## 9. Funciones que se añadirán

Los siguientes incrementos incorporarán, en este orden:

1. personas, zonas y tareas de limpieza;
2. responsables, frecuencias y fechas;
3. consulta de pendientes y vencimientos;
4. registro de cumplimiento e historial.

El manual se ampliará únicamente después de comprobar cada función.
