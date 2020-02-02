from random import randint
from celle import Cell

'''Oblig 7 - IN1000. Student: David Andreas Bordvik.
Denne klassen utgjør selve spillbrettet i Game Of Life spillet'''

class GameBoard:
    ''' Konstuktør'''
    def __init__( self , width, height):
        self._width = width #Brettets bredde
        self._height = height #Brettets høyde
        self._generationNumber = 0 #Cellegenerasjon
        self._board = [] #Selve brettet
        self._newGenBoard = [] #Neste generasjons brett
        self._nAlive = 0 #Antall levende celler

        ##For løkke for å bygge opp en to-dimensjonal liste som representerer brettet basert på brettets høyde og bredde
        for i in range (0,width):
            self._board.append([]) #Lager en ny dimensjone for hver kollonne
            self._newGenBoard.append([])  #Neste generasjons-brett må ha lik dimensjon som selve brettet.

        ##For løkke som putter nye unike celler inn i hvert element i listen (i brettet). Tilsvarende for neste generasjon.
        for x in range(0,width):
            for y in range(0,height):
                newCell = Cell() #Ny unik celle for brettet
                newGenCell = Cell() #Ny unik celle for neste generasjon
                self._board[x].append(newCell) #Legger til en ny Celle på hver plass i listen
                self._newGenBoard[x].append(newGenCell) #Legger til en ny Celle på hver plass i listen for neste generasjon
        self.generateCellStatus() #Setter initiell cellestatus (død eller levende).

    ''' Metode for å tegne brettet'''
    def drawBoard( self ):
        for x in range(self._height):
            for y in range(self._width):
                print(self._board[y][x].getStatusSign(), end=' ')
            print(" ")


    ''' Metoden setter cellestatus slik at det kun står 1 beacon på brettet. Brette må ha minst en størrelse på 4x4'''
    def setBeacon(self):
        if(self._width>3 and self._height>3):
            for x in range(self._width):
                for y in range(self._height):
                    self._board[x][y].setDead() #Setter først alle celler til å være døde
            ##Bygger opp en beacon på brettet
            self._board[0][0].setAlive()
            self._board[1][0].setAlive()
            self._board[0][1].setAlive()
            self._board[3][2].setAlive()
            self._board[2][3].setAlive()
            self._board[3][3].setAlive()
            self._nAlive = 6 #Kun en beacon står på brettet => instansvariabel for antall levende celler blir 6
        else:
            print("Ikke mulig å sette en beacon på på brettet, da brettet er for lite. Må minst være rt 4x4 brett")

    ''' Metoden finner antall naboer til cellen på koordinat x,y gitt via parameterlisten. 
        Returnere en ny 3x3 liste med som inneholder alle naboer'''
    def findNeighbors( self , x, y):
        neighborsList = []
        x2 = x-1 #Translasjon av x til ny startpos med x som utgangspunkt
        y2 = y-1 #Translasjon av y til ny startpos med y som utgangspunkt

        for nyListe in range(3):
            neighborsList.append([]) #Bygger opp en liste slik at det blir en to-dimensjonal 3x3 liste for naboer

        # for i_x in [x-1,x,x+1]: # Alternativ måte å iterere igjennom x-retning for en 3x3 matrise. DENNE ER IKKE BRUKT!
        for i_x in range(3): #itererer igjennom x-retning
            for i_y in range(3): #itererer igjennom y-retning
                if(((x2+i_x)>=0) and ((x2+i_x)< self._width)): #Betingelse for å sjekke alle kantene for x-retning
                    if(((y2+i_y)>=0) and ((y2+i_y)< self._height)): #Betingelse for å sjekke alle kantene for x-retning
                        ##Er i lovlig område
                        if((i_x==1)and(i_y==1)): #Sjekker om man er på "denne" cellen
                            neighborsList[i_x].append(None)# "Denne" (Seg selv) cellen skal ikke inkluderes blandt naboer.
                        else:
                            neighborsList[i_x].append(self._board[x2+i_x][y2+i_y])##Legger naboceller fra brett inn i ny liste
                    else:
                        neighborsList[i_x].append(None)#Legger cell fra brett inn i ny liste
                else:
                    neighborsList[i_x].append(None)#Legger cell fra brett inn i ny liste
        return neighborsList

    ''' Metoden returnere hvilket generasjonsnummer som er gjeldende'''
    def getGeneration(self):
        return self._generationNumber

