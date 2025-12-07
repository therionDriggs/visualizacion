# Usamos una imagen base de Python
FROM python:3.12-slim

# Copiamos el script al contenedor (¡CAMBIADO A app.py!)
COPY app.py /app/app.py

# Directorio de trabajo
WORKDIR /app

# Instalar el servidor web Flask y Gunicorn
RUN pip install Flask gunicorn

# Exponer el puerto que usará Gunicorn
EXPOSE 8080

# Comando para ejecutar el servidor Gunicorn (¡CAMBIADO A app:app!)
# 'app:app' significa: módulo app, objeto Flask llamado app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]
