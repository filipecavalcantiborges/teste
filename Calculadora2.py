operacao=input("qual operação quer fazer ?: ")
operacao.lower()
primeironum=float(input("primeiro número:"))
segundonum=float(input("segundo número:"))
match operacao:
   case "soma":
      resultado = primeironum + segundonum
      print(f"seu resultado é {round(resultado,2)}")
   case "divisão":
      resultado = primeironum / segundonum
      if segundonum == 0:
         print("operação não é posível!")
      else:
         print(f"seu resultado é {round(resultado,2)}")
   case "potenciação":
      resultado = primeironum ** segundonum
      print(f"seu resultado é {round(resultado,2) }")
   case "subtração":
      resultado = primeironum - segundonum
      print(f"seu resultado é {round(resultado,2)}")
   case _:
      print("operação inválida!")
