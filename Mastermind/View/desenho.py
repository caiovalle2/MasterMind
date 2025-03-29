# Isabella Lopes 
# Caio Valle
# Alexandre Sanson

from Model import *

variante = 45  # Variante para a criação das "bolinhas" do tabuleiro
pontoIni = 55  # Posição inicial para os pontos X e Y
pos_x = 250

# Desenha o tabuleiro do jogo
def desenha_tabuleiro(cnv):
   
    num_tentativas = getNumTentativas()  # Obtém o número máximo possível de tentativas da partida
    lista_cores = getCores()  # Obtém a lista de cores existentes na partida
    num_pinos = len(getSenha())  # Obtém o número de pinos da partida a partir do tamanho da lista da senha

    for i in range(num_tentativas):

        for j in range(num_pinos):

            # Definição dos pontos x e y
            x = 540 - (pontoIni * j) + 90 - pos_x
            y = 620 - (pontoIni * i)
            
            # Desenha as posições dos pinos coloridos
            cnv.create_oval(x, y, x + variante, y + variante, fill = "light gray", outline = "dim gray", width = 2)

            if i < num_tentativas :
                
                # Definição dos pontos x e y (posição das flags)
                x = (pontoIni/2 * j) + 690 - pos_x
                y += (variante/7)
                
                # Desenha as posições dos pinos de flags
                cnv.create_oval(x + variante/4, y + variante/4, x + variante/2, y + variante/2, fill = "light gray", outline = "dim gray", width = 1)

    for i in range(0, len(lista_cores)):

        # Definição dos pontos x e y (posição das cores)
        x = 540 -(pontoIni) - 200 - pos_x
        y = 620 - (pontoIni * i+1)

        # Desenha as posições das cores
        cnv.create_oval(x, y, x + variante, y + variante, fill = lista_cores[i], outline = "dim gray", width = 2)
    return
        

# Faz a comparação da tentativa da rodada do jogador com a senha do jogo
def confere_tentativa():
    global rodada, tentativa
    tent_jogador = getTentativajogador()  # Obtém a lista de tentativas do jogador da partida
    tent_flag = getTentativaflag()  # Obtém a lista de flags da partida
    rodada = getTurno()  # Obtém o número da rodada (turno) da partida
    return

