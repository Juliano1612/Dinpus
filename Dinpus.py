from tkinter import *
from tkinter import messagebox
from random import *
import random
import os

mainframe = Tk()
mainframe.geometry("850x610+150+150")


tabuleiro = Canvas(mainframe, width=610, height=600, bg="white")
tabuleiro.grid(row = 4, column = 4)

# 1 - Jogador, 2 - Poço, 3 - Wumpus, 4 - Tesouro, 5 - Brisa, 6 - Fedor, 7 - Brisa + Fedor
xPl = 3
yPl = 0
score = 0
wumpusLiving = True
temFlecha = True
getTreasure = False
gameover = False

elementosJogo = [2,2,3,4]
tabuleiroJogo = [[0 for x in range(4)] for y in range(4)]
discoveryMatrix = [[0 for x in range(4)] for y in range(4)]


random.shuffle(elementosJogo)
for x in range(4):
    n = randint(0,3)
    m = randint(0,3)
    while tabuleiroJogo[n][m] != 0 or (n == 3 and m == 0) or (n == 2 and m == 0) or (n == 3 and m == 1):
        n = randint(0, 3)
        m = randint(0, 3)
    tabuleiroJogo[n][m] = elementosJogo[x]
tabuleiroJogo[3][0] = 1
discoveryMatrix[3][0] = 1

print(tabuleiroJogo[0])
print(tabuleiroJogo[1])
print(tabuleiroJogo[2])
print(tabuleiroJogo[3])
print("")

