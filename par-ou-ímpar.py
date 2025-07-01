# Nível 1 — Revisão + lógica simples
# 3. Verificar se um número é par ou ímpar
# Peça ao usuário um número inteiro
# Verifique se o número é par (divisível por 2) ou ímpar
# Exiba a mensagem correspondente:
# - "O número é par." se o resto da divisão por 2 for 0
# - "O número é ímpar." caso contrário

# Exemplo de código:
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
