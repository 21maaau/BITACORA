print("Semana 12: Ejercicio 1")
print("a. Sumatoria")
print("b. factorial")
print("c. Tablas de Multiplicar")
print("d. Numero Perfecto")
opcion=input("Elija una opcion a calcular: ")

match(opcion):
    case "a":
        N=0
        while N<=0:
            N=int(input("Ingrese un numero entero positivo: "))
            if N<0:
                print("El numero ingresado debe ser entero positivo")
            sumatoria=0
            for cont in range(1,N+1):
                sumatoria+=cont #sumatoria=sumatoria+cont
            print("La sumatoria es:",sumatoria)
    case "b":
            N=0
            while N<=0:
                N=int(input("Ingrese un numero entero positivo: "))
                if N<=0:
                    print("El numero ingresado debe ser entero positivo")
            factorial=1
            for cont in range(1,N+1):
                factorial*=cont #factorial=factorial*cont
            print("La factorial es:",factorial)
    case"c":
        for i in range(1,11):
            for j in range(1,11):
                print(i*j,"\t",end='')
            print()
    case "d":
        N=0
        while N<=0:
            N=int(input("Ingrese un numero entero positivo: "))
            if N<=0:
                print("El numero ingresado debe ser entero positivo")
        acumulador=0
        for factor in range(1,N):
            if N%factor==0:
                acumulador+=factor
        if N==acumulador:
            print("Es perfecto")
        else:
            print("No es perfecto")
    case _:
        print("Elija una opcion valida")


