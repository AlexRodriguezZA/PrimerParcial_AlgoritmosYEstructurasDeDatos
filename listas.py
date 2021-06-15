class Lista(object):
    """Crea un objeto de tipo lista"""
    def __init__(self):
        self.__elementos = []
    
    def __criterio(self,dato,criterio):
        if(criterio==None):
            return dato;
        else:
            return dato[criterio];
    
    def insertar(self , dato, criterio = None): #!Tenemos que tener en cuenta de que la inserción este ordenada
        if(len(self.__elementos) == 0):
            self.__elementos.append(dato)
        elif(self.__criterio(dato,criterio) < self.__criterio((self.__elementos[0]),criterio)):
            self.__elementos.insert(0,dato)
        else:
            pos = 0;
            while(pos < len(self.__elementos) and self.__criterio(dato,criterio) >= self.__criterio(self.__elementos[pos],criterio )):
                pos += 1
            self.__elementos.insert(pos,dato)
    
    def obtenerElemento(self,pos):
        if(pos >= 0 ):
                return self.__elementos[pos]
        else:
            return None
    
    def modificar_elemento(self,pos,nuevoValor):
        self.__elementos.pop(pos)
        self.insertar(nuevoValor)
    
    def eliminar(self, dato, criterio=None, clave=None, criterio_clave=None):
        pos = self.busqueda(dato, criterio, clave, criterio_clave)
        if(pos != -1):
            return self.__elementos.pop(pos)
        else:
            return None

    def busqueda(self,datoBuscado,criterio = None, clave = None, criterio_clave = None):
        pos = -1
        primero = 0;
        ultimo = len(self.__elementos)
        while(primero <= ultimo and pos == -1):
            medio = (primero + ultimo) // 2;
            if(self.__criterio(self.__elementos[medio],criterio) == datoBuscado):
                pos = medio;
            elif(self.__criterio(self.__elementos[medio],criterio) > datoBuscado):
                ultimo = medio -1
            else:
                primero = medio +1
            
        if(pos != -1 and clave is not None and self.__elementos[pos][criterio_clave] != clave):
            while(self.__criterio(self.__elementos[pos],criterio) == self.__criterio(self.__elementos[pos-1],criterio)):
                pos -= 1;
            control = False
            while(self.__elementos[pos][criterio_clave] != clave and 
            self.__criterio(self.__elementos[pos],criterio) == self.__criterio(self.__elementos[pos+1],criterio)):
                pos += 1;
            if(self.__elementos[pos](criterio_clave) != clave):
                pos = -1;
            
            
        return pos;


    
    def lista_Vacia(self):
        return len(self.__elementos) == 0;
    
    def tamanio(self):
        return len(self.__elementos)
    
    def barrido(self):
        for elementos in self.__elementos:
            print(elementos)
    
    def barrido_eliminando(self, datos_eliminar):
        for elemento in self.__elementos:
            if(elemento in datos_eliminar):
                self.__elementos.remove(elemento)



