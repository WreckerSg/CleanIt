# Validación real de Docker, PostgreSQL y dispositivo móvil

## Identificación

| Campo | Valor |
|---|---|
| Versión | 1.0.1 |
| Fecha | 9 de septiembre de 2026 |
| Ambiente | Windows, Docker Desktop y red Wi-Fi local |
| Aplicación | Django con Gunicorn y WhiteNoise |
| Base de datos | PostgreSQL 16 en contenedor |
| Datos | Registros ficticios de prueba |

## PSN-03 - Compatibilidad móvil

Se accedió desde un teléfono conectado a la misma red Wi-Fi del computador. El
recorrido incluyó inicio de sesión, consulta de pendientes, registro de
cumplimiento, consulta del historial y cierre de sesión.

Resultado informado por el ejecutor:

- los recorridos principales se completaron sin bloqueo;
- los controles permanecieron accesibles;
- no se observó desbordamiento que impidiera operar;
- el registro realizado desde el teléfono quedó visible en el historial.

La ejecución aprueba la compatibilidad móvil requerida para el alcance académico
del MVP. Una investigación de usabilidad con una muestra mayor puede realizarse
como mejora posterior, pero no bloquea la entrega.

## PSN-06 - Respaldo y restauración de PostgreSQL

El ambiente se inició con los servicios `web` y `db` saludables. Se generó un
respaldo con `pg_dump`, se copió fuera del contenedor y se restauró en la base
aislada `cleanit_restore_test`.

Resultado informado por el ejecutor:

- el respaldo terminó sin errores;
- la restauración terminó sin reemplazar la base principal;
- las tablas de usuarios, tareas y cumplimientos quedaron disponibles;
- los conteos consultados coincidieron con el origen;
- CleanIt continuó funcionando sobre PostgreSQL después de la validación.

## Verificación adicional de interfaz

Se corrigió la entrega de archivos estáticos bajo Gunicorn mediante WhiteNoise y
`collectstatic`. La ruta `/static/css/cleanit.css` respondió correctamente y la
interfaz gráfica se visualizó desde el contenedor. El puerto del equipo se
configura mediante `WEB_PORT`; el servicio conserva el puerto interno `8000`.

## Decisión

Los casos **PSN-03** y **PSN-06** quedan aprobados para la versión 1.0.1. Las
pruebas PSN-04 y PSN-05 continúan condicionadas porque requieren generación de
carga y un ambiente descartable de estrés.
