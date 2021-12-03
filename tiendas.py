#from listas import Listas
class TiendaChachi:
    def __init__(self,fecha,nombre_producto,cantidad_producto,precio_unitario):
        self.__fecha = fecha
        self.__nombre_producto = nombre_producto
        self.__cantidad_producto = cantidad_producto
        self.__precio_unitario = precio_unitario
        self.__ventas_lista = []
        #self.listas = Listas()
        



    def get_fecha(self):
        return self.__fecha
    def get_nombre_producto(self):
        return self.__nombre_producto
    def get_cantidad_producto(self):
        return self.__cantidad_producto
    def get_precio_unitario(self):
        return self.__precio_unitario
    def get_ventas_lista(self):
        return self.__ventas_lista


    def set_fecha(self,fecha):
        self.__fecha = fecha

    def set_nombre_producto(self,nombre_producto):
        self.__nombre_producto = nombre_producto
        
    def set_cant_producto(self,cantidad_producto):
        self.__cantidad_producto = cantidad_producto

    def set_nombre_producto(self,precio_unitario):
        self.__precio_unitario = precio_unitario




    def restar_cantidad_producto(self,cantidad_comprada):
        if self.__cantidad_producto -cantidad_comprada< 0:
            return False        
        else:
            self.__cantidad_producto -=  cantidad_comprada

            return True

    def calcular_saldo_suf(self,salario_user,cantidad_producto):
        total =cantidad_producto * self.__precio_unitario
        if salario_user <total:
            return False
        else:
            salario_act = salario_user - total
            return salario_act