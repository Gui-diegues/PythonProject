from jogo import *
from historico import salvar_resultado, mostrar_historico, mostrar_ranking
from exportador import exportar_ranking_csv

def jogar_uma_partida():
    jogador_X = "Vitória"
    jogador_O = "Guilherme"
    nomes = {"X": jogador_X, "O": jogador_O}

    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"
    mostrar_tabuleiro(tabuleiro)

    while True:
        try:
            print(f"\n{nomes[jogador_atual]}, é sua vez ({jogador_atual}).")
            linha = int(input("Linha (0-2): "))
            coluna = int(input("Coluna (0-2): "))
        except ValueError:
            print("Digite números válidos entre 0 e 2.")
            continue

        if not jogada_valida(tabuleiro, linha, coluna):
            print("Jogada inválida. Tente outra.")
            continue

        tabuleiro[linha][coluna] = jogador_atual
        mostrar_tabuleiro(tabuleiro)

        if verificar_vitoria(tabuleiro, jogador_atual):
            print(f"\n🎉 {nomes[jogador_atual]} venceu!")
            salvar_resultado(f"{nomes[jogador_atual]} venceu com {jogador_atual}")
            break
        elif tabuleiro_cheio(tabuleiro):
            print("\n🤝 Empate!")
            salvar_resultado(f"Empate entre {jogador_X} e {jogador_O}")
            break

        jogador_atual = "O" if jogador_atual == "X" else "X"

def menu():
    while True:
        print("\n=== MENU JOGO DA VELHA ===")
        print("1. Jogar")
        print("2. Ver histórico")
        print("3. Ver ranking")
        print("4. Exportar ranking para CSV")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            jogar_uma_partida()
        elif opcao == "2":
            mostrar_historico()
        elif opcao == "3":
            mostrar_ranking()
        elif opcao == "4":
            exportar_ranking_csv()
        elif opcao == "5":
            print("Até a próxima!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
