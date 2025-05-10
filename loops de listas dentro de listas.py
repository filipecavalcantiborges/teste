notas_alunos=[]
for x in range(3):
    rm=str(input("Qual o RM do aluno?: "))
    nota=float(input("Qual a nota do aluno?: "))
    ident_e_nota=[rm, nota]
    notas_alunos.append(ident_e_nota)

for x in notas_alunos:
    rm=x[0]
    print("O RM do aluno é =>",rm)
    rm=x[1]
    print(" e essas é sua nota ",rm)