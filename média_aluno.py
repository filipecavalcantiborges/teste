def medianota(n1,n2,n3,n4):
    media = int(('n1' + n2 + n3 + n4)/4)
    print(f"a média do aluno {aluno} é {media}")
    if 7 >media:
        print(f"o aluno {aluno} esta reprovado! ")
    elif media > 7:
        print(f"o aluno {aluno} esta aprovado!")

aluno = input("digite aqui o nome do aluno: ")
nota1 = int(input("digite aqui a primeira nota de seu aluno: "))
nota2 = int(input("digite aqui a segunda nota de seu aluno: "))
nota3 = int(input("digite aqui a terceira nota de seu aluno: "))
nota4 = int(input("digite aqui a quarta nota de seu aluno: "))
medianota(nota1,nota2,nota3,nota4)