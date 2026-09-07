# Definiciones y fundamentos de calidad

## 1. Propósito

Establecer el lenguaje común utilizado en el plan de pruebas de CleanIt. Las definiciones se adaptan al proyecto y se apoyan en los cuatro temas de la Unidad 3 y en la plantilla académica de casos funcionales y no funcionales proporcionada para la actividad.

## 2. Calidad, verificación y validación

**Calidad de software:** grado en que el producto satisface los requisitos acordados y las necesidades de sus usuarios. Para que un atributo pueda evaluarse debe expresarse mediante condiciones observables y, cuando corresponda, métricas.

**Aseguramiento de la calidad:** conjunto planificado de actividades aplicadas al proceso, los documentos, los componentes intermedios y el producto final para aumentar la confianza en su calidad.

**Verificación:** determina si un artefacto fue construido de acuerdo con su especificación. En CleanIt incluye revisar historias, criterios de aceptación, diseño, modelos, código futuro y documentación.

**Validación:** determina si el comportamiento del producto satisface la necesidad real del usuario. Incluye recorridos completos, usabilidad y aceptación. Las pruebas aumentan la probabilidad de detectar problemas, pero no garantizan la ausencia total de defectos.

## 3. Elementos del proceso de prueba

| Concepto | Aplicación en CleanIt |
|---|---|
| Base de prueba | Historias SCRUM-15 a SCRUM-23, criterios de aceptación, riesgos, arquitectura y reglas del negocio |
| Caso de prueba | Condiciones, datos, pasos y resultado esperado para verificar un comportamiento específico |
| Procedimiento | Secuencia reproducible para preparar, ejecutar y cerrar una prueba |
| Dato de prueba | Usuario, tarea, frecuencia, fecha o permiso ficticio utilizado durante la ejecución |
| Resultado esperado | Comportamiento definido antes de ejecutar la prueba |
| Resultado observado | Comportamiento realmente obtenido durante una ejecución identificada |
| Evidencia | Registro, captura, salida, métrica o enlace que permite comprobar el resultado observado |
| Defecto | Diferencia reproducible entre el resultado esperado y el observado |
| Reprueba | Ejecución del caso que falló después de aplicar una corrección |
| Regresión | Reejecución de casos relacionados para detectar efectos secundarios |

## 4. Niveles y tipos de prueba

### 4.1 Pruebas unitarias

Verifican de forma aislada una regla o unidad pequeña. Para CleanIt se enfocarán en validaciones de tareas, responsables, fechas y cálculo de recurrencias. Se prevé automatizarlas con las herramientas de prueba de Django.

### 4.2 Pruebas de integración

Comprueban la interacción entre formularios, vistas, servicios, Django ORM y PostgreSQL. La integración se considera incorrecta si aparece un error grave que comprometa seguridad, persistencia o trazabilidad; en ese caso el cambio no debe avanzar de rama.

### 4.3 Pruebas del sistema

Evalúan CleanIt como un conjunto mediante recorridos completos por rol: autenticarse, administrar personas, crear y asignar tareas, consultar pendientes, completar actividades y revisar el historial.

### 4.4 Pruebas de aceptación

Confirman con el Product Owner que el incremento satisface los criterios acordados y puede promoverse a `main`. No sustituyen las pruebas técnicas anteriores.

### 4.5 Pruebas no funcionales

- **Seguridad:** autenticación, autorización, protección CSRF, sesiones y datos sensibles.
- **Usabilidad y adaptabilidad:** claridad de los recorridos y funcionamiento en tamaños móviles.
- **Rendimiento:** tiempos de respuesta y tasa de errores bajo la carga objetivo.
- **Estrés:** comportamiento al superar gradualmente la carga prevista y capacidad de recuperación.
- **Recuperación:** restauración de respaldos y conservación de relaciones y conteos.
- **Compatibilidad:** ejecución en navegadores y resoluciones definidas.

### 4.6 Pruebas documentales

Verifican formato, completitud, correctitud, trazabilidad y facilidad de comprensión del plan, el manual y la documentación técnica, tal como propone la plantilla suministrada.

## 5. Requisitos funcionales y no funcionales

**Requisito funcional:** expresa una capacidad o regla de negocio, por ejemplo asignar una tarea a una persona activa o registrar una actividad completada.

**Requisito no funcional:** expresa una condición de calidad o restricción, por ejemplo impedir accesos por fuera del rol, responder dentro del umbral establecido o adaptarse a una pantalla de 360 px.

## 6. Atributos de calidad utilizados

El material académico presenta los seis atributos de ISO/IEC 9126. En este plan se utilizan como marco de clasificación, no como declaración de certificación.

| Atributo | Interpretación para CleanIt | Ejemplo de verificación |
|---|---|---|
| Funcionalidad | Las operaciones responden a las historias y reglas definidas | Crear, asignar y completar tareas |
| Fiabilidad | Los datos y estados permanecen consistentes ante errores o repeticiones | Evitar doble registro y restaurar respaldos |
| Usabilidad | El usuario entiende y completa los flujos principales | Recorrido móvil sin ayuda |
| Eficiencia | La aplicación responde dentro de los objetivos de carga | Tiempo p95 y tasa de error |
| Mantenibilidad | Los cambios pueden probarse y rastrearse de forma controlada | Pruebas unitarias, ramas y trazabilidad |
| Portabilidad | El ambiente puede reproducirse en configuraciones definidas | Docker Compose y navegadores compatibles |

## 7. Métricas

**Métrica de proceso:** mide la eficacia del trabajo utilizado para construir y verificar el producto, como tiempo medio de corrección o porcentaje de casos ejecutados.

**Métrica de producto:** mide atributos del software o de sus representaciones.

- **Estática:** se obtiene sin ejecutar el programa, por ejemplo cobertura de requisitos en el diseño de casos o completitud documental.
- **Dinámica:** se obtiene durante la ejecución, por ejemplo tiempo de respuesta, errores bajo carga o defectos encontrados.

En la fase actual solo pueden informarse como reales las métricas estáticas del material diseñado. Las métricas dinámicas de esta entrega están expresamente identificadas como simuladas.

## 8. Fuentes académicas utilizadas

- Unidad 3, Tema 1: *Normas y modelos de la calidad del software*.
- Unidad 3, Tema 2: *Métricas del software*.
- Unidad 3, Tema 3: *Métodos de prueba apropiados para evaluar el software*.
- Unidad 3, Tema 4: *Plan de pruebas*.
- Plantilla: *Modelo de Casos de Prueba - requerimientos funcionales y no funcionales*.

Estos materiales fueron proporcionados como apoyo de la actividad. Su contenido fue sintetizado y aplicado al contexto de CleanIt.

