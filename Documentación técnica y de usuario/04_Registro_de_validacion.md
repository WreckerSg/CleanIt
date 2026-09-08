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
| Ambiente de desarrollo | Python 3.12, Django 5.2.17 y SQLite |
| Pruebas automatizadas | 18 ejecutadas, 18 aprobadas, 0 fallidas |
| Comprobación de Django | 0 problemas |
| Migraciones | Sin cambios pendientes |
| Validación en Windows | Pendiente después de actualizar `dev` |

La aceptación de este incremento requiere repetir las pruebas en Windows y crear al menos una zona y una tarea con datos ficticios.
