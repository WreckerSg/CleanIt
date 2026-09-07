# Matriz de trazabilidad de pruebas

## 1. Historias de usuario

| Jira | Necesidad | Casos asociados | Cobertura diseñada |
|---|---|---|---|
| SCRUM-15 | Registrar personas | PI-02, PSF-03, PSF-04 | Persistencia, flujo válido, obligatoriedad, formato y duplicidad |
| SCRUM-16 | Editar o desactivar personas | PI-02, PSF-05 | Edición, desactivación, acceso y conservación de relaciones |
| SCRUM-17 | Crear tareas | PU-01, PI-03, PSF-06 | Reglas de datos, persistencia y recorrido completo |
| SCRUM-18 | Editar o retirar tareas | PI-03, PSF-07 | Actualización y retiro lógico sin perder historial |
| SCRUM-19 | Definir frecuencia | PU-01, PU-03, PU-04, PI-05, PSF-08 | Catálogo, diaria, semanal, mensual y límites de calendario |
| SCRUM-20 | Asignar responsable | PU-02, PI-04, PSF-09 | Persona activa, rechazo de inactiva y persistencia |
| SCRUM-21 | Consultar pendientes | PU-05, PSF-10 | Estados, aislamiento, orden y vencimiento |
| SCRUM-22 | Marcar como completada | PI-05, PI-06, PSF-11 | Historial, siguiente fecha e idempotencia |
| SCRUM-23 | Consultar estado e historial | PI-03, PI-05, PSF-11, PSN-06 | Filtros, trazabilidad, integridad y restauración |

## 2. Acceso y requisitos no funcionales

| Requisito o riesgo | Casos asociados | Evidencia futura |
|---|---|---|
| Autenticación y cuenta inactiva | PI-01, PSF-01, PSF-02 | Respuesta, redirección y sesión |
| Acceso no autorizado | PI-01, PSF-10, PSN-01, PSN-02 | Matriz de permisos y solicitudes negativas |
| Frecuencia incorrecta | PU-03, PU-04, PI-05, PSF-08 | Fechas calculadas y aserciones unitarias |
| Falta de actualización | PI-05, PI-06, PSF-11 | Historial y prueba de duplicidad |
| Baja adopción | PSF-10, PSN-03 | Tasa de éxito, tiempos y observaciones anónimas |
| Rendimiento insuficiente | PSN-04, PSN-05 | Reporte original de carga y estrés |
| Pérdida de información | PI-03, PI-05, PI-06, PSN-06 | Restricciones, respaldo, restauración y conteos |
| Documentación incompleta | PD-01, PD-02 | Lista de comprobación y observaciones |

## 3. Atributos de calidad

| Atributo del marco académico | Casos principales |
|---|---|
| Funcionalidad | PSF-01 a PSF-11 |
| Fiabilidad | PU-04, PU-05, PI-05, PI-06, PSN-06 |
| Usabilidad | PSN-03 y PSF-10 |
| Eficiencia | PSN-04 y PSN-05 |
| Mantenibilidad | PU-01 a PU-05, PD-01 y PD-02 |
| Portabilidad | PSN-03 y la preparación reproducible del ambiente |

## 4. Estado de cobertura

| Indicador | Resultado actual |
|---|---:|
| Historias con al menos un caso | 9 de 9 (100 %) |
| Casos unitarios diseñados | 5 |
| Casos de integración diseñados | 6 |
| Casos funcionales del sistema diseñados | 11 |
| Casos no funcionales diseñados | 6 |
| Casos documentales diseñados | 2 |
| **Total de casos diseñados** | **30** |
| Casos ejecutados realmente | **0** |

La cobertura actual corresponde al **diseño**. Solo podrá hablarse de cobertura ejecutada cuando exista una versión funcional y evidencia asociada a un commit.

