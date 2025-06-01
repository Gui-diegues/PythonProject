def salvar_resultado(resultado):
    with open("resultados_jogo_da_velha.txt", "a") as f:
        f.write(resultado + "\n")

def mostrar_historico():
    print("\n📜 Histórico de partidas:")
    try:
        with open("resultados_jogo_da_velha.txt", "r") as f:
            linhas = f.readlines()
            if not linhas:
                print("Nenhuma partida registrada.")
            else:
                for i, linha in enumerate(linhas, 1):
                    print(f"{i}. {linha.strip()}")
    except FileNotFoundError:
        print("Ainda não há histórico.")

def contar_vitorias():
    v_vitoria = 0
    v_guilherme = 0
    empates = 0

    try:
        with open("resultados_jogo_da_velha.txt", "r") as f:
            for linha in f:
                if "Vitória" in linha and "venceu" in linha:
                    v_vitoria += 1
                elif "Guilherme" in linha and "venceu" in linha:
                    v_guilherme += 1
                elif "Empate" in linha:
                    empates += 1
    except FileNotFoundError:
        pass

    return v_vitoria, v_guilherme, empates

def mostrar_ranking():
    v_vitoria, v_guilherme, empates = contar_vitorias()
    print("\n🏆 Ranking:")
    print(f"Vitória (X): {v_vitoria} vitórias")
    print(f"Guilherme (O): {v_guilherme} vitórias")
    print(f"Empates: {empates}")
