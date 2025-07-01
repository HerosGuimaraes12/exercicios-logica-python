
# exercicios-logica-python
# Nível 1 — Revisão + lógica simples
# 1. Aprovado ou reprovado?
# Peça ao usuário três notas (0 a 10), calcule a média e diga:
# "Aprovado" se a média for maior ou igual a 7
# "Recuperação" se for entre 5 e 6.9
# "Reprovado" se for menor que 5

# Exemplo de código:
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")

    
