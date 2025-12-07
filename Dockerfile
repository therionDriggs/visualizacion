# Usamos una imagen base de Python
FROM python:3.12-slim

# Copiamos el script al contenedor
COPY contador.py /app/contador.py

# Directorio de trabajo
WORKDIR /app

# Comando para ejecutar el script
CMD ["python", "contador.py"]

