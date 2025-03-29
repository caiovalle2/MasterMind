# Isabella Lopes 
# Caio Valle
# Alexandre Sanson

from Model import *
from View import *

cor = ''  # Variável cor
tentativa = ['','','','','','']  # Lista das tentativas (ou das posições que devem ser preeenchidas com pinos pelo jogador na rodada)
iniciar = 0
vencedor = 0

# Obtém a cor selecionada pelo jogador e posiciona o pino da cor selecionada no local desejado
def escolher_cor(e):
    global cor, tentativa

    if iniciar == 0 or vencedor == 1:
        return
    
    lista_cores = getCores()  # Obtém a lista de cores da partida
    num_pinos = len(getSenha())  # Obtém o número de pinos da partida a partir do tamanho da lista da senha
    rodada = getTurno()  # Obtém o número da rodada (ou turno)
    x = e.x  # Obtém a posição X do tabuleiro selecionada pelo jogador
    y = e.y  # Obtém a posição Y do tabuleiro selecionada pelo jogador
    
    if rodada == getNumTentativas():
        return
    
    if cor == '':
        for i in range(0, len(lista_cores)):
            # Definição dos pontos x e y (posição das cores)
            corx = 540 - (pontoIni) - 200 - pos_x
            cory = 620 - (pontoIni * i)
            
            # Se o clique for em uma das cores na paleta de cores
            if(x > corx and x < corx + variante and y > cory and y < cory + variante):
                cor = lista_cores[i]  # A variável cor é redefinida com a cor selecionada
                print(cor)
    elif (cor != ''):
        for i in range(0, num_pinos):
            # Definição dos pontos x e y
            corx = 540 - (pontoIni * i) + 90 - pos_x
            cory =  620 - pontoIni * rodada
            
            # Se o clique for dentro de uma das posições disponiveis naquela rodada
            if(x > corx  and x < corx + variante and y > cory  and y < cory + variante ):
                tentativa[i] = cor  # A posição i da lista de tentativas é preenchida com a cor selecionada
                print(i)
                cor = ''  # A variável cor é reinicializada

                # Definição dos pontos x e y
                x = 540 - (pontoIni * i) + 90 - pos_x
                y = 620 - (pontoIni) * rodada
                    
                # Desenha a cor selecionada na posição indicada
                e.widget.create_oval(x, y, x + variante, y + variante, fill = tentativa[i], outline = "dim gray", width = 2)


# Verifica se o jogo pode ser atualizado para a próxima partida e compara a jogada do jogador com a senha
def verifica():
    global rodada, tentativa, cnv, vencedor, texto
    arquivo = open("jogo.txt",'w')
    num_tent = getNumTentativas()
    
    num_pinos = len(getSenha())  # Obtém o número de pinos a partir do tamanho da lista da senha
    if vencedor == 1:
        return
    if '' not in tentativa[:num_pinos]:  # Se todos os espaços disponíveis para alocação dos pinos foi preenchida
        
        rodada = atualiza_rodada(tentativa[:num_pinos])  # A rodada é atualizada
        cnv.delete(texto)
        texto = cnv.create_text(790, 520, fill="black", font="Times 20 italic bold", text="Rodada: " + str(rodada + 1))
        if compara():  # Faz a comparação dos pinos do jogador com a senha e cria as flags da rodada
            # Caso o jogador tenha adivinhado a senha na jogada a mensagem é exibida
            cnv.create_text(900, 400, fill="black", font="Times 20 italic bold", text="Parabéns, você ganhou!")
            vencedor = 1
            arquivo.truncate(0)
            # Desenhamos então as flags pretas
            tentativa_flags = getflags()  # Obtém a lista das flags do jogo
            for j in range(num_pinos):
                
                # Definição dos pontos x e y (posição das flags)
                x = (pontoIni/2 * j) + 690 - pos_x
                y = 620 - (pontoIni * (rodada-1)) + (variante/7)
                    
                # Desenha as posições dos pinos de flags
                if tentativa_flags[j] != ' ':
                    cnv.create_oval(x + variante/4, y + variante/4, x + variante/2, y + variante/2, fill = tentativa_flags[j], outline = "dim gray", width = 1)
            
        elif rodada == num_tent:
            if not compara():  # Caso seja a última rodada e o jogador não adivinhou a senha
                cnv.create_text(900, 400, fill="black", font="Times 20 italic bold", text="Que pena, você perdeu.")
                vencedor = -1
                arquivo.truncate(0)
            
            tentativa_flags = getflags()  # Obtém a lista das flags do jogo
            for j in range(num_pinos):
                
                # Definição dos pontos x e y (posição das flags)
                x = (pontoIni/2 * j) + 690 - pos_x
                y = 620 - (pontoIni * (rodada-1)) + (variante/7)
                    
                # Desenha as posições dos pinos de flags
                if tentativa_flags[j] != ' ':
                    cnv.create_oval(x + variante/4, y + variante/4, x + variante/2, y + variante/2, fill = tentativa_flags[j], outline = "dim gray", width = 1)
        else:  # Caso o jogador não tenha adivinhado a senha e ainda não é a última rodada
            tentativa_flags = getflags()  # Obtém a lista das flags do jogo
            for j in range(num_pinos):
                
                # Definição dos pontos x e y (posição das flags)
                x = (pontoIni/2 * j) + 690 - pos_x
                y = 620 - (pontoIni * (rodada-1)) + (variante/7)
                    
                # Desenha as posições dos pinos de flags
                if tentativa_flags[j] != ' ':
                    cnv.create_oval(x + variante/4, y + variante/4, x + variante/2, y + variante/2, fill = tentativa_flags[j], outline = "dim gray", width = 1)
        tentativa = ['','','','','','']  # A lista da tentativa é reinicializada 
        print(rodada)

    arquivo.close()    


