# Dicionários
família = {"Ricardo": 60, "Lucia": 61, "Arthur": 35, "Ana Luísa": 23, "Lisa": 18}
print({k: 2024 - v for (k,v) in família.items()})
# Sets
print({s + "USD" for s in ["EUR", "GBP", "BRL", "HKD"]})
# Funções
def converte_celsius(graus, fonte="fahrenheit"):
    if fonte.lower() == "fahrenheit":
        return (graus-32) * (5/9)
    elif fonte.lower() == "kelvin":
        return graus - 273,15
    else:
        return f"Não sei como converter de {fonte}"
    