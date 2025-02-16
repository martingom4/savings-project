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
import sys
#ahora vamos a hacer una clase que haga lo mismo que el diccionario pero con metodos de clase y metodos estaticos y vamos a hacer que el programa sea un menu que se repita hasta que el usuario decida salir del programa

class gestroContactos:
    contactos = {
        "nombre": [],
        "telefono": [],
        "email": []
    }

    @classmethod
    def agregar_contacto(cls):
        nombre = input("Ingrese el nombre de la persona: ")
        telefono = input("Ingrese el teléfono de la persona: ")
        email = input("Ingrese el email de la persona: ")
        cls.contactos["nombre"].append(nombre)
        cls.contactos["telefono"].append(telefono)
        cls.contactos["email"].append(email)
        print("Contacto agregado correctamente")
        print(cls.contactos)
        return cls.contactos

    @classmethod
    def buscar_contacto(cls):
        nombre = input("Ingrese el nombre de la persona que desea buscar: ")
        for i in range(len(cls.contactos["nombre"])):
            if cls.contactos["nombre"][i] == nombre:
                print("Nombre: ", cls.contactos["nombre"][i])
                print("Teléfono: ", cls.contactos["telefono"][i])
                print("Email: ", cls.contactos["email"][i])
                break
        else:
            print("Contacto no encontrado")

    @classmethod
    def actualizar_contacto(cls):
        nombre = input('Ingrese el nombre de la persona que quiere actualizar: ')
        if nombre not in cls.contactos['nombre']:
            print(f"El contacto {nombre} no existe")
            return
        for i in range(len(cls.contactos['nombre'])):
            if cls.contactos['nombre'][i] == nombre:
                cls.contactos['nombre'][i] = input('Ingrese el nuevo nombre: ')
                cls.contactos['telefono'][i] = input('Ingrese el nuevo teléfono: ')
                cls.contactos['email'][i] = input('Ingrese el nuevo email: ')
                print('Contacto actualizado correctamente')
                print(cls.contactos)
                break

    @classmethod
    def eliminar_contacto(cls):
        nombre = input("Ingrese el nombre de la persona que quiere eliminar: ")
        for i in range(len(cls.contactos["nombre"])):
            if cls.contactos["nombre"][i] == nombre:
                cls.contactos["nombre"].pop(i)
                cls.contactos["telefono"].pop(i)
                cls.contactos["email"].pop(i)
                print("Contacto eliminado correctamente")
                print(cls.contactos)
                break
        else:
            print("Contacto no encontrado")

    @classmethod
    def ver_contactos(cls):
        if len(cls.contactos["nombre"]) == 0:
            print("No hay contactos para mostrar")
        else:
            for i in range(len(cls.contactos["nombre"])):
                print("Nombre: ", cls.contactos["nombre"][i])
                print("Teléfono: ", cls.contactos["telefono"][i])
                print("Email: ", cls.contactos["email"][i])
                print("|-----------------|")


gestor = gestroContactos()
def main():
    while True:
        print("\nBienvenido al gestor de contactos")
        opcion = input("1. Agregar contacto\n2. Buscar contacto\n3. Actualizar contacto\n4. Eliminar contacto\n5. Ver contactos\n6. Salir\n")
        match opcion:
            case "1":
                gestor.agregar_contacto()
            case "2":
               gestor.buscar_contacto()
            case "3":
                gestor.actualizar_contacto()
            case "4":
                gestor.eliminar_contacto()
            case "5":
                gestor.ver_contactos()
            case "6":
                False
                print('Gracias por usar el gestor de contactos')
                break
            case _:
                print("Opción no válida")

if __name__ == "__main__":
    main()
