# Isabella Lopes 
# Caio Valle
# Alexandre Sanson

from random import shuffle

__all__ = ['novo_jogo', 'criar_senha', 'nivel', 'compara','atualiza_rodada','getflags','getCores','getNumTentativas','getSenha','putSenha','getTurno','getNivel','getTentativajogador','getTentativaflag','update_flags']


def novo_jogo(nvl):
    #Reinicia todas as variáveis para valores bases
    global senha, tentativas, cores, turno, tentativas_flags, tentativas_jogador, niveljogo
    tentativas = 8 # Número máximo de tentativas possíveis
    senha = [] # Senha do jogo
    cores = ["green", "pink", "blue", "red", "purple", "yellow"] # Lista das cores
    tentativas_jogador = [[" ", " ", " ", " "] for x in range(tentativas)] # Lista das tentativas do jogador
    tentativas_flags = [[" ", " ", " ", " "] for x in range(tentativas)] # Lista das flags (pinos brancos e pretos)
    turno = 0; # Número do turno do jogo
    niveljogo = nvl
    nivel(nvl)
    return tentativas


def criar_senha():
    #Cria uma nova senha aleatória
    global senha, cores
    sel = []  # Lista da senha
    for i in cores:
        sel.extend(cores)
    shuffle(sel)
    senha = sel[0:len(cores)-2]
    return senha


def nivel(nvl):
    #Adapta as variáveis de acordo com o nível
    global tentativas, cores, nivel, tentativas_jogador, tentativas_flags

    if(nvl >= 2):
        cores.append("brown")
        tentativas = 10
        for i in range(0,len(tentativas_jogador)):
            tentativas_jogador[i].append(" ")
            tentativas_flags[i].append(" ")
        tentativas_jogador.extend([[" ", " ", " ", " "," "],[" ", " ", " ", " "," "]])
        tentativas_flags.extend([[" ", " ", " ", " "," "],[" ", " ", " ", " "," "]])
    if(nvl == 3):
        cores.append("black")
        tentativas = 12
        for i in range(0,len(tentativas_jogador)):
            tentativas_jogador[i].append(" ")
            tentativas_flags[i].append(" ")
        tentativas_jogador.extend([[" ", " ", " ", " "," "," "],[" ", " ", " ", " "," "," "]])
        tentativas_flags.extend([[" ", " ", " ", " "," "," "],[" ", " ", " ", " "," "," "]])
    return


def atualiza_rodada(ten):
    #Função responsável de guardar as tentativas do jogador e mudar o turno
    global tentativas_jogador,turno

    tentativas_jogador[turno] = ten
    turno += 1
    if turno > tentativas:
        turno = -1
    return turno


def getflags():
    #Pega os flags da rodada (os primeiros pinos devem ser pretos)
    global tentativas_flags, turno
    flags =  tentativas_flags[turno - 1]
    flags.sort(reverse = True)
    return flags

def update_flags(lst):
    global tentativas_flags
    
    tentativas_flags[turno] = lst
    return 

def compara():
    #Compara os N valores da tentativas_jogador com a senha e criando os flags da rodada.
    global tentativas_flags, tentativas_jogador, senha, turno
    atual = turno - 1
    lista = []
    for i in range(0,len(senha)):
        if tentativas_jogador[atual][i] == senha[i]:
            tentativas_flags[atual][i] = "black"
            lista.append(tentativas_jogador[atual][i])
        elif tentativas_jogador[atual][i] in senha and tentativas_jogador[atual][i] not in tentativas_jogador[atual][i+1:]:
            if tentativas_jogador[atual][i] not in lista:
                tentativas_flags[atual][i] = "white"
    
    if tentativas_jogador[atual] == senha:
        return 1
    else:
        return 0


def getNumTentativas(): #Obtém o número de tentativas possíveis da partida
    global tentativas
    return tentativas


def getNumPinos(): #Obtém o número de pinos
    global cores
    return len(cores)


def getCores(): #Obtém a lista de cores
    global cores
    return cores


def getSenha(): #Obtém a senha do jogo
    return senha


def putSenha(val): #Redefine a senha a partir da senha da rodada salva
    global senha
    senha = val


def getTurno(): #Obtém o turno do jogo
    return turno


def getNivel(): #Obtém o nível do jogo
    return niveljogo


def getTentativajogador(): #Obtém as tentativas do jogador
    return tentativas_jogador


def getTentativaflag(): #Obtém as flags
    return tentativas_flags