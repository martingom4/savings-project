'''
vamos a hacer una calculadora simple en python

que debenmos de hacer?
1. crear una funcion que sume dos numeros
2. crear una funcion que reste dos numeros
3. crear una funcion que multiplique dos numeros
4. crear una funcion que divida dos numeros

despues debo de hacer que el usuario pueda ingresar los numeros y la operacion que desea hacer y que el programa le devuelva el resultado de la operacion que el usuario desea hacer con los numeros que ingreso

'''
class Calculadora:
    @staticmethod
    def suma(a,b):
        return a + b
    @staticmethod
    def res(a,b):
        return a - b
    @staticmethod
    def multi(a,b):
        return a * b
    @staticmethod
    def div(a,b):
        return a /b

def main():
    print("Bienvenido a la calculadora")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    opcion= int(input("Ingrese el numero de la operacion que desea hacer: "))
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    match opcion:
        case 1:
            print(Calculadora.suma(num1, num2))
        case 2:
            print(Calculadora.res(num1, num2))
        case 3:
            print(Calculadora.multi(num1, num2))
        case 4:
            print(Calculadora.div(num1, num2))
        case _:
            print("Operacion no valida")

if __name__ == "__main__":
    main()

