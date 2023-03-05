print("Olá, esse é o programa que calcula médias da faculdade")
print(" ")
ID = int(input('Digite o ID do estudante: '))
nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
me = float(input('Digite a média de exercícios: '))
MA = (nota1 + nota2 * 2 + nota3 * 3 + me )/7
print("A média de aproveitamento do estudante",ID, "foi: ",MA)
if MA < 4:
        print('O conceito é E e o aluno está REPROVADO')
elif MA > 4 and MA < 6:
        print('O conceito é D e o aluno está REPROVADO')
elif MA > 6 and MA < 7.5:
        print('O conceito é C e o aluno está APROVADO')
elif MA > 7.5 and MA < 9:
        print('O conceito é B e o aluno está APROVADO')
elif MA > 9 and MA < 11:
        print('O conceito é A e o aluno está APROVADO')
else: 
        print("Opção inválida")
print('Até o próximo bimestre!')
