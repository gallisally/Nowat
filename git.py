#!/bin/bash

# Ruta local de tu repositorio de código
RUTA_LOCAL="/ruta/a/tu/repo/local"

# Mensaje del commit
MENSAJE_COMMIT="Actualización de código"

# Nombre de la rama
RAMA="main"

# Nombre de usuario de GitHub
USUARIO_GITHUB="tu_usuario_github"

# Nombre del repositorio en GitHub
REPOSITORIO_GITHUB="nombre_repositorio"

# URL del repositorio remoto en GitHub
URL_REPO_GITHUB="https://github.com/$USUARIO_GITHUB/$REPOSITORIO_GITHUB.git"

# Cambia al directorio local del repositorio
cd "$RUTA_LOCAL"

# Asegúrate de estar en la rama correcta
git checkout "$RAMA"

# Agrega todos los cambios al área de preparación
git add .

# Crea un nuevo commit con los cambios
git commit -m "$MENSAJE_COMMIT"

# Sube los cambios al repositorio remoto en GitHub
git push origin "$RAMA"

# Abre la página del repositorio en GitHub en el navegador
xdg-open "$URL_REPO_GITHUB"
