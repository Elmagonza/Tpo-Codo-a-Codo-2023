import mysql.connector

class Nomina:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
        )
        
        self.cursor = self.conn.cursor(dictionary=True)
        
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS registros (
        legajo INT(8),
        nombre VARCHAR(255) NOT NULL,
        apellido VARCHAR(255) NOT NULL,
        edad INT(2) NOT NULL,
        mail VARCHAR(255),
        rama VARCHAR(20))''')
        self.conn.commit()
        
    def agregar_registro(self, legajo, nombre, apellido, edad, mail, rama):
        
        self.cursos.execute(f"SELECT * FROM registros WHERE legajo = {legajo}")
        legajo_existe = self.cursor.fetchone()
        if legajo_existe:
            return False
        
        sql = f"INSERT INTO registros (legajo, nombre, apellido, edad, mail, rama) VALUES ({legajo},{nombre},{apellido},{edad},{mail},{rama})"
        self.cursor.execute(sql)
        self.conn.commit()   
        return True
        
    def consultar_registro(self, legajo):
        # Consultamos un registro a partir de su legajo
        self.cursor.execute(f"SELECT * FROM registros WHERE legajo =
        {legajo}")
        
        return self.cursor.fetchone()
    
    def modificar_registro(self, legajo, nuevo_nombre,
nuevo_apellido, nueva_edad, nuevo_mail, nueva_rama):
    # Modificamos los datos de un registro a partir de su legajo
        sql = f"UPDATE registros SET nombre = '{nuevo_nombre}', apellido = {nuevo_apellido},edad = {nueva_edad}, mail = '{nuevo_mail}', rama = {nueva_rama} WHERE legajo = {legajo}"
        self.cursor.execute(sql)
        self.conn.commit()
        
        return self.cursor.rowcount > 0
    
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
    
    def listar_registros(self):
        # Mostramos en pantalla un listado de todos los registros en la tabla
        self.cursor.execute("SELECT * FROM registros")
        registros = self.cursor.fetchall()
        print("-" * 40)
        for registro in self.registros:
            print(f'\tLegajo....: {registro["legajo"]}')
            print(f'\tNombre....: {registro["nombre"]}')
            print(f'\tApellido..: {registro["apellido"]}')
            print(f'\tEdad......: {registro["edad"]}')
            print(f'\tMail......: {registro["mail"]}')
            print(f'\tRama......: {registro["rama"]}')
            print("-"*40)
            
    def eliminar_producto(self, legajo):
        # Eliminamos un producto de la tabla a partir de su legajo
        self.cursor.execute(f"DELETE FROM productos WHERE legajo =
        {legajo}")
        self.conn.commit()
        return self.cursor.rowcount > 0
    
#programa principal

nomina = Nomina(host="localhost", user="root", password="", database="miapp")
        