#bin! /bin/bash
# Validar que se pase un argumento ( nombre de archivo)
if [ -z “$1” ]; then
    echo “Por favor proporciona el nombre del archivo.”
    exit 1
fi

# Permitir la ejecución del archivo
chmod +x $1

# Cambiar la propiedad del archivo root
sudo chown root:root $1
echo “Se han modificado los permisos y la propiedad del archivo ‘$1’.”
