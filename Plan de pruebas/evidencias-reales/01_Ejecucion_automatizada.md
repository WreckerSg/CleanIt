# Ejecución automatizada de la versión candidata

## Resultado consolidado

| Comprobación | Resultado real |
|---|---|
| `python manage.py test` | 38 pruebas ejecutadas, 38 aprobadas, 0 fallidas |
| `python manage.py check` | 0 problemas |
| `python manage.py makemigrations --check --dry-run` | No se detectaron migraciones pendientes |
| `python manage.py check --deploy` con variables de producción | 0 problemas |
| `python -m pip check` | No se detectaron requisitos rotos |
| `python -m compileall -q src manage.py` | Compilación sintáctica correcta |
| `git diff --check` | Sin errores de espacios o marcadores de conflicto |

Salida principal:

```text
Found 38 test(s).
System check identified no issues (0 silenced).
......................................
----------------------------------------------------------------------
Ran 38 tests

OK
Destroying test database for alias 'default'...
```

## Cobertura funcional observada

- autenticación válida, inválida e inactiva;
- roles, permisos administrativos y aislamiento por objeto;
- usuarios, zonas, tareas, responsables y retiro lógico;
- frecuencias diaria, semanal y mensual con año bisiesto;
- pendientes, vencimientos y filtros;
- cumplimiento único, observación, próxima fecha e historial;
- CSRF, configuración de producción y ausencia de migraciones pendientes.

## Limitación del ambiente

Docker no está instalado en el ambiente de ejecución utilizado. Por lo tanto, la configuración de Compose y PostgreSQL fue revisada como código, pero el arranque de contenedores y la restauración permanecen condicionados a un host con Docker.
