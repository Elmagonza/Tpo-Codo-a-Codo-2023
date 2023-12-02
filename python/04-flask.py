# Instalar con pip install Flask
from flask import Flask, request, jsonify
from flask import request
# Instalar con pip install flask-cors
from flask_cors import CORS
# Instalar con pip install mysql-connector-python
import mysql.connector

# Si es necesario, pip install Werkzeug
#from werkzeug.utils import secure_filename

# No es necesario instalar, es parte del sistema standard de Python
# import os
# import time

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
        
    #----------------------------------------------------------------
       
    def listar_registros(self):
        self.cursor.execute("SELECT * FROM registros")
        registros = self.cursor.fetchall()
        return registros
    
    #----------------------------------------------------------------
        
    def consultar_registro(self, legajo):
    # Consultamos un registro a partir de su legajo
        self.cursor.execute(f"SELECT * FROM registros WHERE legajo = {legajo}")
        return self.cursor.fetchone()
    
    #----------------------------------------------------------------
    
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
    
    #----------------------------------------------------------------
    
    def agregar_registro(self, legajo, nombre, apellido, edad, mail, rama):
    # Verificamos si ya existe un registro con el mismo código
        self.cursor.execute(f"SELECT * FROM registros WHERE legajo ={legajo}")
        registro_existe = self.cursor.fetchone()
        if registro_existe:
            return False
        # Si no existe, agregamos el nuevo registro a la tabla
        sql = "INSERT INTO registros (legajo, nombre, apellido, edad, mail, rama) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (legajo, nombre, apellido, edad, mail, rama)
        self.cursor.execute(sql, valores)
        self.conn.commit()
        return True        
    
    #----------------------------------------------------------------
        
    def modificar_registro(self,legajo, nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_mail, nueva_rama):
        #Modificamos un registro a partir de su legajo
        sql = "UPDATE registros SET nombre = %s, apellido = %s, edad = %s, mail = %s, rama = %s WHERE legajo = %s"
        valores = (nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_mail, nueva_rama,legajo)
        self.cursor.execute(sql, valores)
        self.conn.commit() 
        return self.cursor.rowcount > 0
    
    #----------------------------------------------------------------
    
    def eliminar_registro(self, legajo):
        # Eliminamos un registro de la tabla a partir de su legajo
        self.cursor.execute(f"DELETE FROM registros WHERE legajo ={legajo}")
        self.conn.commit()
        return self.cursor.rowcount > 0
    
#--------------------------------------------------------------------
# Cuerpo del programa
#--------------------------------------------------------------------

# Crear una instancia de la clase Nomina
nomina = Nomina(host='kevingcrimson.mysql.pythonanywhere-services.com', user='kevingcrimson', password='codoacodo',
database='kevingcrimson$miapp')


#----------------------------------------------------------------
#Ruta /registros
@app.route("/registros", methods=["GET"])
def listar_registros():
    registros = nomina.listar_registros()
    return jsonify(registros)
#----------------------------------------------------------------    
@app.route("/registros/<int:legajo>", methods=["GET"])
def mostrar_registro(legajo):
    nomina.mostrar_registro(legajo)
    registro = nomina.consultar_registro(legajo)
    if registro:
        return jsonify(registro)
    else:
        return "registro no encontrado", 404
#----------------------------------------------------------------
@app.route("/registros", methods=["POST"])
def agregar_registro():
# Recojo los datos del form
    legajo = request.form['legajo']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    mail = request.form['mail']
    rama = request.form['rama']
    #nombre_mail = secure_filename(mail.filename)
    #nombre_base, extension = os.path.splitext(nombre_mail)
    #nombre_mail = f"{nombre_base}_{int(time.time())}{extension}"
    #mail.save(os.path.join(ruta_destino, nombre_mail))
    if nomina.agregar_registro(legajo, nombre, apellido,edad, mail, rama):
        return jsonify({"mensaje": "registro agregado"}), 201
    else:
        return jsonify({"mensaje": "registro ya existe"}), 400
#----------------------------------------------------------------        
@app.route("/registros/<int:legajo>", methods=["PUT"])
def modificar_registro(legajo): 
    # Recojo los datos del form
    nuevo_nombre = request.form.get("nombre")
    nuevo_apellido = request.form.get("apellido")
    nueva_edad = request.form.get("edad")
    nuevo_mail = request.form.get("mail")
    nueva_rama = request.form.get("rama")
    # Procesamiento de la imagen                (SIN USAR)
        # imagen = request.files['imagen']
        # nombre_imagen = secure_filename(imagen.filename)
        # nombre_base, extension = os.path.splitext(nombre_imagen)
        # nombre_imagen = f"{nombre_base}_{int(time.time())}{extension}"
        # imagen.save(os.path.join(ruta_destino, nombre_imagen))
        
    # Actualización del registro
    if nomina.modificar_registro(legajo, nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_mail, nueva_rama):
        return jsonify({"mensaje": "registro modificado"}), 200
    else:
        return jsonify({"mensaje": "registro no encontrado"}), 404
#----------------------------------------------------------------    
@app.route("/registros/<int:legajo>", methods=["DELETE"])
def eliminar_registro(legajo):
    # Primero, obtén la información del registro para encontrar la imagen
    registro = nomina.consultar_registro(legajo)
    if registro:
        # # Eliminar la imagen asociada si existe
        #     ruta_imagen = os.path.join(ruta_destino, registro['imagen_url'])
        #     if os.path.exists(ruta_imagen):
        #     os.remove(ruta_imagen)
        # Luego, elimina el registro del catálogo
        if nomina.eliminar_registro(legajo):
            return jsonify({"mensaje": "registro eliminado"}), 200
        else:
            return jsonify({"mensaje": "Error al eliminar el registro"}),500
    else:
        return jsonify({"mensaje": "registro no encontrado"}), 404
    
#----------------------------------------------------------------    
    
if __name__ == "__main__":
    app.run(debug=True)