for x in range(0,4):
    for y in range(0,4):
        if tabuleiroJogo[x][y] == 2:#poço
            if x == 0:#primeira linha
                if y == 0:#primeira coluna
                    if tabuleiroJogo[x+1][y] == 0 :#cell de baixo vazia
                        tabuleiroJogo[x+1][y] = 5
                    if tabuleiroJogo[x][y+1] == 0:#cell da direita vazia
                        tabuleiroJogo[x][y+1] = 5
                    if tabuleiroJogo[x+1][y] == 6 :#cell de baixo com fedor
                        tabuleiroJogo[x+1][y] = 7
                    if tabuleiroJogo[x][y+1] == 6:#cell da direita com fedor
                        tabuleiroJogo[x][y+1] = 7
                elif y == 3:#ultima coluna
                    if tabuleiroJogo[x+1][y] == 0 :#cell de baixo vazia
                        tabuleiroJogo[x+1][y] = 5
                    if tabuleiroJogo[x][y-1] == 0:#cell da esquerda vazia
                        tabuleiroJogo[x][y-1] = 5
                    if tabuleiroJogo[x+1][y] == 6 :#cell de baixo com fedor
                        tabuleiroJogo[x+1][y] = 7
                    if tabuleiroJogo[x][y-1] == 6:#cell da esquerda com fedor
                        tabuleiroJogo[x][y-1] = 7
                else:#colunas do meio
                    if tabuleiroJogo[x+1][y] == 0 :#cell de baixo vazia
                        tabuleiroJogo[x+1][y] = 5
                    if tabuleiroJogo[x][y-1] == 0:#cell da esquerda vazia
                        tabuleiroJogo[x][y-1] = 5
                    if tabuleiroJogo[x][y+1] == 0:#cell da direita vazia
                        tabuleiroJogo[x][y+1] = 5
                    if tabuleiroJogo[x+1][y] == 6 :#cell de baixo com fedor
                        tabuleiroJogo[x+1][y] = 7
                    if tabuleiroJogo[x][y-1] == 6:#cell da esquerda com fedor
                        tabuleiroJogo[x][y-1] = 7
                    if tabuleiroJogo[x][y+1] == 6:#cell da direita com fedor
                        tabuleiroJogo[x][y+1] = 7
                        ######################################
            elif x == 3:#ultima linha
                if y == 0:  # primeira coluna
                    if tabuleiroJogo[x - 1][y] == 0:  # cell de cima vazia
                        tabuleiroJogo[x - 1][y] = 5
                    if tabuleiroJogo[x][y + 1] == 0:  # cell da direita vazia
                        tabuleiroJogo[x][y + 1] = 5
                    if tabuleiroJogo[x - 1][y] == 6:  # cell de cima com fedor
                        tabuleiroJogo[x - 1][y] = 7
                    if tabuleiroJogo[x][y + 1] == 6:  # cell da direita com fedor
                        tabuleiroJogo[x][y + 1] = 7
                elif y == 3:  # ultima coluna
                    if tabuleiroJogo[x - 1][y] == 0:  # cell de cima vazia
                        tabuleiroJogo[x - 1][y] = 5
                    if tabuleiroJogo[x][y - 1] == 0:  # cell da esquerda vazia
                        tabuleiroJogo[x][y - 1] = 5
                    if tabuleiroJogo[x - 1][y] == 6:  # cell de cima com fedor
                        tabuleiroJogo[x - 1][y] = 7
                    if tabuleiroJogo[x][y - 1] == 6:  # cell da esquerda com fedor
                        tabuleiroJogo[x][y - 1] = 7
                else:#colunas do meio
                    if tabuleiroJogo[x - 1][y] == 0:  # cell de cima vazia
                        tabuleiroJogo[x - 1][y] = 5
                    if tabuleiroJogo[x][y - 1] == 0:  # cell da esquerda vazia
                        tabuleiroJogo[x][y - 1] = 5
                    if tabuleiroJogo[x][y + 1] == 0:  # cell da direita vazia
                        tabuleiroJogo[x][y + 1] = 5
                    if tabuleiroJogo[x - 1][y] == 6:  # cell de cima com fedor
                        tabuleiroJogo[x - 1][y] = 7
                    if tabuleiroJogo[x][y - 1] == 6:  # cell da esquerda com fedor
                        tabuleiroJogo[x][y - 1] = 7
                    if tabuleiroJogo[x][y + 1] == 6:  # cell da direita com fedor
                        tabuleiroJogo[x][y + 1] = 7
                        #######################################
            else:#linhas do meio
                if y == 0:  # primeira coluna
                    if tabuleiroJogo[x - 1][y] == 0:  # cell de cima vazia
                        tabuleiroJogo[x - 1][y] = 5
                    if tabuleiroJogo[x + 1][y] == 0:  # cell de baixo vazia
                        tabuleiroJogo[x + 1][y] = 5
                    if tabuleiroJogo[x][y + 1] == 0:  # cell da direita vazia
                        tabuleiroJogo[x][y + 1] = 5
                    if tabuleiroJogo[x - 1][y] == 6:  # cell de cima com fedor
                        tabuleiroJogo[x - 1][y] = 7
                    if tabuleiroJogo[x + 1][y] == 6:  # cell de baixo com fedor
                        tabuleiroJogo[x + 1][y] = 7
                    if tabuleiroJogo[x][y + 1] == 6:  # cell da direita com fedor
                        tabuleiroJogo[x][y + 1] = 7
                elif y == 3:  # ultima coluna
                    if tabuleiroJogo[x - 1][y] == 0:  # cell de cima vazia
                        tabuleiroJogo[x - 1][y] = 5
                    if tabuleiroJogo[x + 1][y] == 0:  # cell de baixo vazia
                        tabuleiroJogo[x + 1][y] = 5
                    if tabuleiroJogo[x][y - 1] == 0:  # cell da esquerda vazia
                        tabuleiroJogo[x][y - 1] = 5
                    if tabuleiroJogo[x - 1][y] == 6:  # cell de cima com fedor
                        tabuleiroJogo[x - 1][y] = 7
                    if tabuleiroJogo[x + 1][y] == 6:  # cell de baixo com fedor
                        tabuleiroJogo[x + 1][y] = 7
                    if tabuleiroJogo[x][y - 1] == 6:  # cell da esquerda com fedor
                        tabuleiroJogo[x][y - 1] = 7
                else:#colunas do meio
                    if tabuleiroJogo[x - 1][y] == 0:  # cell de cima vazia
                        tabuleiroJogo[x - 1][y] = 5
                    if tabuleiroJogo[x + 1][y] == 0:  # cell de baixo vazia
                        tabuleiroJogo[x + 1][y] = 5
                    if tabuleiroJogo[x][y - 1] == 0:  # cell da esquerda vazia
                        tabuleiroJogo[x][y - 1] = 5
                    if tabuleiroJogo[x][y + 1] == 0:  # cell da direita vazia
                        tabuleiroJogo[x][y + 1] = 5
                    if tabuleiroJogo[x - 1][y] == 6:  # cell de cima com fedor
                        tabuleiroJogo[x - 1][y] = 7
                    if tabuleiroJogo[x + 1][y] == 6:  # cell de baixo com fedor
                        tabuleiroJogo[x + 1][y] = 7
                    if tabuleiroJogo[x][y - 1] == 6:  # cell da esquerda com fedor
                        tabuleiroJogo[x][y - 1] = 7
                    if tabuleiroJogo[x][y + 1] == 6:  # cell da direita com fedor
                        tabuleiroJogo[x][y + 1] = 7

        elif tabuleiroJogo[x][y] == 3:#wumpus
            if x == 0:  # primeira linha
                if y == 0:  # primeira coluna
                    if tabuleiroJogo[x + 1][y] == 0:  # cell de baixo vazia
                        tabuleiroJogo[x + 1][y] = 6
                    if tabuleiroJogo[x][y + 1] == 0:  # cell da direita vazia
                        tabuleiroJogo[x][y + 1] = 6
                    if tabuleiroJogo[x + 1][y] == 5:  # cell de baixo com brisa
                        tabuleiroJogo[x + 1][y] = 7
                    if tabuleiroJogo[x][y + 1] == 5:  # cell da direita com fedor
                        tabuleiroJogo[x][y + 1] = 7
                elif y == 3:  # ultima coluna
                    if tabuleiroJogo[x + 1][y] == 0:  # cell de baixo vazia
                        tabuleiroJogo[x + 1][y] = 6
                    if tabuleiroJogo[x][y - 1] == 0:  # cell da esquerda vazia
                        tabuleiroJogo[x][y - 1] = 6
                    if tabuleiroJogo[x + 1][y] == 5:  # cell de baixo com brisa
                        tabuleiroJogo[x + 1][y] = 7
                    if tabuleiroJogo[x][y - 1] == 5:  # cell da esquerda com brisa
                        tabuleiroJogo[x][y - 1] = 7
                else:#colunas do meio
                    if tabuleiroJogo[x + 1][y] == 0:  # cell de baixo vazia
                        tabuleiroJogo[x + 1][y] = 6
                    if tabuleiroJogo[x][y - 1] == 0:  # cell da esquerda vazia
                        tabuleiroJogo[x][y - 1] = 6
                    if tabuleiroJogo[x][y + 1] == 0:  # cell da direita vazia
                        tabuleiroJogo[x][y + 1] = 6
                    if tabuleiroJogo[x + 1][y] == 5:  # cell de baixo com brisa
                        tabuleiroJogo[x + 1][y] = 7
                    if tabuleiroJogo[x][y - 1] == 5:  # cell da esquerda com brisa
                        tabuleiroJogo[x][y - 1] = 7
                    if tabuleiroJogo[x][y + 1] == 5:  # cell da direita com brisa
                        tabuleiroJogo[x][y + 1] = 7
                        ######################################
            elif x == 3:  # ultima linha
                if y == 0:  # primeira coluna
                    if tabuleiroJogo[x - 1][y] == 0:  # cell de cima vazia
                        tabuleiroJogo[x - 1][y] = 6
                    if tabuleiroJogo[x][y + 1] == 0:  # cell da direita vazia
                        tabuleiroJogo[x][y + 1] = 6
                    if tabuleiroJogo[x - 1][y] == 5:  # cell de cima com brisa
                        tabuleiroJogo[x - 1][y] = 7
                    if tabuleiroJogo[x][y + 1] == 5:  # cell da direita com brisa
                        tabuleiroJogo[x][y + 1] = 7
                elif y == 3:  # ultima coluna
                    if tabuleiroJogo[x - 1][y] == 0:  # cell de cima vazia
                        tabuleiroJogo[x - 1][y] = 6
                    if tabuleiroJogo[x][y - 1] == 0:  # cell da esquerda vazia
                        tabuleiroJogo[x][y - 1] = 6
                    if tabuleiroJogo[x - 1][y] == 5:  # cell de cima com brisa
                        tabuleiroJogo[x - 1][y] = 7
                    if tabuleiroJogo[x][y - 1] == 5:  # cell da esquerda com brisa
                        tabuleiroJogo[x][y - 1] = 7
                else:#colunas do meio
                    if tabuleiroJogo[x - 1][y] == 0:  # cell de cima vazia
                        tabuleiroJogo[x - 1][y] = 6
                    if tabuleiroJogo[x][y - 1] == 0:  # cell da esquerda vazia
                        tabuleiroJogo[x][y - 1] = 6
                    if tabuleiroJogo[x][y + 1] == 0:  # cell da direita vazia
                        tabuleiroJogo[x][y + 1] = 6
                    if tabuleiroJogo[x - 1][y] == 5:  # cell de cima com brisa
                        tabuleiroJogo[x - 1][y] = 7
                    if tabuleiroJogo[x][y - 1] == 5:  # cell da esquerda com brisa
                        tabuleiroJogo[x][y - 1] = 7
                    if tabuleiroJogo[x][y + 1] == 5:  # cell da direita com brisa
                        tabuleiroJogo[x][y + 1] = 7
                        #######################################
            else:#linhas do meio
                if y == 0:  # primeira coluna
                    if tabuleiroJogo[x - 1][y] == 0:  # cell de cima vazia
                        tabuleiroJogo[x - 1][y] = 6
                    if tabuleiroJogo[x + 1][y] == 0:  # cell de baixo vazia
                        tabuleiroJogo[x + 1][y] = 6
                    if tabuleiroJogo[x][y + 1] == 0:  # cell da direita vazia
                        tabuleiroJogo[x][y + 1] = 6
                    if tabuleiroJogo[x - 1][y] == 5:  # cell de cima com brisa
                        tabuleiroJogo[x - 1][y] = 7
                    if tabuleiroJogo[x + 1][y] == 5:  # cell de baixo com brisa
                        tabuleiroJogo[x + 1][y] = 7
                    if tabuleiroJogo[x][y + 1] == 5:  # cell da direita com brisa
                        tabuleiroJogo[x][y + 1] = 7
                elif y == 3:  # ultima coluna
                    if tabuleiroJogo[x - 1][y] == 0:  # cell de cima vazia
                        tabuleiroJogo[x - 1][y] = 6
                    if tabuleiroJogo[x + 1][y] == 0:  # cell de baixo vazia
                        tabuleiroJogo[x + 1][y] = 6
                    if tabuleiroJogo[x][y - 1] == 0:  # cell da esquerda vazia
                        tabuleiroJogo[x][y - 1] = 6
                    if tabuleiroJogo[x - 1][y] == 5:  # cell de cima com brisa
                        tabuleiroJogo[x - 1][y] = 7
                    if tabuleiroJogo[x + 1][y] == 5:  # cell de baixo com brisa
                        tabuleiroJogo[x + 1][y] = 7
                    if tabuleiroJogo[x][y - 1] == 5:  # cell da esquerda com brisa
                        tabuleiroJogo[x][y - 1] = 7
                else:#colunas do meio
                    if tabuleiroJogo[x - 1][y] == 0:  # cell de cima vazia
                        tabuleiroJogo[x - 1][y] = 6
                    if tabuleiroJogo[x + 1][y] == 0:  # cell de baixo vazia
                        tabuleiroJogo[x + 1][y] = 6
                    if tabuleiroJogo[x][y - 1] == 0:  # cell da esquerda vazia
                        tabuleiroJogo[x][y - 1] = 6
                    if tabuleiroJogo[x][y + 1] == 0:  # cell da direita vazia
                        tabuleiroJogo[x][y + 1] = 6
                    if tabuleiroJogo[x - 1][y] == 5:  # cell de cima com brisa
                        tabuleiroJogo[x - 1][y] = 7
                    if tabuleiroJogo[x + 1][y] == 5:  # cell de baixo com brisa
                        tabuleiroJogo[x + 1][y] = 7
                    if tabuleiroJogo[x][y - 1] == 5:  # cell da esquerda com brisa
                        tabuleiroJogo[x][y - 1] = 7
                    if tabuleiroJogo[x][y + 1] == 5:  # cell da direita com brisa
                        tabuleiroJogo[x][y + 1] = 7



