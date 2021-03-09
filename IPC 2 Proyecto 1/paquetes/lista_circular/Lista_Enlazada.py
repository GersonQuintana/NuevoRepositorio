class Dato:

    def __init__(self, dato=None):
        self.dato = dato

class Nodo:

    def __init__(self, dato=None, next_horizontal=None, next_vertical=None, x=None, y=None):
        self.dato = dato
        self.next_horizontal = next_horizontal
        self.next_vertical = next_vertical
        self.x = x
        self.y = y

class Nodo_Binario:
    
    def __init__(self, dato=None, next_horizontal_b=None, next_vertical_b=None, a=None, b=None):
        self.dato = dato
        self.next_horizontal_b = next_horizontal_b
        self.next_vertical_b = next_vertical_b
        self.a = a
        self.b = b

class Lista_Enlazada:

    def __init__(self, n=None, m=None):
        self.head = None
        self.head_b = None
        self.n = n
        self.m = m
        # Punteros para la matriz con numeros diferentes de 0 y 1
        self.x = 0
        self.y = 0
        # Punteros para la matriz binaria (solo con valores de 0 y 1)
        self.a = 0
        self.b = 0
        #print("Se recibio n=" + str(n) + " m=" + str(m))
        

    # Va a permitir ingresar datos a la matriz, va a recibir las posiciones en donde voy a guardar el valor
    def insertar__(self, dato, x_, y_):
        #print("Se recibio el valor ", dato)
        if (self.x == self.n and self.y == self.m): # Si ya se llego al limite hay que reiniciar los punteros
            self.x = 0
            self.y = 0

        dato1 = dato
        if (self.head == None):
            dato = Dato(dato=dato)
            self.head = Nodo(dato=dato, x=x_, y=y_)
            #print("Se ingreso " + str(dato1) + " en la pocion " + str(x_) + ", " + str(y_) + "*")
            self.y += 1 # El apuntandor se mueve de columna
            return

        actual_horizontal = self.head
        actual_vertical = self.head
        while (self.x < (self.n)):
            while (self.y < self.m):
                if (self.y == (self.m - 1)):    # Si ya se llego al limite de columnas [][][] => None
                    while (actual_vertical.next_vertical != None):
                        actual_vertical = actual_vertical.next_vertical

                    while (actual_horizontal.next_horizontal != None):
                        actual_horizontal = actual_horizontal.next_horizontal

                    dato = Dato(dato=dato)
                    actual_horizontal.next_horizontal = Nodo(dato=dato, x=x_, y=y_)
                    actual_vertical.next_vertical = actual_horizontal.next_horizontal
                    #actual_vertical.next_vertical = Nodo(dato=dato, x=self.x, y=self.y)
                    
                    #print("Se ingreso " + str(dato1) + " en la pocion " + str(x_) + ", " + str(y_) + "*")
                    self.x += 1
                    self.y = 0
                    #self.x = 0
                    return
                    
                while (actual_horizontal.next_horizontal != None):
                    actual_horizontal = actual_horizontal.next_horizontal
                dato = Dato(dato=dato)
                actual_horizontal.next_horizontal = Nodo(dato=dato, x=x_, y=y_)
                #print("Se ingreso " + str(dato1) + " en la pocion " + str(x_) + ", " + str(y_))
                self.y += 1
                return
            return

    
    # Va a permitir ingresar un 1 o 0 dependiendo del valor en la matriz binaria
    def insertar_binaria(self, dato, x_, y_):

        if (self.a == self.n and self.b == self.m): # Si ya se llego al limite hay que reiniciar los punteros
            self.a = 0
            self.b = 0

        dato1 = dato
        if (self.head_b == None):
            dato = Dato(dato=dato)
            self.head_b = Nodo_Binario(dato=dato, a=x_, b=y_)
            #print("Se ingreso " + str(dato1) + " en la pocion " + str(x_) + ", " + str(y_) + "*")
            self.b += 1 # El apuntandor se mueve de columna
            return

        actual_horizontal_b = self.head_b
        actual_vertical_b = self.head_b
        while (self.a < (self.n)):
            while (self.b < self.m):
                if (self.b == (self.m - 1)):    # Si ya se llego al limite de columnas [][][] => None
                    while (actual_vertical_b.next_vertical_b != None):
                        actual_vertical_b = actual_vertical_b.next_vertical_b

                    while (actual_horizontal_b.next_horizontal_b != None):
                        actual_horizontal_b = actual_horizontal_b.next_horizontal_b

                    dato = Dato(dato=dato)
                    actual_horizontal_b.next_horizontal_b = Nodo_Binario(dato=dato, a=x_, b=y_)
                    actual_vertical_b.next_vertical_b = actual_horizontal_b.next_horizontal_b
                    #actual_vertical.next_vertical = Nodo(dato=dato, x=self.x, y=self.y)
                    
                    #print("Se ingreso " + str(dato1) + " en la pocion " + str(x_) + ", " + str(y_) + "*")
                    self.a += 1
                    self.b = 0
                    #self.x = 0
                    return
                    
                while (actual_horizontal_b.next_horizontal_b != None):
                    actual_horizontal_b = actual_horizontal_b.next_horizontal_b
                dato = Dato(dato=dato)
                actual_horizontal_b.next_horizontal_b = Nodo_Binario(dato=dato, a=x_, b=y_)
                #print("Se ingreso " + str(dato1) + " en la pocion " + str(x_) + ", " + str(y_))
                self.b += 1
                return
            return
    
    def insertar_(self, dato):
        #print("Se recibio el valor ", dato)
        if (self.x == self.n and self.y == self.m): # Si ya se llego al limite hay que reiniciar los punteros
            self.x = 0
            self.y = 0

        dato1 = dato
        if (self.head == None):
            dato = Dato(dato=dato)
            self.head = Nodo(dato=dato, x=self.x, y=self.y)
            #print("Se ingreso " + str(dato1) + " en la pocion " + str(self.x) + ", " + str(self.y) + "*")
            self.y += 1 # El apuntandor se mueve de columna
            return

        actual_horizontal = self.head
        actual_vertical = self.head
        while (self.x < (self.n)):
            while (self.y < self.m):
                if (self.y == (self.m - 1)):    # Si ya se llego al limite de columnas [][][] => None
                    while (actual_vertical.next_vertical != None):
                        actual_vertical = actual_vertical.next_vertical

                    while (actual_horizontal.next_horizontal != None):
                        actual_horizontal = actual_horizontal.next_horizontal

                    dato = Dato(dato=dato)
                    actual_horizontal.next_horizontal = Nodo(dato=dato, x=self.x, y=self.y)
                    actual_vertical.next_vertical = actual_horizontal.next_horizontal
                    #actual_vertical.next_vertical = Nodo(dato=dato, x=self.x, y=self.y)
                    
                    #print("Se ingreso " + str(dato1) + " en la pocion " + str(self.x) + ", " + str(self.y) + "*")
                    self.x += 1
                    self.y = 0
                    #self.x = 0
                    return
                    
                while (actual_horizontal.next_horizontal != None):
                    actual_horizontal = actual_horizontal.next_horizontal
                dato = Dato(dato=dato)
                actual_horizontal.next_horizontal = Nodo(dato=dato, x=self.x, y=self.y)
                #print("Se ingreso " + str(dato1) + " en la pocion " + str(self.x) + ", " + str(self.y))
                self.y += 1
                return
            return
        


    # Va a permitir imprimir los datos de la matriz buscada
    def imprimir_datos(self):
        actual_horizontal = self.head
        actual_vertical = self.head
        #print("SI ENTRO")

        for i in range(self.n):
            for j in range(self.m):
                x = actual_horizontal.x
                y = actual_horizontal.y
                if (x==i and y==j):
                    #print("(" + str(x) + ", " + str(y) + ") " + str(actual_horizontal.dato.dato), end=" => ")
                    print(str(actual_horizontal.dato.dato), end=" => ")
                    #print(actual_horizontal.dato.dato, end=" => ")
                actual_horizontal = actual_horizontal.next_horizontal


    def imprimir_binaria(self):
        actual_horizontal_b = self.head_b
        actual_vertical_b = self.head_b

        for i in range(self.n):
            for j in range(self.m):
                a = actual_horizontal_b.a # En la primera vuelta valdrán 0
                b = actual_horizontal_b.b
                if (a==i and b==j):
                    print(actual_horizontal_b.dato.dato, end=" => ")
                actual_horizontal_b = actual_horizontal_b.next_horizontal_b


    # Busca el valor almacenado en la posicion indicada en la matriz binaria
    def buscar_posicion(self, x, y):
        actual_horizontal_b = self.head_b
        actual_vertical_b = self.head_b
        #print("RECIBIDO: x==" + str(x) + " y==" + str(y))

        #print("n====== ", self.n)
        for i in range(self.n):
            #print("ENTRO")
            for j in range(self.m):
                a = actual_horizontal_b.a
                b = actual_horizontal_b.b
                #print(str(a) + "==" + str(x) + " and " + str(b) + "==" + str(y))
                if (a==x and b==y):
                    #print("Valor: " + str(actual_horizontal_b.dato.dato) + "Posicion x=" + str(a) + " y=" + str(b))
                    return actual_horizontal_b.dato.dato
                actual_horizontal_b = actual_horizontal_b.next_horizontal_b
    

    

    # Va a buscar la posición pero ahora dentro de la lista con los valores que vanian en el archivo
    def buscar_posicion_datos(self, a, b):
        actual_horizontal = self.head
        actual_vertical = self.head
        #print("RECIBIDO: x==" + str(x) + " y==" + str(y))

        #print("n====== ", self.n)
        for i in range(self.n):
            #print("ENTRO")
            for j in range(self.m):
                x = actual_horizontal.x
                y = actual_horizontal.y
                #print(str(a) + "==" + str(x) + " and " + str(b) + "==" + str(y))
                if (x==a and y==b):
                    #print("Valor: " + str(actual_horizontal_b.dato.dato) + "Posicion x=" + str(a) + " y=" + str(b))
                    return actual_horizontal.dato.dato
                actual_horizontal = actual_horizontal.next_horizontal
                

    def modificar_binario(self, x, y):
        actual_horizontal_b = self.head_b
        actual_vertical_b = self.head_b

        for i in range(self.n):
            for j in range(self.m):
                a = actual_horizontal_b.a
                b = actual_horizontal_b.b
                if (a==x and b==y):
                    actual_horizontal_b.dato.dato = 55 # Dandole un valor a cualqueriera de los datos de la matriz binaria, para ya no volver a compararla
                    #print("AHORA (" + str(a) + ", " + str(b) + ") == " + str(55))
                    return
                actual_horizontal_b = actual_horizontal_b.next_horizontal_b
                   
                    

    def imprimir(self):
        actual = self.head
        while (actual != None):
            print(actual.dato.dato)
            #print(actual.dato.grupo)
            actual = actual.next_horizontal

    def eliminar(self, name_matrix):
        actual = self.head
        previo = None
        while (actual and actual.dato.nombre_matriz != name_matrix):
            previo = actual
            actual = actual.next

        if (previo == None):
            self.head = actual.next
        elif (actual):
            previo.next = actual.next
            actual.next = None
    

    # Va a permitir escribir escribir en un archivo XML
    def escribir_XML(self):
        root = Element('matrices')

        actual_horizontal = self.head
        actual_vertical = self.head

        for i in range(self.n):
            for j in range(self.m):
                x = actual_horizontal.x
                y = actual_horizontal.y
                if (x==i and y==j):
                    print("(" + str(x) + ", " + str(y) + ") " + str(actual_horizontal.dato.dato), end=" => ")
                    #print(actual_horizontal.dato.dato, end=" => ")
                actual_horizontal = actual_horizontal.next_horizontal
