class Mar:
    def __init__(self,):
        self.tablero = [["🌊" for i in range(10)] for i in range(10)]
    def imprimir_mar(self):
        for fila in self.tablero:
            print(" ".join(fila)) # Imprime cada fila del tablero y separa cada elemento con un espacio.


class Ship:
    def __init__(self, nombre, tamaño = 3):
        self.nombre = nombre
        self.tamaño = tamaño
        self.posicion = []
        self.hits = 0

    def colocar_barco(self, mar, start_row, start_col, direccion):
        #Verificar si el barco cabe en el tablero:
        if direccion == "h" and start_col + self.tamaño > 10:
                print("El barco no cabe en el tablero")
                return False
        if direccion == "v" and start_row + self.tamaño > 10:
                print("El barco no cabe en el tablero")
                return False

        #Verificar si hay un barco en la posición deseada:
        if direccion == "h":
            for col in range(start_col, start_col + self.tamaño):
                if mar.tablero[start_row][col] != "🌊":
                    print("No se puede colocar el barco aquí")
                    return False
        if direccion == "v":
            for row in range(start_row, start_row + self.tamaño):  
                if mar.tablero [start_col][row] != "🌊":
                    return False
             
                
                
        
                
                
                     


mar = Mar()
mar.imprimir_mar()





"""barco = Ship("Destructor", 3)
# Llamar al método createBoard a través de la instancia
tablero = barco.createBoard()
barco.imprimir_tablero(tablero)"""