def criar_tabuleiro():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tabuleiro(tabuleiro):
    print("\n  0 1 2")
    for i, linha in enumerate(tabuleiro):
        print(f"{i} {'|'.join(linha)}")
        if i < 2:
            print("  -----")

def verificar_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all(c == jogador for c in linha):
            return True
    for col in range(3):
        if all(tabuleiro[l][col] == jogador for l in range(3)):
            return True
    if all(tabuleiro[i][i] == jogador for i in range(3)) or all(tabuleiro[i][2-i] == jogador for i in range(3)):
        return True
    return False

def tabuleiro_cheio(tabuleiro):
    return all(c != " " for linha in tabuleiro for c in linha)

def jogada_valida(tabuleiro, linha, coluna):
    return 0 <= linha <= 2 and 0 <= coluna <= 2 and tabuleiro[linha][coluna] == " "
