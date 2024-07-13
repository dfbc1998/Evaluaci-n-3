from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    resultado = {}
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        def mapear_nota(nota):
            return 10 + (nota - 1) * (70 - 10) / (100 - 1)

        nota1_mapeada = mapear_nota(nota1)
        nota2_mapeada = mapear_nota(nota2)
        nota3_mapeada = mapear_nota(nota3)

        promedio = round((nota1_mapeada + nota2_mapeada + nota3_mapeada) / 2)  # Redondear el promedio a 2 decimales
        estado = "Aprobado" if promedio >= 40 and asistencia >= 75 else "Reprobado"
        resultado = {'promedio': promedio, 'estado': estado}
    return render_template('ejercicio1.html', resultado=resultado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    resultado = {}
    if request.method == 'POST':
        nombres = [request.form['nombre1'], request.form['nombre2'], request.form['nombre3']]
        nombre_mas_largo = max(nombres, key=len)
        longitud = len(nombre_mas_largo)
        resultado = {'nombre': nombre_mas_largo, 'longitud': longitud}
    return render_template('ejercicio2.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
