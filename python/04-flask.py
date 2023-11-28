# Instalar con pip install Flask
from flask import Flask, request, jsonify
from flask import request
# Instalar con pip install flask-cors
from flask_cors import CORS
# Instalar con pip install mysql-connector-python
import mysql.connector
# Si es necesario, pip install Werkzeug
from werkzeug.utils import secure_filename
# No es necesario instalar, es parte del sistema standard de Python
import os
import time

app = Flask(__name__)
CORS(app) # Esto habilitará CORS para todas las rutas

class Nomina:
# Constructor de la clase
    def __init__(self, host, user, password, database):
        # Primero, establecemos una conexión sin especificar la base de datos
        self.conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
        )   
        
        self.cursor = self.conn.cursor()
        # Intentamos seleccionar la base de datos
        try:
            self.cursor.execute(f"USE {database}")
        except mysql.connector.Error as err:
            # Si la base de datos no existe, la creamos
            if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                self.cursor.execute(f"CREATE DATABASE {database}")
                self.conn.database = database
            else:
                raise err
            
        # Una vez que la base de datos está establecida, creamos la tabla si no existe
    
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS registros (
        legajo INT(8),
        nombre VARCHAR(255) NOT NULL,
        apellido VARCHAR(255) NOT NULL,
        edad INT(2) NOT NULL,
        mail VARCHAR(255),
        rama VARCHAR(20))''')
        self.conn.commit()
        
        # Cerrar el cursor inicial y abrir uno nuevo con el parámetro dictionary=True
        self.cursor.close()
        self.cursor = self.conn.cursor(dictionary=True)
        
    def listar_registros(self):
        self.cursor.execute("SELECT * FROM registros")
        registros = self.cursor.fetchall()
        return registros
        
    def consultar_registro(self, legajo):
    # Consultamos un registro a partir de su legajo
        self.cursor.execute(f"SELECT * FROM registros WHERE legajo =
        {legajo}")
        return self.cursor.fetchone()
    
    
    def mostrar_registro(self, legajo):
        # Mostramos los datos de un registro a partir de su legajo
        registro = self.consultar_registro(legajo)
        if registro:
            print("-" * 40)
            print(f'\tLegajo....: {registro["legajo"]}')
            print(f'\tNombre....: {registro["nombre"]}')
            print(f'\tApellido..: {registro["apellido"]}')
            print(f'\tEdad......: {registro["edad"]}')
            print(f'\tMail......: {registro["mail"]}')
            print(f'\tRama......: {registro["rama"]}')
            print("-" * 40)
        else:
            print("Registro no encontrado.")
    
                
        
        
        
#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------
# Crear una instancia de la clase Nomina
nomina = Nomina(host='localhost', user='root', password='',
database='miapp')

#Ruta /registros
@app.route("/registros", methods=["GET"])
def listar_registros():
    registros = nomina.listar_registros()
    return jsonify(registros)

if __name__ == "__main__":
    app.run(debug=True)
    
@app.route("/registros/<int:legajo>", methods=["GET"])
def mostrar_registro(legajo):
    registro = nomina.consultar_registro(legajo)
    if registro:
        return jsonify(registro)
    else:
        return "registro no encontrado", 404
