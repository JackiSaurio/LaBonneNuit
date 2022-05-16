from flask import Flask, render_template, request
from tkinter import messagebox as MessageBox
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'labonnenuit'

app.secret_key = 'mysecretkey'

mysql = MySQL(app)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/menu')
def menu():
    return render_template("menu.html")


@app.route('/reservacion')
def reservacion():
    return render_template("reservaciones.html")


@app.route('/TrabajaConNosotros')
def TrabajaConNosotros():
    return render_template("TrabajaConNosotros.html")

@app.route('/Reservacion', methods=["POST"])
def Reservacion():
    try:
        cursor = mysql.connection.cursor()
        nombre = str(request.form.get('nombre'))
        apellido = str(request.form.get('apellido'))
        email = str(request.form.get('email'))
        telefono = int(request.form.get('telefono'))
        nPeronas = int(request.form.get('selNumPersonas'))
        fecha = str(request.form.get('selNumPersonas'))
        hora = int(request.form.get('selHora'))
        nTarjeta = int(request.form.get('nTarjeta'))
        inFechaExp = str(request.form.get('inFechaExp'))
        inCvv = int(request.form.get('inCvv'))
        if (nombre != "" or apellido != "" or email != "" or len(telefono) < 0 or len(
                nPeronas) < 0 or fecha != "" or inFechaExp != "" or len(hora) < 0 or len(nTarjeta) < 0 or len(inCvv) < 0):
            MessageBox.showinfo("Error!", "Han quedado campos sin llenar")
            return render_template("reservaciones.html")
        else:
            cursor.execute("INSERT INTO reservaciones VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s, %s)",
                           (nombre, apellido, email, telefono, nPeronas, fecha, hora, nTarjeta, inFechaExp, inCvv))
            mysql.connection.commit()
            return render_template("index.html")
    except Exception:
        MessageBox.showinfo("Error!", "Han quedado campos sin llenar")
        return render_template("reservaciones.html")


@app.route('/EnviarDatosSoli', methods=["POST"])
def EnviarDatosSoli():
    try:
        cursor = mysql.connection.cursor()
        nombre = str(request.form.get('nombre'))
        apellido = str(request.form.get('apellido'))
        email = str(request.form.get('email'))
        telefono = int(request.form.get('telefono'))
        edad = int(request.form.get('edad'))
        direccion = str(request.form.get('direccion'))
        colonia = str(request.form.get('colonia'))
        cp = int(request.form.get('cp'))
        if nombre!= "" or apellido!= "" or email!= "" or len(telefono) < 0 or len(edad) < 0 or direccion!= "" or colonia!= "" or len(cp) < 0:
            MessageBox.showinfo("Error!", "Han quedado campos sin llenar")
            return render_template("TrabajaConNosotros.html")
        else:
            cursor.execute("INSERT INTO solicitudes VALUES (%s, %s, %s,%s, %s, %s, %s, %s)",
                           (nombre, apellido, email, telefono, edad, direccion, colonia, cp))
            mysql.connection.commit()
            return render_template("index.html")
    except Exception:
        MessageBox.showinfo("Error!", "Han quedado campos sin llenar")
        return render_template("TrabajaConNosotros.html")



if __name__ == '__main__':
    app.run()
