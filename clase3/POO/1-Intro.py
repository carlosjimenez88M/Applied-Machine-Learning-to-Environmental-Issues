 '''
 Programación orientada a objetos
 '''
 
 
 # Se basa en la premisa 
 # objetos y acciones
 
 # Las caracteristicas en OOPP son atributos como : una marca, un tamaño de una prenda de vestir, etc
 # las acciones son métodos como puede ser un cambio de precio
 
 # Vamos a hacer nuestra primer clase y ver como funciona
 
 #%%
 
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
     


nueva_camiseta = Camiseta("Amarillo Pollito",
         "XXL",
         "Fresca",
         30)

    
 
# %%
nueva_camiseta.precio
# %%
nueva_camiseta.cambio_de_precio(10)
nueva_camiseta.precio
# %%
print(nueva_camiseta.descuento(0.3))

# %%
#==============================#
#      Ejercicio en Clase      #
#==============================#

#Ejercicio 1: Crear una Clase Persona
#Objetivo: Familiarizarse con la creación de clases y objetos.

#rea una clase llamada Persona que tenga los siguientes atributos:

#nombre
#edad
#genero
#Implementa un constructor para la clase que inicialice estos atributos.

#Crea un método llamado mostrar_informacion que imprima la información de la persona.

#Instancia tres objetos de la clase Persona y llama al método mostrar_informacion para cada uno.

# Ejercicio 2: Crear una Clase CuentaBancaria
# Objetivo: Trabajar con encapsulamiento y métodos para gestionar el estado del objeto.

# Crea una clase llamada CuentaBancaria con los atributos titular y saldo.
# Implementa métodos para depositar (depositar) y retirar (retirar) dinero.
# Implementa un método para mostrar el saldo (mostrar_saldo).
# Instancia un objeto de la clase CuentaBancaria y realiza algunas operaciones de depósito y retiro, mostrando el saldo después de cada operación.