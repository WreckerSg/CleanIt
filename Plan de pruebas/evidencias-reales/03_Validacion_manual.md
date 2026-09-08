# Validación manual en Windows

## Ambiente

| Campo | Valor |
|---|---|
| Sistema | Windows con PowerShell |
| Python | 3.10.11 |
| Navegador | Google Chrome |
| Base local | SQLite |
| Dirección | `http://127.0.0.1:8081/` |
| Datos | Cuentas y tareas ficticias |

## Recorridos confirmados

- El superusuario inició sesión y fue identificado como **Administrador**.
- Se creó `participante1` y el panel lo identificó como **Participante**.
- El participante no visualizó funciones administrativas.
- Se creó la zona `Cocina` y quedó activa.
- Se creó `Limpiar la cocina`, asignada a `participante1` y con frecuencia semanal.
- La descripción de la tarea se editó correctamente.
- El sistema impidió desactivar una zona con una tarea activa.
- La tarea fue retirada de forma lógica y permaneció visible con estado **Retirada**.

Las capturas observadas durante el recorrido no se almacenan en el repositorio porque incluían elementos personales o ajenos a la aplicación en la interfaz del navegador.

Los flujos de pendientes, cumplimiento, recurrencia e historial quedaron cubiertos por pruebas funcionales automatizadas. Pueden repetirse visualmente durante la demostración con datos ficticios.
