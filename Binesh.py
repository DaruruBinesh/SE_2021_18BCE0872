
"""
      Student Name :  Binesh Daruru
            Reg.No :  18BCE0872
            Campus :  ( VIT ) Vellore Institute of Technology, Vellore
 Applying job Role : Software Engineer role
  Applying Company : Hitwicket
  Coding Test Name : Hitwicket | Live Programming Test Instructions for developers
  
"""

import itertools
WHITE = "white"
BLACK = "black"




class Game:
   
    def _init_(self):
        self.playersturn = BLACK
        self.message = "this is where prompts will go"
        self.gameboard = {}
        self.placePieces()
        print("chess program. enter moves in algebraic notation separated by space")
        self.main()

        
    def placePieces(self):

        for i in range(0,5):
            self.gameboard[(i,0)] = Pawn(WHITE,uniDict[WHITE][Pawn],1)
            self.gameboard[(i,4)] = Pawn(BLACK,uniDict[BLACK][Pawn],-1)
            

        
    def main(self):
        
        while True:
            self.printBoard()
            print(self.message)
            self.message = ""
            startpos,endpos = self.parseInput()
            try:
                target = self.gameboard[startpos]
            except:
                self.message = "could not find piece; index probably out of range"
                target = None
                
            if target:
                print("found "+str(target))
                if target.Color != self.playersturn:
                    self.message = "you aren't allowed to move that piece this turn"
                    continue
                if target.isValid(startpos,endpos,target.Color,self.gameboard):
                    self.message = "that is a valid move"
                    self.gameboard[endpos] = self.gameboard[startpos]
                    del self.gameboard[startpos]
                    self.isCheck()
                    if self.playersturn == BLACK:
                        self.playersturn = WHITE
                    else : self.playersturn = BLACK
                else : 
                    self.message = "invalid move" + str(target.availableMoves(startpos[0],startpos[1],self.gameboard))
                    print(target.availableMoves(startpos[0],startpos[1],self.gameboard))
            else : self.message = "there is no piece in that space"
                    
    
        
    def canSeeKing(self,kingpos,piecelist):
       
        for piece,position in piecelist:
            if piece.isValid(position,kingpos,piece.Color,self.gameboard):
                return True
                
    def parseInput(self):
        try:
            a,b = input().split()
            a = ((ord(a[0])-97), int(a[1])-1)
            b = (ord(b[0])-97, int(b[1])-1)
            print(a,b)
            return (a,b)
        except:
            print("error decoding input. please try again")
            return((-1,-1),(-1,-1))
    

        
    def printBoard(self):
        print("  1 | 2 | 3 | 4 | 5 |")
        for i in range(0,5):
            print("-"*23)
            print(chr(i+97),end="|")
            for j in range(0,5):
                item = self.gameboard.get((i,j)," ")
                print(str(item)+' |', end = " ")
            print()
        print("-"*32)
            
           

class Piece:
    
    def _init_(self,color,name):
        self.name = name
        self.position = None
        self.Color = color
    def isValid(self,startpos,endpos,Color,gameboard):
        if endpos in self.availableMoves(startpos[0],startpos[1],gameboard, Color = Color):
            return True
        return False
    def _repr_(self):
        return self.name
    
    def _str_(self):
        return self.name
    
    def availableMoves(self,x,y,gameboard):
        print("ERROR: no movement for base class")
        
    def AdNauseum(self,x,y,gameboard, Color, intervals):
      
        answers = []
        for xint,yint in intervals:
            xtemp,ytemp = x+xint,y+yint
            while self.isInBounds(xtemp,ytemp):
                #print(str((xtemp,ytemp))+"is in bounds")
                
                target = gameboard.get((xtemp,ytemp),None)
                if target is None: answers.append((xtemp,ytemp))
                elif target.Color != Color: 
                    answers.append((xtemp,ytemp))
                    break
                else:
                    break
                
                xtemp,ytemp = xtemp + xint,ytemp + yint
        return answers
                
    def isInBounds(self,x,y):
        
        if x >= 0 and x < 5 and y >= 0 and y < 5:
            return True
        return False
    
    def noConflict(self,gameboard,initialColor,x,y):
        
        if self.isInBounds(x,y) and (((x,y) not in gameboard) or gameboard[(x,y)].Color != initialColor) : return True
        return False
        
        
chessCardinals = [(1,0),(0,1),(-1,0),(0,-1)]
chessDiagonals = [(1,1),(-1,1),(1,-1),(-1,-1)]

def knightList(x,y,int1,int2):
    
    return [(x+int1,y+int2),(x-int1,y+int2),(x+int1,y-int2),(x-int1,y-int2),(x+int2,y+int1),(x-int2,y+int1),(x+int2,y-int1),(x-int2,y-int1)]
def kingList(x,y):
    return [(x+1,y),(x+1,y+1),(x+1,y-1),(x,y+1),(x,y-1),(x-1,y),(x-1,y+1),(x-1,y-1)]

        
class Pawn(Piece):
    def _init_(self,color,name,direction):
        self.name = name
        self.Color = color
       
        self.direction = direction
    def availableMoves(self,x,y,gameboard, Color = None):
        if Color is None : Color = self.Color
        answers = []
        if (x+1,y+self.direction) in gameboard and self.noConflict(gameboard, Color, x+1, y+self.direction) : answers.append((x+1,y+self.direction))
        if (x-1,y+self.direction) in gameboard and self.noConflict(gameboard, Color, x-1, y+self.direction) : answers.append((x-1,y+self.direction))
        if (x,y+self.direction) not in gameboard and Color == self.Color : answers.append((x,y+self.direction))
        return answers

uniDict = {WHITE : {Pawn : "♙"}, BLACK : {Pawn : "♟"}}
        

        


Game()
