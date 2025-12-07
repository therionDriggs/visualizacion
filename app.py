from flask import Flask, render_template_string
import time

app = Flask(__name__)

# Definición del script original
def ejecutar_conteo():
    resultado = 0
    html_output = "<h1>Resultado del Contador</h1>"
    for i in range(1, 11):
        resultado += i
        html_output += f"<p>Suma hasta {i}: {resultado}</p>"
    html_output += "<p>El script terminó su conteo y se mantiene en ejecución (servidor).</p>"
    return html_output

@app.route('/')
def home():
    # Renderizar el resultado como HTML
    return ejecutar_conteo()

if __name__ == "__main__":
    # El servidor Gunicorn o NGINX/uWSGI usualmente maneja esto, 
    # pero lo dejamos para pruebas locales
    app.run(host='0.0.0.0', port=8080)
