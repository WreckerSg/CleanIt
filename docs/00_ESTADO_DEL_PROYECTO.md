# Estado del proyecto y alcance de la evidencia

## Estado actual

El **Paso 1 fue aceptado**. Los incrementos 2.1 y 2.2 fueron validados en Windows. La versión 1.0.1 completa el MVP con pendientes, cumplimiento, recurrencias, filtros e historial, supera treinta y ocho pruebas automatizadas y fue comprobada con Docker, PostgreSQL y un dispositivo móvil.

El producto mínimo viable está completo como versión estable del repositorio, pero todavía no está desplegado públicamente. En consecuencia:

- el manual del Paso 2 describe las funciones disponibles y separa las mejoras futuras;
- treinta y ocho verificaciones automatizadas se ejecutan sobre software real;
- las evidencias y métricas conservadas dentro del Paso 1 siguen siendo simulaciones académicas históricas;
- las evidencias reales se conservan separadas de las simulaciones históricas;
- la presencia en `main` identifica una versión estable del repositorio, no un servicio público desplegado.

## Propósito de la simulación

La actividad solicita evidencias simuladas. Estas se utilizan para mostrar cómo se registrarían las ejecuciones, los defectos, las correcciones y los resultados una vez exista el producto. La simulación permite evaluar la calidad del plan sin ocultar el estado real del desarrollo.

## Criterio para generar evidencia real

Para cada incremento que llegue a `qa` se deberá:

1. crear un ambiente de pruebas independiente;
2. ejecutar los casos con datos controlados;
3. guardar la fecha, versión, responsable y resultado real;
4. anexar capturas o salidas generadas por las herramientas;
5. abrir en GitHub los defectos encontrados;
6. reemplazar los archivos simulados por evidencias reales sin alterar el historial de Git.

## Control de cambios

| Versión documental | Estado | Descripción |
|---|---|---|
| 0.1 | Planificación | Alcance, riesgos, Scrum, Jira y stack definidos. |
| 0.2 | Entrega final documental | Plan de pruebas, manual, documentación técnica y gestión postproyecto. |
| 0.3 | En desarrollo | Base navegable y primeras pruebas automatizadas reales. |
| 1.0 | Estable | Producto mínimo viable aceptado en el repositorio; despliegue público pendiente. |
