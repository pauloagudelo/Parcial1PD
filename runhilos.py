import matrizhilos
import threading

def main():
    b=True
    while b==True:

        lista = ['CALCULADORA MATRICES', '   MENU\n''1.Determinante', '2.Transpuesta',
                 '3.Multiplicar por un numero la matriz', '4.Salir']

        for i in lista:
            print i
        p = int(input("Seleccione La operacion que Desea calcular: "))

        def matriz_det():
            matrizA = matrizhilos.Matriz()
            matrizA.crearMatrizA()
            a = matrizA.llenarmatrizA()
            matrizA.imprime_matriz()
            matrizA.matriz_det(a)
        if p == 1:
            hilo1 = threading.Thread(target=matriz_det, args=())
            hilo1.start()
            # hilo1.setName("Nombre paulo")
            # print threading.enumerate()
            hilo1.join()

        def transpuesta():
            matrizA = matrizhilos.Matriz()
            matrizA.crearMatrizA()
            matrizA.llenarmatrizA()
            matrizA.imprime_matriz()
            matrizA.transpuesta()

        if p == 2:
            hilo2 = threading.Thread(target=transpuesta, args=())
            hilo2.start()
            # hilo2.setName("Nombre paulo")
            # print threading.enumerate()
            hilo2.join()

        def numero():
            matrizA = matrizhilos.Matriz()
            matrizA.crearMatrizA()
            matrizA.llenarmatrizA()
            matrizA.imprime_matriz()
            matrizA.matriz_numero()

        if p == 3:
            hilo3 = threading.Thread(target=numero, args=())
            hilo3.start()
            #hilo3.setName("Nombre paulo")
            #print threading.enumerate()
            hilo3.join()


        if p == 4:
            b=False
            print " Salir del Menu: "

        if p<4:
            raw_input("PRESIONE ENTER PARA VOLVER AL MENU:")

if __name__ == '__main__':
    main()
