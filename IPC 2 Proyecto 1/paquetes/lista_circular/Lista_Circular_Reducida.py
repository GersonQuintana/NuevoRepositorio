import paquetes.lista_circular.Lista_Circular
import paquetes.lista_circular.Lista_Enlazada as lista_e
import paquetes.lista_circular.Lista_Enlazada_Reducida as LER
from xml.etree.ElementTree import Element, SubElement, Comment
from xml.etree import ElementTree
from xml.dom import minidom

class Matriz:

    def __init__(self, nombre=None, lista_enlazada=None, n=None, m=None, frecuencia=None, grupos=None):
        self.nombre = nombre
        self.n = n
        self.m = m
        self.lista_enlazada = lista_e.Lista_Enlazada(n=n, m=m)
        self.frecuencia = frecuencia
        self.lista_ER = LER.Lista_Enlazada()


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
        #print("Insertado > ", nombre_matriz)
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

    def imprimir(self):
        if (self.head == None):
            return
        nodo = self.head
        print(nodo.matriz.nombre, end=" => ")
        while (nodo.next != self.head):
            nodo = nodo.next
            print(nodo.matriz.nombre, end=" => ")


    # Funcion que me va a permitir rellenar a una matriz con sus datos
    def matriz_a_llenar(self, nombre_matriz):
        if (self.head == None):  # Si la matriz esta vacia
            return 
        nodo = self.head
        if (nodo.next == self.head): # Si solo hay un elemento (apuntandose a si mismo)
            return nodo.matriz
        for i in range(self.tamano):
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
    

    # Le va a dar la estructura mas amigable al archivo xml generado con las matrices reducidad
    def prettify(self, elem):
        #print("Lego", elem)
        #rough_string = ElementTree.tostring(elem, 'utf-8')
        rough_string = ElementTree.tostring(elem, "utf-8")
        #print("Lego", elem)
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="  ")


    # En esta va a tener la logica para escribir en el archivo xml
    def escribir_XML(self, ruta_escritura):
        if (self.head == None):  # Si la matriz esta vacia
            return 
        nodo = self.head
        root = Element('matrices')  # Creando la raiz del arbol que va a tener el nombre de matrices
            
        for k in range(self.tamano):
            #print("SI LLEGA")
            tamano = nodo.matriz.lista_ER.tamano 
            m = nodo.matriz.lista_enlazada.m
            nombre = nodo.matriz.nombre
            #print(nodo.matriz.nombre)
            frecuencia = nodo.matriz.frecuencia
            hijo = SubElement(root, "matriz")
            hijo.set("nombre", nombre + "_Salida")
            hijo.set("n", str(frecuencia))
            hijo.set("m", str(m))
            hijo.set("g", str(tamano))
            for i in range(frecuencia):
                for j in range(m):
                    dato = nodo.matriz.lista_enlazada.buscar_posicion_datos(i ,j)
                    #print(dato)
                    nieto = SubElement(hijo, "dato")
                    nieto.set("x", str(i+1))
                    nieto.set("y", str(j+1))
                    nieto.text = str(dato)
            
            grupo = 0
                
            for k in range(tamano):
                grupo = nodo.matriz.lista_ER.buscar_posicion(k)
                nieto = SubElement(hijo, "frecuencia")
                nieto.set("g", str(k+1))
                nieto.text = str(grupo)
            
            hijo.tail = "\n"                # Cuando escribe la matriz reducida de una matriz da un salto de linea    

            nodo = nodo.next                # Avanzando al siguiente nodo
        
            #print("CAMBIO")

        #print("yA ")
        
        
        
        r = self.prettify(root)
        archivo = open(ruta_escritura, "w")
        archivo.write(r)

