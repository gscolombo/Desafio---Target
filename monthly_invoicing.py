from json import load

data = load(open(".\dados.json"))

invoices = []
for reg in data:
    invoices.append(reg["valor"])


min_invoicing = min(invoices)
max_invoicing = max(invoices)
avg_invoicing = sum(invoices) / len(invoices)

number_of_days = 0
for value in invoices:
    if value> avg_invoicing:
        number_of_days += 1

print(f"Menor valor de faturamento: {min_invoicing}")
print(f"Maior valor de faturamento: {max_invoicing}")
print(f"Faturamento médio no mês: {avg_invoicing}")
print(f"Número de dias no mês com valor de faturamento acima da média do mês: {number_of_days}")