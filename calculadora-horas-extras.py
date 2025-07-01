# Nível 1 — Revisão + lógica simples
# 2. Calculadora de salário com horas extras
# Peça ao usuário:
# - O salário base
# - A quantidade de horas trabalhadas no mês
# - As horas extras trabalhadas
# Calcule o valor da hora normal (salário base / 160)
# Calcule o valor da hora extra (1.5x a hora normal)
# Calcule o salário total somando horas normais e extras
# Mostre o salário total formatado com 2 casas decimais

# Exemplo de código:
salario_base = float(input("Digite seu salário base: "))
horas_trabalhadas = float(input("Horas trabalhadas no mês: "))
horas_extras = float(input("Horas extras trabalhadas: "))

valor_hora = salario_base / 160
valor_hora_extra = valor_hora * 1.5

salario_total = (valor_hora * horas_trabalhadas) + (valor_hora_extra * horas_extras)

print(f"Salário total no mês: R$ {salario_total:.2f}")