# Reseta a cor escolhida pelo jogador caso seja pressionado "Esc"
def reseta_cor(e):
    global cor
    cor = ''  # Reinicializa a variável cor


# Pega todos os Widgets do jogo
def getCanvas(canvas, novo1, botao1, botao2, botao3, cont, SV, ver):
    global Novo, cnv, btn1, btn2, btn3, salvar, continuar, verificar
    Novo = novo1  # Botão de iniciação do jogo
    cnv = canvas  # Definição do canvas
    btn1 = botao1  # Botão de iniciação de partida com nível 1
    btn2 = botao2  # Botão de iniciação de partida com nível 2
    btn3 = botao3  # Botão de iniciação de partida com nível 3
    salvar = SV  # Botão de salvamento da partida
    continuar = cont  # Botão de continuação da partida salva
    verificar = ver  # Botão de verificação da tentativa do jogador


# Posiciona os botões do nivel quando o novo jogo for clicado
def novo():
    global Novo, cnv, btn1, btn2, btn3, salvar, continuar, verificar, vencedor

    vencedor = 0 
    cnv.delete("all")  # Reinicia a janela
    btn1.place(width = 500, height = 80, x = 350, y = 80)  # Posicionamento do botão de iniciação de partida com nível 1
    btn2.place(width = 500, height = 80, x = 350, y = 180)  # Posicionamento do botão de iniciação de partida com nível 2
    btn3.place(width = 500, height = 80, x = 350, y = 280)  # Posicionamento do botão de iniciação de partida com nível 3
    Novo.place(width = 0, height = 0, x = 700, y = 350)  # Posicionamento do botão de iniciação do jogo
    salvar.place(width = 0, height = 0, x = 700, y = 350)  # Posicionamento do botão de salvamento da partida
    continuar.place(width = 0, height = 0, x = 700, y = 400)  # Posicionamento do botão de continuação da partida salva
    verificar.place(width = 0, height = 0, x = 700, y = 600)  # Posicionamento do botão de verificação da tentativa do jogador


# Reposiciona os botões do jogo de iniciar, salvar e continuar
def posiciona_jogo():
    global Novo, cnv, btn1, btn2, btn3, salvar, continuar, verificar, iniciar, texto, rodada
    rodada = getTurno()
    iniciar = 1
    btn1.place(width = 0, height = 0, x = 500, y = 80)  # Reposicionamento do botão de iniciação de partida com nível 1
    btn2.place(width = 0, height = 0, x = 500, y = 80)  # Reposicionamento do botão de iniciação de partida com nível 2
    btn3.place(width = 0, height = 0, x = 500, y = 80)  # Reposicionamento do botão de iniciação de partida com nível 3
    Novo.place(width = 400, height = 50, x = 700, y = 70)  # Reposicionamento do botão de iniciação do jogo
    salvar.place(width = 400, height = 50, x = 700, y = 140)  # Reposicionamento do botão de salvamento da partida
    continuar.place(width = 400, height = 50, x = 700, y = 210)  # Reposicionamento do botão de continuação da partida salva
    verificar.place(width = 100, height = 50, x = 700, y = 600)  # Reposicionamento do botão de verificação da tentativa do jogador
    cnv.create_rectangle(700,300,1100,550,width = 2)
    texto = cnv.create_text(790, 520, fill="black", font="Times 20 italic bold", text="rodada: " + str(rodada + 1))


