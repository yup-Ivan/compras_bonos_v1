from funct.utils import *
from datetime import datetime

carrito = CarritoCompra()
artic1 = Articulo('111', 'Leche', 'Leche Semidesnatada', 5)
artic2 = Articulo('112', 'Galletas', 'De chocolate', 2)
carrito.agregar_articulo(artic1)
carrito.agregar_articulo(artic2)
bono1 = Bono("DESC20", 20, datetime(2024, 12, 31))
carrito.agregar_bono(bono1)
print(f'Compra total: {carrito.compra_total()}')
carrito.total_desc()
