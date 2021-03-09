#import paquetes.lista_circular.Matriz as Matriz_class
#import paquetes.lista_circular.Nodo as Nodo_class
import paquetes.lista_circular.Lista_Enlazada as lista_e
import paquetes.lista_circular.Lista_Circular_Reducida as LCR


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
        self.lista_CR = LCR.Lista_Circular()    # Creando un objeto de la clase Lista_Circular para guardar la lista circular de los nombre de la matrices reducidas

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

    
    # Esta funcion es la que va a comparar dentro de la matriz que filas cumplen con un mismo patron para sumar, y asi obtener la matriz reducida
    def comparar_filas(self):
        if (self.head == None):
            return 
        nodo = self.head
        lista_sumar = []        # Voy a almacenar en cada posicion las filas que tengan el mismo patron (Ej. [0, 2], [1, 4], [3])
        lista_anidada = []      # Y es en esta lista donde voy a agrupar en cada posicion una lista de elementos que cumplan con un determinado patron
        cont = 0                # Este contador me a decir que si una fila tiene el mismo patron que otra, el contador deberia de ser igual al numero de columnas y por ende se guardarian el numero de fila de ambas filas
        auxiliar = 0            # Esta unicamente me va a ayudar a que en la primera vuelta pueda agrear una posicion dentro de la lista_anidada y asi poder recorrerla en la proxima vuelta
        
        #while (nodo.next != self.head):
        for x in range(self.tamano): 
            n = nodo.matriz.lista_enlazada.n
            m = nodo.matriz.lista_enlazada.m
            lista_anidada = []
            auxiliar = 0
            #print("---------------------------------" + nodo.matriz.nombre + "--------------------------------------")
            for k in range(n):
                for i in range(n):
                    cont = 0    
                    for j in range(m):
                        d1 = nodo.matriz.lista_enlazada.buscar_posicion(k, j)
                        d2 = nodo.matriz.lista_enlazada.buscar_posicion(i, j)
                        #print("Comparacion :" + str(d1) + " == " + str(d2))
                        #print(str(d1) + " == " + str(d2))
                        if (d1 == d2):                                          # Si el numero binario es igual...
                            cont += 1
                            #print("CONTADOR ", cont)

                        #print(str(cont) + "==" + str(m))
                        if (cont == m):                                         # Para que sean iguales las columnas el cont debe tener el mismo valor que el numero de columnas
                            lista_sumar.append(i)                               # Guardando la fila
                            #print("**SE AGREGO CON EXITO ", i)
                            #nodo.matriz.lista_enlazada.modificar_binario(i, 0)
                            #nodo.matriz.lista_enlazada.n = 0 # Al darle esto ya nunca será igual a un 1 o 0
                

                #print("Las filas que siguen un mismo patron son: ")
                #print(lista_sumar)
                cont_ = 0

                if (auxiliar == 0): # Va a ayudar para que a la segunda vuelta, el ciclo ya pueda realizar un recorrido
                    lista_anidada.append(lista_sumar) # En la primera vuelta la lista_anidad tiene que tener lo primero guardado en la lista sumar
                    auxiliar = 1                      # Cambiando su valor para que en la proxima vuelta pueda realizar iteraciones
                else:
                    for h in range(len(lista_anidada)): # Recorro cada posicion dentro de la lista_anidada para que, la lista_sumar tiene los mismos elementos ya almacenados dentro de la lista_anidad y asi evitar que las filas que cumplen con un determinado patron ya no se repitan
                        if (lista_sumar == lista_anidada[h]):   # Si en la lista_anidada ya existe lo que hay en la lista_sumar
                            cont_ = 1
                        if (h == (len(lista_anidada) - 1) and cont_ == 0): # Si ya va en la ultima vuelta y no encontro lo que tenia la lista_sumar dentro de la lista_anidada (el cont nunca tomo el valor de 1)
                            lista_anidada.append(lista_sumar)
                
                lista_sumar = []                        # Limpiando la lista, para en la proxima vuelta ya no existan los de la actual

            
            # -------------------------------------------------------------------------------------------------------------------------------------------------------
            # Es en este momento en el que ya tengo las filas agrupadas segun el patron que sigan de la forma [[1,3], [4], [0,2,5], [6]]
            # Caracteristicas:
            #   El tamaño de la lista_anidada va a ser el numero de filas en la matriz reducida
            # -------------------------------------------------------------------------------------------------------------------------------------------------------
            
            nombre_matriz = nodo.matriz.nombre      # Obteniendo el nombre de la matriz de la que se esta calculando la matriz reducida
            filas = len(lista_anidada)              # El numero de filas de la matriz anidada va a ser igual al tamaño de la lista_anidada
            columnas = m                            # El numero de columnas de la matriz reducida va a ser igual que el numero de columnas de la matriz original
            self.lista_CR.insertar(nombre_matriz=nombre_matriz, n=filas, m=columnas)    # Enviando en nombre de la matriz de la matriz reducida, el numero de filas y columnas
            matriz_a_llenar = self.lista_CR.matriz_a_llenar(nombre_matriz)              # Buscando la matriz que acabo de insertar, para ingresar la matriz reducida, para que me retorne el objeto matriz el cual tiene asociado una lista enlazada que es donde voy a guardar la matriz reducida         
            suma = 0                                                                    # Inicializando la variable donde voy a guardar la suma de cada una de las posiciones

            #print()
            #print("Las listas totales son ", lista_anidada)
            for grupo in lista_anidada:             # recorriendo las posiciones => [[1,3], [4], [0,2,5], [6]]
                for b in range(columnas):           # Manteniendo la fija la columna que se tomara como referencia
                    for a in grupo:                 # Recorriendo las posiciones de las lista que esta en esa posicion => [1,3] (estas son la filas que tienen el mismo patron)
                        a = int(a)                  # Posicionando el puntero en la fila que cumple con el mismo patron
                        dato = nodo.matriz.lista_enlazada.buscar_posicion_datos(a, b)   # Retorna el valor que se encuentra en la posicion enviada
                        #print("Sumando ", dato)
                        suma += dato
                        #print("Se sumo " + "(" + str(b) + "," + str(a) + ") = " + str(suma))
                    #print("SE SUMO ", suma)
                    matriz_a_llenar.lista_enlazada.insertar_(suma)      # Es aqui donde guarda la suma en la matriz  reducida
                    suma = 0                                            # Regresando la variable suma a 0

            for grupo in lista_anidada:                                 # Recorriendo la lista que contiene agrupadas la filas que cumplen con un patron en especifico ([[1,3], [4], [0,2,5], [6]])
                tamano_grupos = len(grupo)                              # Obtenido el taño de la lista que se encuantra en la posicion 0 ([1,3])
                #print("El tamaño de " + str(grupo) + " es " + str(tamano_grupos))
                matriz_a_llenar.lista_ER.insertar(tamano_grupos)        # La matriz tambien tiene asociada una lista del tipo Lista_Enlazada_Reducida, y en esa matriz voy a guardardar el numero de grupos fomados de esa matriz
                
            matriz_a_llenar.frecuencia = len(lista_anidada)             # Enviando el numero de etiquetas <frecuencia> que va a tener (que tambien va a ser el numero de filas de la matriz reducida)
            #matriz_a_llenar.grupos(len)

            #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            #matriz_a_llenar.lista_enlazada.imprimir_datos()
            #print()
            #print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

            # Hasta este punto ya tengo agrupadas las filas que hay que sumar
            nodo = nodo.next                                            # Pasando a lsiguinete nodo

    
    # Con esta funcion voy a llamar a otra del modulo Lista_Circular_Reducida
    def mostrar_XML(self, ruta_escritura):
        self.lista_CR.escribir_XML(ruta_escritura)