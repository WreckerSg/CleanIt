# Evidencias reales de la versión 1.0.1

Esta carpeta reúne resultados obtenidos sobre la aplicación ejecutable. Se mantiene separada de `evidencias-simuladas/` para no mezclar mediciones reales con el escenario académico inicial.

## Identificación

| Campo | Valor |
|---|---|
| Versión | 1.0.1 |
| Fecha | 9 de septiembre de 2026 |
| Framework | Django 5.2.17 LTS |
| Base de pruebas | SQLite aislada creada por Django |
| Herramienta | `django.test` y comprobaciones de administración |
| Datos | Exclusivamente ficticios |

## Resultados

| Evidencia | Resultado |
|---|---|
| [Ejecución automatizada](01_Ejecucion_automatizada.md) | 38 de 38 pruebas aprobadas |
| [Matriz de resultados](02_Matriz_de_resultados.md) | 28 de 28 casos ejecutados aprobados; 2 condicionados por ambiente |
| [Validación manual](03_Validacion_manual.md) | Acceso, roles, zonas y tareas comprobados en Windows |
| [Docker, PostgreSQL y móvil](04_Validacion_Docker_PostgreSQL_y_movil.md) | Interfaz, recorrido móvil, respaldo y restauración aprobados |

## Decisión

La versión cumple los criterios para promoción académica por `dev`, `qa`, `pre-main` y `main`: no existen fallos automatizados ni problemas de configuración conocidos. Esta decisión autoriza una versión estable del repositorio, no equivale a un despliegue público.

La compatibilidad móvil y la restauración de PostgreSQL fueron comprobadas en un
host con Docker y un teléfono real. Las pruebas de carga y estrés permanecen
condicionadas a un generador de carga y un ambiente descartable; no se presentan
como aprobadas.
