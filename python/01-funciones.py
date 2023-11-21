def agregar_producto(codigo, descripcion, cantidad, precio, imagen, proveedor):
    if consultar_producto(codigo):
        return False
    else:
        nuevo_producto = {
            "codigo" : codigo,
            "descripcion":descripcion,
            "cantidad": cantidad,
            "precio" : precio,
            "imagen" : imagen,
            "proveedor": proveedor
        }
        productos.append(nuevo_producto)
        return True

def consultar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            return producto
    return False

def listar_productos():
    print()
    print("-"*50)
    for producto in productos:
        print(f'Código.........: {producto["codigo"]}')
        print(f'Descripcion....: {producto["descripcion"]}')
        print(f'Cantidad.......: {producto["cantidad"]}')
        print(f'Precio.........: {producto["precio"]}')
        print(f'Imagen.........: {producto["imagen"]}')
        print(f'Proveedor......: {producto["proveedor"]}')
        print("-"*50)
        
def modificar_producto(codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
    for producto in productos:
        if producto['codigo'] == codigo:
            producto['descripcion'] = nueva_descripcion
            producto['cantidad'] = nueva_cantidad
            producto['precio'] = nuevo_precio
            producto['imagen'] = nueva_imagen
            producto['proveedor'] = nuevo_proveedor
            return True
    return False

def eliminar_producto(codigo):
    for producto in productos:
        if producto['codigo'] == codigo:
            productos.remove(producto)
            return True
    return False
#---------------------------------------------------------------------------------
#Programa principal

#Definir lista(contiene diccionarios)

productos = [
            
]