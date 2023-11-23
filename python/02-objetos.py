class Nomina:
    registros = []
    
    def agregar_registro(self, legajo, nombre, apellido, edad, mail, rama):
        if self.consultar_registro(legajo):
            return False
        else:
            nuevo_registro = { # Diccionario de datos
                "legajo" : legajo,
                "nombre":nombre,
                "apellido": apellido,
                "edad" : edad,
                "mail" : mail,
                "rama": rama
            }
            self.registros.append(nuevo_registro)
            return True

    def consultar_registro(self, legajo):
        for registro in self.registros:
            if registro['legajo'] == legajo:
                return registro
        return False
    
    def listar_registros(self):
        print()
        print("-"*50)
        for registro in self.registros:
            print(f'\tLegajo....: {registro["legajo"]}')
            print(f'\tNombre....: {registro["nombre"]}')
            print(f'\tApellido..: {registro["apellido"]}')
            print(f'\tEdad......: {registro["edad"]}')
            print(f'\tMail......: {registro["mail"]}')
            print(f'\tRama......: {registro["rama"]}')
            print("-"*50)
            
    def modificar_registro(self, legajo, nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_mail, nueva_rama):
        for registro in self.registros:
            if registro['legajo'] == legajo:
                registro['nombre'] = nuevo_nombre
                registro['apellido'] = nuevo_apellido
                registro['edad'] = nueva_edad
                registro['mail'] = nuevo_mail
                registro['rama'] = nueva_rama
                return True
        return False
            
    def eliminar_registro(self,legajo):
        for registro in self.registros:
            if registro['legajo'] == legajo:
                self.registros.remove(registro)
                return True
        return False
    
    
#Programa principal

