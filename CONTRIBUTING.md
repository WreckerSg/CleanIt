# Guía de contribución

## Flujo de trabajo

1. Seleccionar en Jira una historia, tarea o defecto listo para iniciar.
2. Crear una rama desde `develop` usando la clave de Jira.
3. Realizar cambios pequeños y verificables.
4. Ejecutar las pruebas relacionadas cuando exista código.
5. Abrir un pull request hacia `develop`.
6. Solicitar revisión y resolver observaciones.
7. Integrar solo cuando se cumpla la definición de terminado.

## Nombres de ramas

```text
feature/SCRUM-17-crear-tareas
fix/SCRUM-19-corregir-recurrencia
docs/SCRUM-35-manual-usuario
test/SCRUM-33-pruebas-integración
```

## Mensajes de commit

Usar la clave de Jira y un verbo en presente:

```text
SCRUM-17 agrega formulario de creación de tareas
SCRUM-19 válida la frecuencia mensual
SCRUM-35 documenta el procedimiento de respaldo
```

## Pull requests

Cada solicitud debe incluir:

- problema o historia relacionada;
- resumen del cambio;
- forma de validarlo;
- pruebas realizadas o razón por la cual no aplican;
- capturas cuando cambie la interfaz;
- riesgos y consideraciones de despliegue.

## Definición de terminado

Un elemento puede pasar a `Done` cuando:

- cumple los criterios de aceptación;
- fue revisado por otra persona cuando el equipo lo permita;
- supera las pruebas aplicables;
- no introduce defectos críticos ni altos conocidos;
- actualiza la documentación relacionada;
- no pública claves, contraseñas ni datos personales;
- queda vinculado con Jira mediante su clave.
