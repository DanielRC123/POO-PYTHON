from datetime import date, datetime
from fecha import Fecha
from tiendas import TiendaChachi
from archivotienda import ArchivoTienda
class Listas:
    def __init__(self, nombre_tienda):
        self.nombre = nombre_tienda

        self.ventas_lista = []
        self.lista_fechas = []
        self.__productos =[]
        self.sueldo_act = 20000
        self.lista_codigos_fecha =[]

    def get_lista_productos(self):
        return self.__productos
    
    def buscar_producto(self,nombre_producto):
        for i in range(len(self.__productos)):
            if self.__productos[i].get_nombre_producto() ==nombre_producto:
                return i
        return -1

    def adicionar_producto(self,tiendas):
        if self.buscar_producto(tiendas.get_nombre_producto()) == -1:
            self.__productos.append(tiendas)
            return True
        return False





    def visualizar_productos(self):
        for productos in self.get_lista_productos():
            print("****************************")
            print("Nombre:  %s" %(productos.get_nombre_producto()))
            print("Unidades:  %s" %(productos.get_cantidad_producto()))
            print("Precio:  %s" %(productos.get_precio_unitario()))
            print("+++++++++++++++++++++++++++++")
        input()


    
    def salario(self):
        print("Su salario acual es de: ", self.sueldo_act)
        input()

    def cant_actual(self):
        return True
        


    def cantidad_suficiente(self,posicion,cant_producto):
        salario_act = self.sueldo_act

        posicion = posicion -1
        salario_act = self.__productos[posicion].calcular_saldo_suf(salario_act,cant_producto)
        if salario_act ==False:
            return False
        else:
            self.sueldo_act = salario_act
            return True


    def cant_actual_producto(self,posicion,cant_producto):
        posicion = posicion -1

        if self.__productos[posicion].restar_cantidad_producto(cant_producto):
            return True
        else:
            return -1


    def registrar_compras(self,codigo):
        fecha_compra = Fecha(500) 
        codigos_fechas = 1
        if self.buscar_fecha(fecha_compra)!=-1:
            return 4
        else:
            self.adicionar_fecha(fecha_compra)
            for productos in range():
                self.__productos.append(datetime.now)[0]
                print(self.__productos[0])



    def buscar_fecha(self,fecha):
        for i in range(len(self.lista_fechas)):
            if self.lista_fechas[i] ==fecha:
                return i 
        return -1

    def adicionar_fecha(self,fecha):
        if self.buscar_fecha(fecha) == -1:
            self.lista_fechas.append(fecha)
            return True
        return False

