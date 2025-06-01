import csv
from historico import contar_vitorias

def exportar_ranking_csv():
    v_vitoria, v_guilherme, empates = contar_vitorias()

    with open("ranking_jogo_da_velha.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Jogador", "Vitórias"])
        writer.writerow(["Vitória", v_vitoria])
        writer.writerow(["Guilherme", v_guilherme])
        writer.writerow(["Empates", empates])

    print("\n✅ Ranking exportado para 'ranking_jogo_da_velha.csv'.")
