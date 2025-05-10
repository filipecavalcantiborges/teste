def a_ser_pago(mp,vp):
    if mp == "dinheiro":
        print(f"o valor a ser pago é {vp * 0.85} com 15% de desconto")
    elif mp == "pix" :
        print(f"o valor a ser pago é {vp * 0.85} com 15% de desconto")
    elif mp == "cartão de crédito":
        print(f"o valor a ser pago é {vp * 0.90} com 10% de desconto")
    elif mp == "cartão 2x":
        print(f"o valor a ser pago é {vp } sem desconto")
    elif mp == "cartão 3x":
        vjuros1 = vp/3 + (vp/3)*0.1
        vjuros2 = vjuros1 + vjuros1*0.1
        print(f"o valor a ser pago é {round(vp/3 + vjuros1 + vjuros2 , 2)}")

valorproduto = float(input("Digite aqui o valor do que você irá comprar: "))
meio_pagamento = input("digite aqui o meio de pagamento que você irá utilizar Dinheiro, pix, cartão de crédito,cartão 2x, cartão 3x: ")
meio_pagamento.lower()
a_ser_pago(meio_pagamento,valorproduto)
