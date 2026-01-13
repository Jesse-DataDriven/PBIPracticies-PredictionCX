# Simulações: Cenários de predição de NPS
print("\n--- Predições de NPS para monitoramento de 85% a 100% ---")

for m in range(85, 101):
    valor = m / 100
    nps_predito = modelo.predict([[valor]])[0]
    print(f"Monitoramento: {m}% → NPS predito: {nps_predito:.2f}")
