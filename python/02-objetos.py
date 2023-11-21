class Catalogo:
    productos = []
    
    def agregar_producto(self, codigo, descripcion, cantidad, precio, imagen, proveedor):
        if self.consultar_producto(codigo):
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
            self.productos.append(nuevo_producto)
            return True

    def consultar_producto(self, codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                return producto
        return False
    
    def listar_productos(self):
        print()
        print("-"*50)
        for producto in self.productos:
            print(f'Código.........: {producto["codigo"]}')
            print(f'Descripcion....: {producto["descripcion"]}')
            print(f'Cantidad.......: {producto["cantidad"]}')
            print(f'Precio.........: {producto["precio"]}')
            print(f'Imagen.........: {producto["imagen"]}')
            print(f'Proveedor......: {producto["proveedor"]}')
            print("-"*50)
            
    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio, nueva_imagen, nuevo_proveedor):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                producto['descripcion'] = nueva_descripcion
                producto['cantidad'] = nueva_cantidad
                producto['precio'] = nuevo_precio
                producto['imagen'] = nueva_imagen
                producto['proveedor'] = nuevo_proveedor
                return True
        return False
            
    def eliminar_producto(self,codigo):
        for producto in self.productos:
            if producto['codigo'] == codigo:
                self.productos.remove(producto)
                return True
        return False
    
    