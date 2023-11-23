def agregar_registro(legajo, nombre, apellido, edad, mail, rama):
    if consultar_registro(legajo):
        return False
    else:
        nuevo_registro = {
            "legajo" : legajo,
            "nombre":nombre,
            "apellido": apellido,
            "edad" : edad,
            "mail" : mail,
            "rama": rama
        }
        registros.append(nuevo_registro)
        return True

def consultar_registro(legajo):
    for registro in registros:
        if registro['legajo'] == legajo:
            return registro
    return False

def listar_registros():
    print()
    print("-"*50)
    for registro in registros:
        print(f'Legajo.........: {registro["legajo"]}')
        print(f'Nombre....: {registro["nombre"]}')
        print(f'Apellido.......: {registro["apellido"]}')
        print(f'Edad.........: {registro["edad"]}')
        print(f'Mail.........: {registro["mail"]}')
        print(f'Rama......: {registro["rama"]}')
        print("-"*50)
        
def modificar_registro(legajo, nuevo_nombre, nuevo_apellido, nueva_edad, nuevo_mail, nueva_rama):
    for registro in registros:
        if registro['legajo'] == legajo:
            registro['nombre'] = nuevo_nombre
            registro['apellido'] = nuevo_apellido
            registro['edad'] = nueva_edad
            registro['mail'] = nuevo_mail
            registro['rama'] = nueva_rama
            return True
    return False

def eliminar_registro(legajo):
    for registro in registros:
        if registro['legajo'] == legajo:
            registros.remove(registro)
            return True
    return False
#---------------------------------------------------------------------------------
#Programa principal

#Definir lista(contiene diccionarios)

registros = [
            
]