# Funções de criar um novo jogo, continuar ou salvar a partida

# Novo jogo com nível 1
def Novo1():
    global cnv
    cnv.delete("all")  # Reinicia a janela
    nvl = 1  # Definição do nível 1
    novo_jogo(nvl)  # Iniciação de jogo com nível 1
    criar_senha()  # Criação da senha aleatória
    desenha_tabuleiro(cnv)  # Desenha o tabuleiro do jogo
    posiciona_jogo()  # Posicionamento dos botões do jogo


# Novo jogo com nível 2
def Novo2():
    global cnv
    cnv.delete("all")  # Reinicia a janela
    nvl = 2  # Definição do nível 2
    novo_jogo(nvl)  # Iniciação de jogo com nível 2
    criar_senha()  # Criação da senha aleatória
    desenha_tabuleiro(cnv)  # Desenha o tabuleiro do jogo
    posiciona_jogo()  # Posicionamento dos botões do jogo


# Novo jogo com nível 3
def Novo3():
    global cnv
    cnv.delete("all")  # Reinicia a janela
    nvl = 3  # Definição do nível 3
    novo_jogo(nvl)  # Iniciação de jogo com nível 3
    criar_senha()  # Criação da senha aleatória
    desenha_tabuleiro(cnv)  # Desenha o tabuleiro do jogo
    posiciona_jogo()  # Posicionamento dos botões do jogo


# Continuar jogada antiga
def continuar():
    global cnv, vencedor

    vencedor = 0
    
    arquivo = open("jogo.txt", "r")

    # Recupera o turno, nível e a senha do jogo
    try:
        turno = int(arquivo.readline())  # Lê a linha do arquivo com o número do turno da jogada salva
    except: #Se o arquivo está vazio, a função é encerrada
        print('Nenhum jogo salvo')
        arquivo.close()
        return  # Lê a linha do arquivo com o número do turno da jogada salva
    nvl = int(arquivo.readline())  # Lê a linha do arquivo com o número representando o nível do jogo
    senha = arquivo.readline().split()  # Lê a linha do arquivo com a senha do jogo
    rodada = 0
    
        

    # Apaga o tabuleiro e cria um novo
    cnv.delete("all")
    novo_jogo(nvl)
    putSenha(senha)
    desenha_tabuleiro(cnv)
    
    # Desenha os pinos das rodadas que foram jogadas
    while(rodada < turno):
        cores = arquivo.readline().split()
        for i in range(len(senha)):
            #Posição dos pinos
            x = 540 - (55 * i) + 90 - 250
            y = 620 - (55)*rodada
                        
            # Desenha as posições dos pinos coloridos
            cnv.create_oval(x, y, x + 45, y + 45, fill = cores[i], outline = "dim gray", width = 2)
            
        cores_flag = arquivo.readline().split()
        for i in range(len(cores_flag)):
                # Definição dos pontos x e y (posição das flags)
                x = (pontoIni/2 * i) + 690 - pos_x
                y = 620 - (55)*rodada + (variante/7)
                
                # Desenha as posições dos pinos de flags
                cnv.create_oval(x + variante/4, y + variante/4, x + variante/2, y + variante/2, fill = cores_flag[i], outline = "dim gray", width = 1)
        

        update_flags(cores_flag)    
        rodada = atualiza_rodada(cores)
        
    
    posiciona_jogo()
    
    arquivo.close()
    print("continuar")


# Salvar partida do jogo
def salvar():
    if (vencedor == 1 or vencedor == -1):
        return
    arquivo = open("jogo.txt",'w')  # Abre o arquivo nomeado "jogo.txt" 
    # Se o arquivo não existir, criará um
    
    

    # Salva o turno, nível e a senha
    arquivo.write(str(getTurno()) + "\n")  # Escreve no arquivo o turno do jogo
    arquivo.write(str(getNivel()) + "\n")  # Escreve no arquivo o nível do jogo
    arquivo.write(' '.join(getSenha()) + "\n")  # Escreve no arquivo a senha do jogo
    
    for i in range(getNumTentativas()):  # Escreve no arquivo as tentativas do jogador e as flags
        arquivo.write(' '.join(getTentativajogador()[i]) + "\n")
        tentativa_flag = getTentativaflag()[i]
        tentativa_flag.sort(reverse=True)
        arquivo.write(' '.join(tentativa_flag) + "\n")

    arquivo.close()
    print("salvar")
