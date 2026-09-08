# Registro de validación de los incrementos

## Incremento 2.1

| Campo | Resultado |
|---|---|
| Versión | Rama `dev`, posterior a la corrección de rol del superusuario |
| Fecha | 8 de septiembre de 2026 |
| Ambiente | Windows, entorno virtual nativo, SQLite, Google Chrome, puerto local 8081 |
| Ejecutor | Autor del proyecto |
| Pruebas automatizadas | 8 ejecutadas, 8 aprobadas, 0 fallidas |
| Comprobación de Django | 0 problemas |

### Recorridos manuales aprobados

- La página privada redirige al inicio de sesión.
- El superusuario inicia sesión y aparece como **Administrador**.
- El administrador visualiza el acceso a la administración de cuentas.
- Se crea la cuenta ficticia `participante1` con rol Participante.
- El participante inicia sesión y aparece como **Participante**.
- El participante no visualiza la administración de usuarios.

Las capturas se revisaron durante la validación, pero no se publican porque incluyen elementos ajenos a la aplicación en la barra del navegador.

## Incremento 2.2

| Campo | Resultado actual |
|---|---|
| Ambiente de desarrollo | Python 3.10 o superior, Django 5.2.17 y SQLite |
| Pruebas automatizadas | 18 ejecutadas, 18 aprobadas, 0 fallidas |
| Comprobación de Django | 0 problemas |
| Migraciones | Sin cambios pendientes |
| Validación en Windows | Aprobada con recorrido manual |

### Recorridos manuales aprobados

- Se creó la zona ficticia `Cocina` y quedó activa.
- Se creó la tarea `Limpiar la cocina` asignada a `participante1`, con frecuencia semanal.
- Se editó la descripción de la tarea y el cambio quedó visible.
- Se impidió desactivar `Cocina` mientras contenía una tarea activa.
- Se retiró lógicamente la tarea y permaneció visible con estado `Retirada`.

## Incremento 2.3

| Campo | Resultado actual |
|---|---|
| Ambiente de desarrollo | Python 3.10 o superior, Django 5.2.17 y SQLite |
| Pruebas automatizadas | 38 ejecutadas, 38 aprobadas, 0 fallidas |
| Comprobación de Django | 0 problemas |
| Comprobación de despliegue | 0 problemas con variables de producción |
| Dependencias | Sin requisitos rotos según `pip check` |
| Migraciones | `chores.0002_completion` y `chores.0003_*` aplicadas |
| Validación funcional | Cubierta por pruebas de vistas, modelos, permisos y filtros |

La ejecución cubre una tarea activa asignada, pendientes aislados por participante, cumplimiento con observación, próxima fecha, prevención de duplicados, historial por rol y filtros. La prueba visual final puede repetirse en Windows como demostración, sin ser una condición para reproducir la suite automatizada.
