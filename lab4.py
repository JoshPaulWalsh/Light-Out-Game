#Joshua Walsh jpw273@nau.edu
#Kile Driscoll kmd594@nau.edu

import random

def main():
    loopUntilWon()

def changeBox(Row_msg,Col_msg,square):
          
    if square[Row_msg][Col_msg]==u"\u25A0":
        square[Row_msg][Col_msg]=u"\u25A1"
  
    elif square[Row_msg][Col_msg]==u"\u25A1":
        square[Row_msg][Col_msg]=u"\u25A0"

#Changes the color of the selected box

def changeCross(Row_msg,Col_msg,square):

    changeBox(Row_msg,Col_msg,square)

    if Row_msg>0 and Row_msg<4:
        changeBox(Row_msg-1,Col_msg,square)
        changeBox(Row_msg+1,Col_msg,square)
    elif Row_msg==0:
        changeBox(Row_msg+1,Col_msg,square)
    elif Row_msg==4:
        changeBox(Row_msg-1,Col_msg,square)
    
    if Col_msg>0 and Col_msg<4:
        changeBox(Row_msg,Col_msg-1,square)
        changeBox(Row_msg,Col_msg+1,square)
    elif Col_msg==0:
        changeBox(Row_msg,Col_msg+1,square)
    elif Col_msg==4:
        changeBox(Row_msg,Col_msg-1,square)

#Analyzes the position of the box and changes the colors of the boxes around it accordingly

def changeSquareGrid(square):
 
    Row_msg= int(input("Please choose a row number (0-4): "))
    Col_msg= int(input("Please choose a column number (0-4): "))

#Asks for input to decide which row and column the selected box is

    changeCross(Row_msg,Col_msg,square)
    
    for i in range(5):
        for r in range(5):
            print(square[i][r],end=" ")
        print("\n")

#Changes the row and column of the box and prints a 5x5 box

def checkForBlackSquares(square):
    for row in range(5):
        for column in range(5):
            if square[row][column]==u"\u25A1":
                return False
    return True

#Checks for whether or not there are black squares in the array

def loopUntilWon():

    square =[
        [u"\u25A0",u"\u25A0",u"\u25A0",u"\u25A0",u"\u25A0"],
        [u"\u25A0",u"\u25A0",u"\u25A0",u"\u25A0",u"\u25A0"],
        [u"\u25A0",u"\u25A0",u"\u25A0",u"\u25A0",u"\u25A0"],
        [u"\u25A0",u"\u25A0",u"\u25A0",u"\u25A0",u"\u25A0"],
        [u"\u25A0",u"\u25A0",u"\u25A0",u"\u25A0",u"\u25A0"],
    ]

    counter=0

    for i in range(1000):
        random_Row=random.randint(0,4)
        random_Col=random.randint(0,4)
        changeCross(random_Row,random_Col,square)

    for i in range(5):
        for r in range(5):
            print(square[i][r], end=" ")
        print("\n")

    while checkForBlackSquares(square)==False:
        counter=counter+1
        changeSquareGrid(square)
    print("You won with "+str(counter)+" moves!")

#Establishes and randomizes the board as well as prints the number of moves it took to solve

main()

#    for i in range(5):
#        for r in range(5):
#            coloredBox=random.choice(['white','black'])
#            if coloredBox=='black':
#                square[i][r]=u"\u25A1"
#            elif coloredBox=='white':
#                square[i][r]=u"\u25A0"
