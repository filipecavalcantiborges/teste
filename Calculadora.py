operação=str(input("Diga Qual operação você quer fazer? "))
operação.lower()

print(f"a operação que vamos fazer é {operação}")
    
val1=float(input("digite um valor para fazer a operação: "))
val2=float(input("digite o segundo valor para fazer a operação: "))

if operação == "soma":
    print(val1 +val2)

elif operação  in [ "sub" , "subtração" , 
"subtracao" ]:
    print(val1 - val2)

elif operação in ["multiplicação" , "multi" , "multiplicacao" ]:
    print(val1 * val2)
    
elif operação in ["div" ,"divisao" , "divisão"]:
    print (round((val1 / val2), 2))
    
elif operação in ["potencia" , "potenciacao" , "potenciação" , "pot" ]:
    print(val1 ** val2)





