# Isabella Lopes 
# Caio Valle
# Alexandre Sanson

from tkinter import *
from Model import *
from View import *
from Controller import *


# Inicia a Janela Inicial    
menu_inicial = Tk()
menu_inicial.title('Mastermind')
cnv = Canvas(menu_inicial, bg = "white", height = 700, width = 1200)

# Botões da Janela Inicial
Novo = Button(menu_inicial, text ="Novo jogo", command = novo, activebackground="light green", bg = 'green', font ='Arial', fg = 'white', bd = '0')
N1 = Button(menu_inicial, text ="Nível 1", command = Novo1, activebackground="light green",bg = 'green', font ='Arial', fg = 'white', bd = '0')
N2 = Button(menu_inicial, text ="Nível 2", command = Novo2, activebackground="light green",bg = 'green', font ='Arial', fg = 'white', bd = '0')
N3 = Button(menu_inicial, text ="Nível 3", command = Novo3, activebackground="light green",bg = 'green', font ='Arial', fg = 'white', bd = '0')
SV = Button(menu_inicial, text ="Salvar partida", command = salvar, activebackground="light green",bg = 'green', font ='Arial', fg = 'white', bd = '0')
CT = Button(menu_inicial, text ="Continuar partida salva", command = continuar, activebackground="light green",bg = 'green', font ='Arial', fg = 'white', bd = '0')

# Posiciona os botões de inicio e continua
Novo.place(width = 500, height = 80, x = 350, y = 100)
CT.place(width = 500, height = 80, x = 350, y = 200)

# Escolhe a cor e a posição na rodada
cnv.bind('<Button-1>', escolher_cor)

menu_inicial.bind('<Escape>', reseta_cor)

# Botão que verifica a tentativa do jogdador
verificar = Button(text = 'Verificar', command = verifica, bg = 'blue', font ='Arial', fg = 'white', bd = '0')

getCanvas(cnv, Novo, N1, N2, N3, CT, SV, verificar)

cnv.pack()
menu_inicial.mainloop()
