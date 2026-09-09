# Matriz de resultados reales

## Casos aplicables al ambiente local

| Caso | Resultado | Evidencia principal |
|---|---|---|
| PU-01 | Aprobado | Formularios obligatorios y opciones controladas |
| PU-02 | Aprobado | Rechazo de responsable inactivo |
| PU-03 | Aprobado | Recurrencia diaria y semanal |
| PU-04 | Aprobado | Día ancla y año bisiesto |
| PU-05 | Aprobado | Estado pendiente y vencido |
| PI-01 | Aprobado | Autenticación, sesión y permisos |
| PI-02 | Aprobado | Edición y desactivación conservan la identidad |
| PI-03 | Aprobado | Creación, edición y retiro lógico |
| PI-04 | Aprobado | Asignación limitada a cuentas activas |
| PI-05 | Aprobado | Cumplimiento transaccional y próxima fecha |
| PI-06 | Aprobado | Envío repetido y restricción de unicidad |
| PSF-01 | Aprobado | Inicio de sesión válido |
| PSF-02 | Aprobado | Credenciales inválidas e inactivas rechazadas |
| PSF-03 | Aprobado | Creación de participante validada en Windows |
| PSF-04 | Aprobado | Correo duplicado y campos inválidos rechazados |
| PSF-05 | Aprobado | Edición y desactivación sin cambiar identidad |
| PSF-06 | Aprobado | Creación de tarea desde formulario |
| PSF-07 | Aprobado | Edición y retiro conservan el registro |
| PSF-08 | Aprobado | Frecuencias única, diaria, semanal y mensual |
| PSF-09 | Aprobado | Responsable activo y rechazo de inactivo |
| PSF-10 | Aprobado | Pendientes propios, orden y vencimiento textual |
| PSF-11 | Aprobado | Cumplimiento e historial filtrable |
| PSN-01 | Aprobado | Autorización por rol y por objeto |
| PSN-02 | Aprobado | CSRF, validación, secretos externos y `check --deploy` |
| PSN-03 | Aprobado | Recorridos principales completados en un teléfono por Wi-Fi |
| PSN-06 | Aprobado | Respaldo y restauración aislada de PostgreSQL mediante Docker |
| PD-01 | Aprobado | Plan, cifras, trazabilidad y separación de evidencias revisados |
| PD-02 | Aprobado | Manual y documentación sincronizados con el código |

Resultado aplicable: **28 aprobados de 28 ejecutados; tasa de aprobación 100 %**.

## Casos condicionados

| Caso | Estado | Condición pendiente |
|---|---|---|
| PSN-04 | Condicionado | Generador de carga con 50 usuarios durante 10 minutos |
| PSN-05 | Condicionado | Ambiente aislado para estrés y recuperación |

Estos dos casos no se contabilizan como aprobados ni fallidos. Se ejecutarán antes de utilizar el sistema con datos reales en un despliegue público.
