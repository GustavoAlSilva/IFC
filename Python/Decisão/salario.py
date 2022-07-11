ganho = float(input("Digite quanto você recebe por hora trabalhada: "))
horas = float(input("Digite quantas horas você trabalha por mês: "))
bruto = ganho * horas
imp_renda = (bruto * (11 / 100))
inss = (bruto * (8 / 100))
sindicato = (bruto * (5 / 100))
liquido = bruto - imp_renda - inss - sindicato 
print("Salário bruto: R$", bruto, "\nImposto de renda: R$", imp_renda, "\nINSS: R$", inss, "\nSindicato: R$", sindicato, "\nSalário líquido: R$", liquido)