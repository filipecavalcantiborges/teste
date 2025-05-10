def decrescente(num1,num2,num3):
    lista0=[]
    if num1 > num2 and num1 > num3:
        lista0.append(num1)
        if num2 > num3:
            lista0.append(num2)
            lista0.append(num3)
        else:
            lista0.append(num3)
            lista0.append(num2)
    if num2 > num1 and num2 > num3:
        lista0.append(num2)
        if num1 > num3:
            lista0.append(num1)
            lista0.append(num3)
        else:
            lista0.append(num3)
            lista0.append(num1)
    if num3 > num1 and num3 > num2:
        lista0.append(num3)
        if num1 > num2:
            lista0.append(num1)
            lista0.append(num2)
        else:
            lista0.append(num2)
            lista0.append(num1)
        
    print(lista0)

a=float(input("digite um número: "))
b=float(input("digite o segundo número:"))
c=float(input("digite o terceiro número:"))
decrescente(a,b,c)