print(tabuleiroJogo[0])
print(tabuleiroJogo[1])
print(tabuleiroJogo[2])
print(tabuleiroJogo[3])


cellsImg = [[0 for x in range(4)] for y in range(4)]
blankimg = PhotoImage()
player = PhotoImage(file = "Images/player90x60.gif")
tesouro = PhotoImage(file = "Images/treasure148x148.gif")
poco = PhotoImage(file = "Images/well148x148.gif")
wumpus = PhotoImage(file = "Images/wumpus148x148.gif")
brisa = PhotoImage(file = "Images/wind148x148.gif")
fedor = PhotoImage(file = "Images/poop148x148.gif")
brisafedor = PhotoImage(file = "Images/windpoop148x148.gif")
arrowIc = PhotoImage(file="Images/arrow100x100.gif")
wumpusIc = PhotoImage(file="Images/wumpus100x100.gif")
treasureIc = PhotoImage(file="Images/treasure100x100.gif")
wumpusDanger = PhotoImage(file="Images/danger60x60.gif")
wumpusSafe = PhotoImage(file="Images/safe60x60.gif")
notreasure = PhotoImage(file="Images/notreasure60x60.gif")
yestreasure = PhotoImage(file="Images/yestreasure60x60.gif")


mainframe.title("Dinpus")

