# Ejercicio 1
class Producto:
    def __init__(self, nombre, precio, cantidad): # Atributos
        # Atributos privados
        self.__nombre = nombre 
        self.__precio = float(precio)
        self.__cantidad = int(cantidad)

    def get_attributes(self): # Método get 
        return f'Caracteristicas del producto:\nNombre: {self.__nombre}\nPrecio: {self.__precio:.2f}\nCantidad: {self.__cantidad}'
    
    def set_attributes(self): # Método set
        self.__nombre = input('\nIngrese el nombre del producto: ')
        
        while True: # Manejo de excepciones
            try:
                self.__precio = float(input('Ingrese el precio del producto: '))
                if self.__precio < 0:
                    raise ValueError('El precio no puede ser negativo.\n')
                break
            
            except Exception as e:
                print(f'Error: {e}\n')
            
        while True: # Manejo de excepciones
            try:
                self.__cantidad = int(input('Ingrese la cantidad del producto: '))
                if self.__cantidad < 0:
                    raise ValueError('La cantidad no puede ser negativa.\n')
                break
            
            except Exception as e:
                print(f'Error: {e}\n')
            

# Instancia de la clase Producto
producto = Producto('Coca-Cola', 1.5, 10)
print(producto.get_attributes())
producto.set_attributes()
print(producto.get_attributes())

# Ejercicio 2
class Estudiante: # Clase 
    def __init__(self, nombre, edad, nota_final): # Atributos
        # Atributos privados
        self.__nombre = nombre
        self.__edad = int(edad)
        self.__nota_final = float(nota_final)
    
    def get_attributes(self): # Método get
        return f'Caracteristicas del estudiante:\nNombre: {self.__nombre}\nEdad: {self.__edad}\nNota final: {self.__nota_final:.2f}\n'
    
    def set_attributes(self): # Método set
        self.__nombre = input('\nIngrese el nombre del estudiante: ')
        
        while True: # Manejo de excepciones
            try:
                self.__edad = int(input('Ingrese la edad del estudiante: '))
                if not self.__edad in range(0, 101):
                    raise ValueError('La edad ser menor a 0.\n' if self.__edad < 0 else 'La edad no puede ser mayor a 100.\n')
                break
            
            except Exception as e:
                print(f'Error: {e}\n')
            
        while True: # Manejo de excepciones
            try:
                self.__nota_final = float(input('Ingrese la nota final del estudiante: '))
                if not self.__nota_final in range(0, 101):
                    raise ValueError('La nota final no puede ser menor a 0.\n' if self.__nota_final < 0 else 'La nota final no puede ser mayor a 100.\n')
                break
            
            except Exception as e:
                print(f'Error: {e}\n')

# Instancia de la clase Estudiante
estudiante = Estudiante('Juan', 20, 90)
print(estudiante.get_attributes())
estudiante.set_attributes()
print(estudiante.get_attributes())

# Ejercicio 3
class Vehiculo: # Clase 
    def __init__(self, marca, modelo, velocidad): # Atributos
        # Atributos privados
        self.__marca = marca
        self.__modelo = modelo
        self.__velocidad = float(velocidad)
    
    def get_attributes(self): # Método get
        return f'Caracteristicas del vehiculo:\nMarca: {self.__marca}\nModelo: {self.__modelo}\nVelocidad: {self.__velocidad:.2f} Km/h\n'
    
    def set_attributes(self): # Método set
        self.__marca = input('\nIngrese la marca del vehiculo: ')
        self.__modelo = input('Ingrese el modelo del vehiculo: ')
        
        while True: # Manejo de excepciones
            try:
                self.__velocidad = float(input('Ingrese la velocidad del vehiculo: '))
                if not self.__velocidad in range(0, 201):
                    raise ValueError('La velocidad no puede ser negativa.\n')
                break
            
            except Exception as e:
                print(f'Error: {e}\n')

# Instancia de la clase Vehiculo
vehiculo = Vehiculo('Toyota', 'Corolla', 120)
print(vehiculo.get_attributes())
vehiculo.set_attributes()
print(vehiculo.get_attributes())

# ejercicio 4 
class Libro: # Clase 
    def __init__(self, titulo, autor, num_paginas, disponible): # Atributos
        # Atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__num_paginas = int(num_paginas)
        self.__disponible = disponible
    
    def get_attributes(self): # Método get
        return f'Caracteristicas del libro:\nTitulo: {self.__titulo}\nAutor: {self.__autor}\nNumero de paginas: {self.__num_paginas}\nDisponibilidad: {self.__disponible}\n'

    def set_attributes(self): # Método set
        self.__titulo = input('\nIngrese el titulo del libro: ')
        self.__autor = input('Ingrese el autor del libro: ')
        
        while True: # Manejo de excepciones
            try:
                self.__num_paginas = int(input('Ingrese el numero de paginas del libro: '))
                if self.__num_paginas < 0:
                    raise ValueError('El numero de paginas no puede ser negativo.\n')
                break
            
            except Exception as e:
                print(f'Error: {e}\n')
                
        while True: # Manejo de excepciones
            try:
                self.__disponible = input('Ingrese la disponibilidad del libro: ')
                if not self.__disponible in ['prestado', 'devuelto']:
                    raise ValueError('La disponibilidad del libro solo puede ser prestado o devuelto.\n')
                break
            
            except Exception as e:
                print(f'Error: {e}')
                
# Instancia de la clase Libro
libro = Libro('El principito', 'Antoine de Saint-Exupéry', 100, 'devuelto')
print(libro.get_attributes())
libro.set_attributes()
print(libro.get_attributes())

# Ejercicio 5
from modules.email import *

class Usuario: # Clase padre
    def __init__(self, username, email, password): # Atributos
        # Atributos privados
        self.__username = username
        self.__email = email
        self.__password = password
    
    # Métodos get
    def get_username(self):
        return f'{self.__username}'
    
    def get_password(self):
        return f'{self.__password}'
    
    def get_email(self):
        return f'{self.__email}'
    
    # Métodos set
    def set_email(self, email):
        self.__email = email
    
    def set_password(self, password):
            self.__password = password
        
# Instancia de la clase Email
user = Usuario('user', 'example@gmail.com', '12345678')
print(f'Username: {user.get_username()}\nEmail: {user.get_email()}\nPassword: {user.get_password()}\n')
while True:
    user.set_email(input('Ingrese el email: '))
    if gmail(user.get_email()):
        break
    else:
        print('Ingrese corectamente el Gmail.\n')

while True:
    user.set_password(input('Ingrese la contraseña: '))
    if len(user.get_password()) >= 8:
        break
    else:
        print('La contraseña debe tener al menos 8 caracteres.\n')
        
print(f'\nUsername: {user.get_username()}\nEmail: {user.get_email()}\nPassword: {user.get_password()}')