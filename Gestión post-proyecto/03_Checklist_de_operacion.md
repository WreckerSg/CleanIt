# Checklist de operación y soporte

## Diario

- [ ] La aplicación responde.
- [ ] No existen errores críticos nuevos.
- [ ] El respaldo programado finalizó correctamente.
- [ ] No se publicaron secretos ni datos personales en reportes.

## Semanal

- [ ] Las incidencias están clasificadas y tienen responsable.
- [ ] Los casos P1 y P2 cumplen el tiempo objetivo o tienen plan documentado.
- [ ] Se revisaron errores repetidos y tareas vencidas.
- [ ] Las cuentas que ya no se utilizan fueron desactivadas.

## Mensual

- [ ] Se restauró una copia en un ambiente aislado.
- [ ] Se revisaron dependencias y avisos de seguridad.
- [ ] Se verificaron permisos y accesos administrativos.
- [ ] Se revisaron capacidad, tiempos de respuesta y almacenamiento.
- [ ] Se actualizaron preguntas frecuentes y documentación.

## Antes de cada versión

- [ ] Todas las migraciones están versionadas.
- [ ] La suite automatizada está aprobada.
- [ ] `python manage.py check` no reporta problemas.
- [ ] `python manage.py check --deploy` fue ejecutado con variables de producción.
- [ ] El cambio avanzó por `dev`, `qa` y `pre-main`.
- [ ] El manual, la documentación técnica y el changelog están actualizados.
- [ ] Existe un procedimiento de reversa y un respaldo previo.
- [ ] No quedan defectos críticos ni altos abiertos.
- [ ] La versión fue aceptada antes de actualizar `main`.
