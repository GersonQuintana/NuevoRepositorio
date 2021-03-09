class Grupo:

    def __init__(self, no_grupos):
        self.no_grupos = no_grupos

class Nodo:

    def __init__(self, no_grupos=None, next=None, posicion=None):
        self.no_grupos = no_grupos
        self.next = next
        self.posicion = posicion

class Lista_Enlazada:

    # Indica que el primero de los nodos va a apuntar a vacio
    def __init__(self):
        self.head = None
        self.posicion = 0
        self.tamano = 0     # Voy a guardar el tamaño de la lista

    # Función que permite insertar a un cliente a la lista
    def insertar(self, no_grupos):
        if (not self.head): # Si no hay cabecera, o si no hay nodo
            no_grupos = Grupo(no_grupos)
            self.head = Nodo(no_grupos=no_grupos, posicion=self.posicion)
            self.posicion += 1
            self.tamano += 1
            return
        # Si ya hay un nodo contenido en la cabecera, es decir, la lista no esta vacia
        actual = self.head # head siempre va a ser el primer nodo de la lista
        while (actual.next): # va a recorrer la lista hasta que encuentre el ultimo nodo (que va a ser el que no este vacio)
            actual = actual.next
        no_grupos = Grupo(no_grupos)
        actual.next = Nodo(no_grupos=no_grupos, posicion=self.posicion)
        self.posicion += 1
        self.tamano += 1

    # Funcion para saber los nodos que tiene la estructura
    def imprimir(self):
        node = self.head # Asignando el primer nodo a la variable node
        while (node != None):
            print(node.no_grupos.no_grupos, end=" => ")
            node = node.next

    def buscar_posicion(self, posicion_buscada):
        nodo = self.head

        for i in range(self.tamano):
            posicion = nodo.posicion
            if (posicion == posicion_buscada):
                return nodo.no_grupos.no_grupos # Retornando el numero de grupos agrupados
            nodo = nodo.next

    
    