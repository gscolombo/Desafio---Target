sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
others = 19849.53

total = sp + rj + mg + es + others
def percent(n, t):
    return (n/t) * 100

print(f"São Paulo: {percent(sp, total):.0f}%")
print(f"Rio de Janeiro: {percent(rj, total):.0f}%")
print(f"Minas Gerais: {percent(mg, total):.0f}%")
print(f"Espírito Santo: {percent(es, total):.0f}%")
print(f"Outros: {percent(others, total):.0f}%")