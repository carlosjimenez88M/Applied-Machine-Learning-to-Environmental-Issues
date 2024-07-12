class Camiseta:
     # La linea de abajo inicializa los atributos con los valores propios de las operaciones
     def __init__(self, color, talla, estilo, precio):
         self.color= color
         self.talla= talla
         self.estilo = estilo
         self.precio = precio
        
     def cambio_de_precio(self, new_price):
        self.precio =  new_price
        
     
     def descuento(self, off):
         return self.precio * (1- off)
     
