# Pruebas automatizadas

Esta carpeta se utilizará cuando comience la implementación. Se propone separar las pruebas en:

```text
tests/
|-- unit/           # Modelos, validaciones y cálculo de frecuencias
|-- integration/    # Formularios, vistas, ORM y PostgreSQL
|-- functional/     # Flujos completos por rol
`-- security/       # Autenticación, autorización y entradas maliciosas
```

Los casos disenados antes de la implementación se encuentran en [`docs/02_CASOS_DE_PRUEBA.md`](../docs/02_CASOS_DE_PRUEBA.md). Los resultados actuales son simulados y no corresponden a la ejecución de una suite automatizada.
