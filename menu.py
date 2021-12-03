from fecha import Fecha
from tiendas import TiendaChachi
from datetime import  datetime
from listas import Listas
from archivotienda import ArchivoTienda
from os import system


class Menu:
    
    def __init__(self,nombre_tienda):
        self.listas = Listas(nombre_tienda)
        #self.listas = Listas()

    def bandeja_productos(self):
        self.listas.visualizar_productos()

    def visualizar_salario(self):
        self.listas.salario()
    





    def visualizar_ventas(self,fecha_user):
        self.listas.registrar_compras()
        print()



    def realizar_compra(self):
        while True:
            print("++++++++++++++++++++++++++++++++++++++++++++++")
            print("----------------Productos-------------------")
            print("++++++++++++++++++++++++++++++++++++++++++++++")
            print("1: Yogur")
            print("2: Cafe")
            print("3: Pan")
            print("4: Salir")

            tipo_producto = int(input("Ingrese el producto que desea comprar: "))
            if tipo_producto ==4:
                break
            else:
                cant_producto = int(input("Ingrese la cantidad a comprar: "))
                if self.listas.cantidad_suficiente(tipo_producto,cant_producto):
                    if tipo_producto == 1:
                        if self.listas.cant_actual_producto(tipo_producto,cant_producto) !=-1:
            
                            if self.listas.cant_actual():
                                self.listas.registrar_compras()
                                print("++++++++++++++++++++++++++++++++++++++++++++++")
                                print("----------------La compra se efectuo correctamente-------------------")
                                print("++++++++++++++++++++++++++++++++++++++++++++++")
                                input()
                            else:
                                print("++++++++++++++++++++++++++++++++++++++++++++++")
                                print("La compra no se pudo realizar correctamente.")
                                print("++++++++++++++++++++++++++++++++++++++++++++++")
                                input()
                        
                        else:
                            print("No hay existencias")
                            input()
                    elif tipo_producto == 2:
                        if self.listas.cant_actual_producto(tipo_producto,cant_producto) !=-1:

                            if self.listas.cant_actual():
                                self.listas.registrar_compras()

                                print("++++++++++++++++++++++++++++++++++++++++++++++")
                                print("----------------La compra se efectuo correctamente-------------------")
                                print("++++++++++++++++++++++++++++++++++++++++++++++")
                                input()

                            else:
                                print("++++++++++++++++++++++++++++++++++++++++++++++")
                                print("La compra no se pudo realizar correctamente.")
                                print("++++++++++++++++++++++++++++++++++++++++++++++")
                                input()
                        
                        else:
                            print("No hay existencias")
                            input()
                    elif tipo_producto == 3:
                        if self.listas.cant_actual_producto(tipo_producto,cant_producto) !=-1:

                            if self.listas.cant_actual():
                                self.listas.registrar_compras()

                                print("++++++++++++++++++++++++++++++++++++++++++++++")
                                print("----------------La compra se efectuo correctamente-------------------")
                                print("++++++++++++++++++++++++++++++++++++++++++++++")
                                input()

                            else:
                                print("++++++++++++++++++++++++++++++++++++++++++++++")
                                print("La compra no se pudo realizar correctamente.")
                                print("++++++++++++++++++++++++++++++++++++++++++++++")
                                input()
                        
                        else:
                            print("No hay existencias")
                            input()
                            
                    else:
                        print("Error, la opcion ingresada es incorrecta.")
                        input()
                else:
                    print("Error salario insuficiente")
                    input()



    def imprimir_ventas_fecha(self):
            while True:
                system("cls")
                print("++++++++++++++++++++++++++++++++++++++++++++++")
                print("----------------Imprimir ventas a partir de la fecha-------------------")
                print("++++++++++++++++++++++++++++++++++++++++++++++")
                print("1: Ver fechas")
                print("2: Salir")
                selec_user = int(input("Ingrese el numero de la fecha que desea visualizar: "))
                self.visualizar_ventas(selec_user)

    def mostrar_menu(self):
        for i in range (3):
            fecha = Fecha(10,24,50)
            lista_productos = ["Yogur","Cafe","Pan"]
            cantidad_productos = [3,2,1]
            precio_unitario = [200,500,300]
            productos = TiendaChachi(fecha[i],lista_productos[i],cantidad_productos[i],precio_unitario[i])
            if self.listas.adicionar_producto(productos):
                nothing = 0
        
        while True:
            system("cls")
            print("1: Cliente")
            print("2: Administrador")
            usuario = int(input("Ingrese su tipo de usuario: "))
            contador_intentos_admin = 0
            if usuario == 1:
                system("cls")
                print("++++++++++++++++++++++++++++++++++++++++++++++")
                print("++++++++++++++++++++++++++++++++++++++++++++++")
                print("----------------Doña chachi-------------------")
                print("++++++++++++++++++++++++++++++++++++++++++++++")
                print("++++++++++++++++++++++++++++++++++++++++++++++")
                print("--------------------MENU PRINCIPAL--------------------------")
                print("++++++++++++++++++++++++++++++++++++++++++++++")
                print("++++++++++++++++++++++++++++++++++++++++++++++")
                print("1: Bandeja de Productos")
                print("2: Mi Salario")
                print("3: Realizar Compra")
                print("4: Salir")
                
                opcion_user = int(input("Ingrese una opcion: "))

                if opcion_user == 1:
                    self.bandeja_productos()
                elif opcion_user == 2:
                    self.visualizar_salario()
                elif opcion_user == 3:
                    self.realizar_compra()
                elif opcion_user == 4:
                    break
                else:
                    print("Error,opcion incorrecta.")

            elif usuario == 2:
                while True:
                    contraseña_admin = int(input("Ingrese su contraseña: "))
                    if contraseña_admin == 123:
                        break
                    else:
                        system("cls")
                        print("Error, contraseña incorrecta")
                    contador_intentos_admin += 1
                    if contador_intentos_admin ==3:
                        break
                while True:
                    system("cls")
                    print("++++++++++++++++++++++++++++++++++++++++++++++")
                    print("++++++++++++++++++++++++++++++++++++++++++++++")
                    print("----------------Doña chachi-------------------")
                    print("++++++++++++++++++++++++++++++++++++++++++++++")
                    print("++++++++++++++++++++++++++++++++++++++++++++++")
                    print("--------------------MENU ADMINISTRADOR--------------------------")
                    print("++++++++++++++++++++++++++++++++++++++++++++++")
                    print("++++++++++++++++++++++++++++++++++++++++++++++")
                    print("1: Bandeja de Productos")
                    print("2: Imprimir ventas por fecha")
                    print("3: Imprimir ventas por nombre del producto")
                    print("4: Salir")
                    opcion_user = int(input("Ingrese una opcion: "))

                    if opcion_user == 1:
                        self.bandeja_productos()
                    elif opcion_user == 2:
                        self.imprimir_ventas_fecha()
                    elif opcion_user == 3:
                        self.realizar_compra()
                    elif opcion_user ==4:
                        break















            else:
                print("Error, opcion no valida: ")
        

if __name__ == '__main__':
    listas = Listas("TIENDA")
    menu = Menu(listas)
    menu.mostrar_menu()