def showTab():
    for x in range(4):
        for y in range(4):
            if tabuleiroJogo[x][y] == 7 and discoveryMatrix[x][y] == 1: #brisa + fedor
                cellsImg[x][y] = Label(tabuleiro, image = brisafedor)
                cellsImg[x][y].image = brisafedor
                cellsImg[x][y].grid(row = x, column = y)
            elif tabuleiroJogo[x][y] == 6 and discoveryMatrix[x][y] == 1: #fedor
                cellsImg[x][y] = Label(tabuleiro, image = fedor)
                cellsImg[x][y].image = fedor
                cellsImg[x][y].grid(row = x, column = y)
            elif tabuleiroJogo[x][y] == 5 and discoveryMatrix[x][y] == 1: #brisa
                cellsImg[x][y] = Label(tabuleiro, image = brisa)
                cellsImg[x][y].image = brisa
                cellsImg[x][y].grid(row = x, column = y)
            elif tabuleiroJogo[x][y] == 4 and discoveryMatrix[x][y] == 1: #tesouro
                cellsImg[x][y] = Label(tabuleiro, image = tesouro)
                cellsImg[x][y].image = tesouro
                cellsImg[x][y].grid(row = x, column = y)
            elif tabuleiroJogo[x][y] == 3 and discoveryMatrix[x][y] == 1: #wumpus
                if(wumpusLiving):
                    cellsImg[x][y] = Label(tabuleiro, image = wumpus)
                    cellsImg[x][y].image = wumpus
                    cellsImg[x][y].grid(row = x, column = y)
                else:
                    cellsImg[x][y] = Label(tabuleiro, image=blankimg, compound=CENTER, width=148, height=148)
                    cellsImg[x][y].grid(row=x, column=y, padx=1, pady=1)
            elif tabuleiroJogo[x][y] == 2 and discoveryMatrix[x][y] == 1: #poco
                cellsImg[x][y] = Label(tabuleiro, image = poco)
                cellsImg[x][y].image = poco
                cellsImg[x][y].grid(row = x, column = y)
            #elif tabuleiroJogo[x][y] == 1 and discoveryMatrix[x][y] == 1: #player
             #   cellsImg[x][y] = Label(tabuleiro, image = player)
             #   cellsImg[x][y].image = player
             #   cellsImg[x][y].grid(row = x, column = y)
            else:
                cellsImg[x][y] = Label(tabuleiro, image = blankimg, compound = CENTER, width = 148, height = 148)
                cellsImg[x][y].grid(row = x, column = y, padx = 1, pady = 1)

    jogador = Label(tabuleiro, image=player)
    jogador.image = player
    jogador.place(x=(150*yPl)+10, y=(150*xPl)+60)

    arrow = Label(mainframe, image=arrowIc)
    arrow.image = arrowIc
    arrow.place(x=630, y=150)

    wumpusicon = Label(mainframe, image=wumpusIc)
    wumpusicon.image = wumpusIc
    wumpusicon.place(x=630, y=300)

    treasureicon = Label(mainframe, image=treasureIc)
    treasureicon.image = treasureIc
    treasureicon.place(x=630, y=450)

    scoreTitle = Label(mainframe, text = "SCORE", font="Times 20 bold")
    scoreTitle.place(x=690, y=20)
    scoreValue = Label(mainframe, text=str(score).zfill(4), font="Times 18")
    scoreValue.place(x=710, y=60)

    if wumpusLiving:
        wumpusStats = Label(mainframe, image=wumpusDanger)
        wumpusStats.image = wumpusDanger
        wumpusStats.place(x=730, y=320)
    else:
        wumpusStats = Label(mainframe, image=wumpusSafe)
        wumpusStats.image = wumpusSafe
        wumpusStats.place(x=730, y=320)

    if temFlecha:
        numFlechas = Label(mainframe, text="1", font="Times 20 bold")
        numFlechas.place(x=750, y=180)
    else:
        numFlechas = Label(mainframe, text="0", font="Times 20 bold")
        numFlechas.place(x=750, y=180)

    if getTreasure:
        treasureStats = Label(mainframe, image = yestreasure)
        treasureStats.image = yestreasure
        treasureStats.place(x=740, y=470)
    else:
        treasureStats = Label(mainframe, image=notreasure)
        treasureStats.image = notreasure
        treasureStats.place(x=740, y=470)





