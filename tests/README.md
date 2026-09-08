# Pruebas automatizadas

La implementación ya cuenta con pruebas de modelos, autenticación, acceso y presentación por rol dentro de cada aplicación Django. Ejecútelas desde la raíz con:

```bash
python manage.py test
```

Cuando crezca la suite, se separará en:

```text
tests/
|-- unit/           # Modelos, validaciones y cálculo de frecuencias
|-- integration/    # Formularios, vistas, ORM y PostgreSQL
|-- functional/     # Flujos completos por rol
`-- security/       # Autenticación, autorización y entradas maliciosas
```

Los casos diseñados antes de la implementación se encuentran en el [`Modelo de casos de prueba`](../Plan%20de%20pruebas/04_Modelo_de_casos_de_prueba.md). Las evidencias del Paso 1 continúan identificadas como simuladas; no deben confundirse con la salida de la suite actual.

Las pruebas se crean inicialmente desde `dev`, se ejecutan formalmente en `qa` y se repiten como regresión en `pre-main` antes de promover una versión a `main`.
