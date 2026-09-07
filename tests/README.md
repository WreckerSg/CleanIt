# Pruebas automatizadas

Esta carpeta se utilizará cuando comience la implementación. Se propone separar las pruebas en:

```text
tests/
|-- unit/           # Modelos, validaciones y cálculo de frecuencias
|-- integration/    # Formularios, vistas, ORM y PostgreSQL
|-- functional/     # Flujos completos por rol
`-- security/       # Autenticación, autorización y entradas maliciosas
```

Los casos diseñados antes de la implementación se encuentran en el [`Modelo de casos de prueba`](../Plan%20de%20pruebas/04_Modelo_de_casos_de_prueba.md). Los resultados actuales son simulados y no corresponden a la ejecución de una suite automatizada.

Cuando exista código, las pruebas se crearán inicialmente desde `dev`, se ejecutarán formalmente en `qa` y se repetirán como regresión en `pre-main` antes de promover una versión a `main`.
