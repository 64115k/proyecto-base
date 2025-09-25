from clases.operaciones import Operaciones

def main():
    op = Operaciones()
    op.leerNumeros()
    op.sumar()
    op.mostrarResultado()

    op.resta()
    op.mostrarResultado()

    op.multiplicacion()
    op.mostrarResultado()

    op.division()
    op.mostrarResultado()
    
    #Realiza las pruebas con las nuevas operaciones
    

if __name__ == "__main__":
    main()
    
    
