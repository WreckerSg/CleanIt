# Guía para subir la entrega a GitHub

El repositorio previsto es <https://github.com/WreckerSg/CleanIt>. El archivo ZIP entregado debe descomprimirse antes de subirlo; GitHub no utiliza el contenido de un ZIP como estructura navegable del repositorio.

## Opción A - Desde el navegador

1. Descargue y descomprima `CleanIt_entrega_final.zip`.
2. Abra el repositorio CleanIt en GitHub.
3. Seleccione **Add file** y después **Upload files**.
4. Arrastre **el contenido interno** de la carpeta `CleanIt-entrega-final`, no la carpeta como un nivel adicional.
5. Confirme que en la raíz aparezcan `README.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`, `docs`, `src`, `tests` y `.github`.
6. Use como mensaje de commit: `SCRUM-35 agrega documentación de la entrega final`.
7. Confirme el commit en la rama `main` si el repositorio todavía está vacío.

## Opción B - Con Git

```bash
git clone https://github.com/WreckerSg/CleanIt.git
cd CleanIt
```

Copie dentro de esa carpeta todo el contenido extraído y ejecute:

```bash
git status
git add .
git commit -m "SCRUM-35 agrega documentación de la entrega final"
git push origin main
```

Si Git solicita autenticación, utilice el inicio de sesión configurado en Git Credential Manager o una clave/token autorizado; GitHub no acepta la contraseña normal de la cuenta para operaciones Git por HTTPS.

## Comprobación posterior

- `README.md` se muestra automáticamente al abrir el repositorio.
- Los enlaces de la tabla de entregables abren los documentos correctos.
- Los diagramas Mermaid aparecen en el README y en la documentación técnica.
- La carpeta `.github/ISSUE_TEMPLATE` contiene las dos plantillas.
- Los archivos `.gitignore` y `.env.example` están presentes.
- La docente puede acceder al repositorio.
- La URL entregada en la plataforma es `https://github.com/WreckerSg/CleanIt`.

