# Evidencias reales de la versión 1.0.0

Esta carpeta reúne resultados obtenidos sobre la aplicación ejecutable. Se mantiene separada de `evidencias-simuladas/` para no mezclar mediciones reales con el escenario académico inicial.

## Identificación

| Campo | Valor |
|---|---|
| Versión | Candidata 1.0.0 |
| Fecha | 8 de septiembre de 2026 |
| Framework | Django 5.2.17 LTS |
| Base de pruebas | SQLite aislada creada por Django |
| Herramienta | `django.test` y comprobaciones de administración |
| Datos | Exclusivamente ficticios |

## Resultados

| Evidencia | Resultado |
|---|---|
| [Ejecución automatizada](01_Ejecucion_automatizada.md) | 38 de 38 pruebas aprobadas |
| [Matriz de resultados](02_Matriz_de_resultados.md) | 26 de 26 casos aplicables aprobados; 4 condicionados por ambiente |
| [Validación manual](03_Validacion_manual.md) | Acceso, roles, zonas y tareas comprobados en Windows |

## Decisión

La versión cumple los criterios para promoción académica por `dev`, `qa`, `pre-main` y `main`: no existen fallos automatizados ni problemas de configuración conocidos. Esta decisión autoriza una versión estable del repositorio, no equivale a un despliegue público.

Las pruebas de usabilidad móvil formal, carga, estrés y restauración de PostgreSQL permanecen condicionadas a un host con navegador móvil, generador de carga y Docker/PostgreSQL. No se presentan como aprobadas.
