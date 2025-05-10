peso=float(input("digite aqui seu peso: "))
print("ok vamos calcular seu IMC!!")
if  18.5 > peso:
    print("você esta abaixo do peso ")
elif 18.5 < peso < 24.9:
    print("você esta no peso ideal")
elif 25 < peso < 29.9 :
    print("você esta levemente acima do peso ")
elif 30 < peso< 34.9:
    print("voce esta obeso grau 1")
elif 35 < peso < 39.9:
    print("você esta obeso grau 2 (severo)")
elif  peso > 40 :
    print("vôce esta obeso grau 3 (mórbido), ta gordo hein !!!")
print("independente de qualquer coisa vá treinar e se cuidar!!!")