# Estado del proyecto y alcance de la evidencia

## Estado actual

El **Paso 1 fue aceptado** y promovido a `main`. El incremento 2.1 fue validado en Windows con ocho pruebas aprobadas. El incremento 2.2 se encuentra en `dev` e incorpora zonas, tareas, responsables, frecuencias y dieciocho pruebas automatizadas.

El producto mínimo viable todavía no está completo ni desplegado. En consecuencia:

- el manual del Paso 2 distingue las funciones disponibles de las futuras;
- dieciocho verificaciones automatizadas se ejecutan sobre software real;
- las evidencias y métricas conservadas dentro del Paso 1 siguen siendo simulaciones académicas históricas;
- las evidencias reales formales se generarán al promover cada incremento a `qa`;
- ningún incremento debe considerarse productivo hasta avanzar por `qa`, `pre-main` y `main`.

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
| 1.0 | Futura | Producto mínimo viable aceptado y desplegado. |
