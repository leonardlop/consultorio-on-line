# ejemplo uso de condicionales if,else ,elif 
#if - si  else -si ,no  elif - si no ,si
# operadores de comparacion < ,> = , >= ,<=,==, !=


#entradas

# edad = input ( "por favor digite su edad: ")
# edad = int(edad)
edad = int(input ( "por favor digite su edad: "))




#transformacion

if edad >= 18:
    # si la salida es verdadera
    print("usted es mayor de edad")
    print("puede comprar licor")
    if edad >= 60:
        print("por favor pase ala caja rapida")
        condicion = input("presenta algun tipo de discapacidad (si - no)")
        if condicion == "si":
            print( "paso por el si")
        else :
            print ("paso por el no")



    else:
        print("por favor espere en fila general")

else:
    # si la salida es falsa
    print("usted es menor de edad")
    print("usted no puede comprar licor")



    

#salidas


