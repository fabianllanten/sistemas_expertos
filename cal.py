flag="si"
while flag!="no":

    print ''' 
<---CALCULADORA BASICA--->
1) SUMAR
2) RESTAR
3) MULTIPLICAR
4) DIVIDIR'''

    def suma(num1, num2):   
        print("la suma de los dos numeros es "+str(int(num1+num2)))
    def restar(num1, num2):   
        print("la resta de los dos numeros es "+str(int(num1-num2)))
    def multiplicar(num1, num2):   
        print("la multiplicacion de los dos numeros es "+str(int(num1*num2))) 
    def dividir(num1, num2):   
        print("la divicion de los dos numeros es "+str(int(num1/num2)))

    opcion=input("Ingrese el numero de su opcion: ")
    if opcion>4:
        print("ingrese una opcion valida")
    else:  
        if opcion>0 and opcion<5:
            num1 = int(input("ingrese el primer numero"))
            num2 = int(input("ingrese el segundo numero"))
            if opcion == 1:
                suma(num1, num2)
            elif opcion == 2:
                restar(num1, num2)
            elif opcion == 3:
                multiplicar(num1, num2)
            elif opcion == 4:
                if num2==0:
                    print "error"
                else:
                    dividir(num1,num2)
        flag=raw_input("Desea hacer otra operacion? [Si/No]: ")
    









 



    
   



