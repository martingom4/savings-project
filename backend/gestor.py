'''
Gestor de Contactos:

Desarrolla un programa que permita al usuario almacenar y gestionar contactos (nombre, teléfono, email, etc.) en una lista o diccionario.

Agrega funcionalidades como buscar contactos, actualizar información y eliminar contactos.

Puedes utilizar un diccionario para almacenar la información de los contactos, donde la llave sea el nombre del contacto y el valor sea una lista con los datos del contacto.

pasos para hacer esto

1. crear un diccionario vacio en donde esten los contactos como claves tendran nombre,telefono, email. como valores pueden ser listas ya que podran muchos contactos
2. crear una funcion que permita agregar contactos al diccionario
3. crear una funcion que permita buscar contactos en el diccionario
4. crear una funcion que permita actualizar la informacion de un contacto
5. crear una funcion que permita eliminar un contacto
6. crear una funcion que permita ver todos los contactos
7. crear una funcion que permita salir del programa

'''
import json
import re

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"

class GestorContactos:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, contacto):
        self.contactos[contacto.nombre] = contacto

    def buscar_contacto(self, nombre):
        return self.contactos.get(nombre, None)

    def actualizar_contacto(self, nombre, nuevo_contacto):
        if nombre in self.contactos:
            self.contactos[nombre] = nuevo_contacto
            return True
        return False

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
            return True
        return False

    def ver_contactos(self):
        if not self.contactos:
            print("No hay contactos para mostrar")
        else:
            for contacto in self.contactos.values():
                print(contacto)

    def guardar_contactos(self, archivo='contactos.json'):
        with open(archivo, 'w') as f:
            json.dump([contacto.__dict__ for contacto in self.contactos.values()], f)

    def cargar_contactos(self, archivo='contactos.json'):
        try:
            with open(archivo, 'r') as f:
                data = json.load(f)
                self.contactos = {contacto['nombre']: Contacto(**contacto) for contacto in data}
        except FileNotFoundError:
            self.contactos = {}

def validar_email(email):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' # formato de email
    return re.match(patron, email) is not None

def validar_telefono(telefono):
    return telefono.isdigit() # esto para validar que sean numeros

def main():
    gestor = GestorContactos()
    gestor.cargar_contactos()

    while True:
        print("\nBienvenido al gestor de contactos")
        opcion = input("1. Agregar contacto\n2. Buscar contacto\n3. Actualizar contacto\n4. Eliminar contacto\n5. Ver contactos\n6. Salir\n")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la persona: ")
            telefono = input("Ingrese el teléfono de la persona: ")
            email = input("Ingrese el email de la persona: ")
            if validar_telefono(telefono) and validar_email(email):
                contacto = Contacto(nombre, telefono, email)
                gestor.agregar_contacto(contacto)
                print("Contacto agregado correctamente")
            else:
                print("Teléfono o email no válido")

        elif opcion == "2":
            nombre = input("Ingrese el nombre de la persona que desea buscar: ")
            contacto = gestor.buscar_contacto(nombre)
            if contacto:
                print(contacto)
            else:
                print("Contacto no encontrado")

        elif opcion == "3":
            nombre = input('Ingrese el nombre de la persona que quiere actualizar: ')
            contacto = gestor.buscar_contacto(nombre)
            if contacto:
                nuevo_nombre = input('Ingrese el nuevo nombre: ')
                nuevo_telefono = input('Ingrese el nuevo teléfono: ')
                nuevo_email = input('Ingrese el nuevo email: ')
                if validar_telefono(nuevo_telefono) and validar_email(nuevo_email):
                    nuevo_contacto = Contacto(nuevo_nombre, nuevo_telefono, nuevo_email)
                    gestor.actualizar_contacto(nombre, nuevo_contacto)
                    print('Contacto actualizado correctamente')
                else:
                    print("Teléfono o email no válido")
            else:
                print("Contacto no encontrado")

        elif opcion == "4":
            nombre = input("Ingrese el nombre de la persona que quiere eliminar: ")
            if gestor.eliminar_contacto(nombre):
                print("Contacto eliminado correctamente")
            else:
                print("Contacto no encontrado")

        elif opcion == "5":
            gestor.ver_contactos()

        elif opcion == "6":
            gestor.guardar_contactos()
            print('Gracias por usar el gestor de contactos')
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()


