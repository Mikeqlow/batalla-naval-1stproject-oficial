class Mar:
    def __init__(self,):
        self.tablero = [[" " for i in range(10)] for i in range(10)]
    def imprimir_mar(self):
        for fila in self.tablero:
            print(" ".join(fila)) # Imprime cada fila del tablero y separa cada elemento con un espacio.


class Ship:
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño
        self.posicion = []
        self.hits = 0
        self.inicial = nombre[0].upper()

    def colocar_barco(self, mar, start_row, start_col, direccion):
        #Verifica si el barco cabe en el tablero y si la posición está disponible:
        if direccion == "h":
            if start_col + self.tamaño > 10:
                print("El barco no cabe en el tablero")
                return False
            for col in range(start_col, start_col + self.tamaño):
                if mar.tablero[start_row][col] != " ":
                    print("No se puede colocar el barco aquí")
                    return False
                
        elif direccion == "v": 
            if start_row + self.tamaño > 10:
                print("El barco no cabe en el tablero")
                return False
            for row in range(start_row, start_row + self.tamaño):  
                if mar.tablero [row][start_col] != " ":
                    print("No se puede colocar el barco aquí")
                    return False
        
        #Coloca el barco en el tablero:
        if direccion == "h":
            for col in range(start_col, start_col + self.tamaño):
                mar.tablero[start_row][col] = self.inicial
                self.posicion.append((start_row, col))
        elif direccion == "v":
            for row in range(start_row, start_row + self.tamaño):  
                mar.tablero [row][start_col] = self.inicial
                self.posicion.append((row, start_col))
        return True
    
    def hit(self, mar, row, col):

        if(row, col) in self.posicion:
            mar.tablero[row][col] = "x"
            print("Disparo acertado")
            self.hits += 1
            if self.hits == self.tamaño:
                print(f"El barco {self.nombre} ha sido hundido")
                return True
            print("El barco sigue en flote")
            return False

        else:
            print("Agua, hazlo mejor")
            return False


        
        
        
                
class Destructor(Ship):   
    def __init__(self):
        super().__init__("Destructor", 2)   
class Submarino(Ship):
    def __init__(self):
        super().__init__("Submarino", 3) 
class Acorazado(Ship):
    def __init__(self):
        super().__init__("Acorazado", 4)

##mar = Mar()
##mar.imprimir_mar()





"""barco = Ship("Destructor", 3)
# Llamar al método createBoard a través de la instancia
tablero = barco.createBoard()
barco.imprimir_tablero(tablero)"""