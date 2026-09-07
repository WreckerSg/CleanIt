# Métricas de calidad y criterios de interpretación

## 1. Enfoque

El material académico diferencia métricas del proceso y del producto, además de métricas estáticas y dinámicas. CleanIt conserva esa distinción para evitar presentar datos simulados como mediciones reales.

## 2. Métricas disponibles en la fase actual

| Métrica estática | Fórmula | Resultado actual |
|---|---|---:|
| Cobertura de historias en el diseño | Historias con casos / historias totales x 100 | 9 / 9 = 100 % |
| Completitud de casos | Casos con campos obligatorios / casos diseñados x 100 | 30 / 30 = 100 % |
| Trazabilidad de casos | Casos con requisito o propósito identificado / total x 100 | 30 / 30 = 100 % |

Estos valores miden los artefactos de planificación, no la calidad de un programa ejecutable.

## 3. Métricas de ejecución futuras

| Métrica | Fórmula | Meta o regla |
|---|---|---|
| Progreso de ejecución | Casos ejecutados / casos aplicables x 100 | 100 % de críticos y altos |
| Tasa de aprobación | Casos aprobados / casos ejecutados x 100 | >= 95 % para salir de `qa` |
| Tasa de fallos | Casos fallidos / casos ejecutados x 100 | Informativa; analizar por severidad |
| Cobertura de requisitos ejecutada | Requisitos con al menos un caso aprobado / requisitos aplicables x 100 | 100 % |
| Efectividad de corrección | Defectos cerrados y reprobados / defectos corregidos x 100 | 100 % antes de `main` |
| Reapertura | Defectos reabiertos / defectos cerrados x 100 | Tendencia descendente |
| Tiempo medio de corrección | Suma del tiempo de resolución / defectos resueltos | Analizar por severidad |
| Éxito de restauración | Comprobaciones correctas / comprobaciones críticas x 100 | 100 % |

## 4. Métricas dinámicas del producto

| Atributo | Indicador | Objetivo inicial |
|---|---|---|
| Eficiencia | Tiempo de respuesta p95 en operaciones principales | <= 2,0 s con carga objetivo |
| Fiabilidad | Tasa de errores HTTP o transacciones fallidas | < 1 % durante la carga objetivo |
| Usabilidad | Recorridos completados sin ayuda | >= 85 % |
| Usabilidad | Tiempo promedio de los cuatro recorridos | <= 3 minutos |
| Seguridad | Casos altos/críticos aprobados | 100 % antes de `main` |
| Recuperación | Entidades y relaciones críticas restauradas | 100 % |

Los objetivos son iniciales y deberán ajustarse con datos reales del MVP y acuerdos del Product Owner.

## 5. Severidad de defectos

| Indicador | Interpretación |
|---|---|
| Defectos críticos abiertos | La ejecución se suspende y la versión no avanza |
| Defectos altos abiertos | La versión no puede pasar a `pre-main` ni `main` |
| Defectos medios abiertos | Requieren tratamiento y decisión antes de producción |
| Defectos bajos abiertos | Pueden aceptarse con justificación y fecha de atención |

La cantidad total no debe interpretarse sin considerar severidad, componente, repetición y riesgo.

## 6. Resultados simulados de esta actividad

El escenario académico utiliza 30 casos:

- Ciclo 1 simulado: 25 aprobados y 5 fallidos; tasa de aprobación de 83,3 %.
- Ciclo 2 simulado: reprueba de los 5 defectos y regresión de 7 casos; todos aprobados.
- Consolidado hipotético: 30 de 30 aprobados.

Estos resultados demuestran el cálculo y la toma de decisión, pero **no son métricas obtenidas de CleanIt**. El valor real actual de casos ejecutados es 0.

## 7. Reglas de publicación

1. No publicar una métrica dinámica sin identificar commit, ambiente, fecha y herramienta.
2. No reemplazar la salida original por una transcripción manual cuando la herramienta pueda exportarla.
3. Separar siempre resultados reales, simulados y metas.
4. Conservar el dato base que permita recalcular porcentajes.
5. No incluir contraseñas, tokens ni datos personales en evidencias.

