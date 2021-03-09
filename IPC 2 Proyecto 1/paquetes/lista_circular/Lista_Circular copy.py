#import paquetes.lista_circular.Matriz as Matriz_class
#import paquetes.lista_circular.Nodo as Nodo_class
import paquetes.lista_circular.Lista_Enlazada as lista_e


class Matriz:

    def __init__(self, nombre=None, lista_enlazada=None, n=None, m=None):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.lista_enlazada = lista_e.Lista_Enlazada(n=n, m=m)


class Nodo:

    def __init__(self, matriz=None, next=None):
        self.matriz = matriz
        self.next = next


class Lista_Circular:

    def __init__(self, head=None):
        self.head = head
        self.tamano = 0

    # Para insertar un nuevo elemento
    def insertar(self, nombre_matriz=None, n=None, m=None):
        if (self.tamano == 0):
            matriz = Matriz(nombre=nombre_matriz, n=n, m=m)
            self.head = Nodo(matriz=matriz)
            self.head.next = self.head
        else:
            #matriz = Matriz_class.Matriz(name_matriz)
            matriz = Matriz(nombre=nombre_matriz, n=n, m=m)
            #print("El seguiente nodo es ", matriz.nombre)
            #nuevo_nodo = Nodo_class.Nodo(matriz=matriz, next=self.head.next)
            nuevo_nodo = Nodo(matriz=matriz, next=self.head.next)
            self.head.next = nuevo_nodo
        self.tamano += 1

    # Solo para estar seguro que estan igresadas las matrices
    def imprimir(self):
        if (self.head == None):
            return
        nodo = self.head
        print(nodo.matriz.nombre, end=" => ")
        while (nodo.next != self.head):
            nodo = nodo.next
            print(nodo.matriz.nombre, end=" => ")
    
    
    # Recibe el numero de matrices ingresadas en el archivo, esto para recorrer toda la lista y validar que no existan dos o mas matrices con el mismo nombre
    def comparar_nombres(self, tamano_lista_c):
        if (self.head == None):                 # Si la lista esta vacia, que retorne False
            return False
        
        # Validando que no exista una matriz con el mismo nombre
        nodo = self.head
        siguiente = self.head
        verdadero = False # Si se queda con el valor de False, significa que no hay ninguna matriz repetida en el archivo de entrada 

        # Con los dos for i in range(tamano) aseguro que la lista sea recorrida completamente
        # Tanto nodo como siguiente van a comenzar desde la cabecera (head) para asi despues ir manipulandolos para que se comparen
        # Para eso sirve la variable k, que en este caso va a aumentar en 1 si o si, ya que compara su mismo posicion, pero
        # si encuentra a otra (ademas de su posicion), k aumenta a 2, lo que indica que ya extiste una matriz con el mismo nombre
        for i in range(tamano_lista_c):
            k = 0
            siguiente = self.head
            for j in range(tamano_lista_c):
                if (nodo.matriz.nombre == siguiente.matriz.nombre):
                    k += 1                                          # Va a aumentar en 1 cada vez que encuentre una matriz con el mismo nombre
                    if (k == 2):                                    # Significa que hay ya 2 matrices con el mismo nombre, ya que el contador llego a 2
                        verdadero = True                           
                        return verdadero 
                siguiente = siguiente.next                          # Pasando al siguiente nodo
            nodo = nodo.next


    # Con esta funcion voy a a buscar el nombre de la matriz que acaban de insertar dentro de los nodos y retornar el objeto matriz que contienen, para ingresar todos los atributos
    # dentro de la etiqueta <dato> correspondiente a cada matriz
    def matriz_a_llenar(self, nombre_matriz):
        if (self.head == None):             # Si la matriz esta vacia, que no retorne nada
            return 
        nodo = self.head
        if (nodo.next == self.head):        # Si solo hay un elemento (apuntandose a si mismo)
            return nodo.matriz
        for i in range(self.tamano):        # Asegurando que se recorra todos los nodos de la lista
            #print("**********************")
            #print(nodo.matriz.nombre + " == " + nombre_matriz)
            #print("**********************")
            if (nodo.matriz.nombre == nombre_matriz):
                return nodo.matriz
            nodo = nodo.next


    # Va a permitir retornar la el objeto matriz buscado para imprimir los datos de la matriz
    def imprimir_matriz_datos(self, nombre_matriz):
        if (self.head == None):
            return
        nodo = self.head
        if (nodo.next == self.head and nodo.matriz.nombre == nombre_matriz):
            return nodo.matriz
        
        for i in range(self.tamano):
            #print(nodo.matriz.nombre + "====" + nombre_matriz)
            if (nodo.matriz.nombre == nombre_matriz):
                return nodo.matriz
            nodo = nodo.next