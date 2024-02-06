from datetime import datetime

class Articulo:

    def __init__(self, codigo : str, nombre : str, descripcion : str, precio : int):

        self.codigo = codigo
        self.nombre = nombre
        self.desc = descripcion
        self.precio = precio

class CarritoCompra:

    def __init__(self):

        self.imp_minimo = 50
        self.lista_articulos = []
        self.bono = None

    def agregar_articulo(self, articulo):
        self.lista_articulos.append(articulo)

    def agregar_bono(self, bono):
        if self.bono is None and bono.aplicado is False:
            self.bono = bono
            bono.aplicado = True
            print('Bono agregado correctamente.')
        else:
            print('El bono no se ha agregado.')

    def importe_descontado(self):
        if self.bono is not None:
            total = self.compra_total
            if total >= self.imp_minimo and self.bono.caducidad > datetime.now():
                total -= self.bono.descuento
                return total
        return total

    @property
    def compra_total(self):
        return sum(articulo.precio for articulo in self.lista_articulos)
         

    def total_desc(self):
        if self.bono is not None:
            print(f'Descuento aplicado: {self.bono.descuento}.')
        else:
            print('No hay bono disponible.')

class Bono:

    def __init__(self, codigo, descuento, caducidad, aplicado=False):
        self.codigo = codigo
        self.descuento = descuento
        self.caducidad = caducidad
        self.aplicado = aplicado

class Usuario:

    def __init__(self, nombre, apellido, mail, activo):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self.activo = activo