def pressUp(self):
    global xPl, yPl, score, gameover
    if not(gameover):
        if xPl != 0:
            score = score-1
            xPl = xPl-1
            discoveryMatrix[xPl][yPl] = 1
            print("Agora estou em " + str(xPl) + " " + str(yPl))
            showTab()
            beRich()
            died()


def pressDown(self):
    global xPl, yPl, score, gameover
    if not(gameover):
        if xPl != 3:
            score = score-1
            xPl = xPl+1
            discoveryMatrix[xPl][yPl] = 1
            print("Agora estou em " + str(xPl) + " " + str(yPl))
            showTab()
            beRich()
            died()


def pressLeft(self):
    global xPl, yPl, score, gameover
    if not(gameover):
        if yPl != 0:
            score = score-1
            yPl = yPl-1
            discoveryMatrix[xPl][yPl] = 1
            print("Agora estou em " + str(xPl) + " " + str(yPl))
            showTab()
            beRich()
            died()


def pressRight(self):
    global xPl, yPl, score, gameover
    if not(gameover):
        if yPl != 3:
            score = score-1
            yPl = yPl+1
            discoveryMatrix[xPl][yPl] = 1
            print("Agora estou em " + str(xPl) + " " + str(yPl))
            showTab()
            beRich()
            died()

def pressR(self):
    print("Restart!")
    mainframe.destroy()
    os.system("python3.5 Dinpus.py")



def pressControlHorizontal(f):
    global xPl, yPl, tabuleiroJogo, wumpusLiving, temFlecha, score
    if temFlecha:
        temFlecha=False
        score = score-9
        if f == 0:#right
            for y in range(yPl, 4):
                if(tabuleiroJogo[xPl][y] == 3):
                    print("Wumpus Killed!")
                    score = score + 1000
                    wumpusLiving=False
        else:
            for y in range(0, yPl):
                if(tabuleiroJogo[xPl][y] == 3):
                    print("Wumpus Killed!")
                    score = score + 1000
                    wumpusLiving=False

def pressControlVertical(f):
    global xPl, yPl, tabuleiroJogo, wumpusLiving, temFlecha, score
    if temFlecha:
        temFlecha=False
        score = score-9
        if f == 0:#up
            for x in range(0, xPl):
                if(tabuleiroJogo[x][yPl] == 3):
                    print("Wumpus Killed!")
                    score = score + 1000
                    wumpusLiving=False
                    showTab()

        else:#down
            for x in range(xPl, 4):
                if(tabuleiroJogo[x][yPl] == 3):
                    print("Wumpus Killed!")
                    score = score + 1000
                    wumpusLiving=False
                    showTab()


def died():
    global xPl, yPl, tabuleiroJogo, gameover, score
    if (tabuleiroJogo[xPl][yPl] == 3 and wumpusLiving) or tabuleiroJogo[xPl][yPl] == 2:
        print("GameOver!")
        score = score -1000
        gameover = True
        showTab()
        messagebox.showinfo("You died!", "Game Over!\nFinal Score :"+ str(score).zfill(4) + "\nPress [r] to restart")

def beRich():
    global xPl, yPl, tabuleiroJogo, getTreasure
    if tabuleiroJogo[xPl][yPl]==4 and not(getTreasure):
        getTreasure = True
        showTab()
        print("You got the treasure!")

def winner(self):
    global xPl, yPl, getTreasure, score, gameover
    print("vamoacaba?")
    if xPl == 3 and yPl == 0:
        if(getTreasure == True):
            score = score+1000
            showTab()
        gameover = True
        messagebox.showinfo("That's All!", "You Win!\nFinal Score :"+ str(score).zfill(4) +"\nPress [r] to restart")




tabuleiro.bind('<Up>', pressUp)
tabuleiro.bind('<Down>', pressDown)
tabuleiro.bind('<Left>', pressLeft)
tabuleiro.bind('<Right>', pressRight)
tabuleiro.bind('<Control-Key-Right>', lambda event: pressControlHorizontal(f = 0))
tabuleiro.bind('<Control-Key-Left>', lambda event: pressControlHorizontal(f = 1))
tabuleiro.bind('<Control-Key-Up>', lambda event: pressControlVertical(f = 0))
tabuleiro.bind('<Control-Key-Down>', lambda event: pressControlVertical(f = 1))
tabuleiro.bind('<Return>', winner)
tabuleiro.bind('<r>', pressR)

tabuleiro.focus_set()


showTab()
mainloop()

