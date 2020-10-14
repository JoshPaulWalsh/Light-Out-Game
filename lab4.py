import random

def changeBox(Row_msg,Col_msg,square):
          
    if square[Row_msg][Col_msg]==u"\u25A0":
        square[Row_msg][Col_msg]=u"\u25A1"
  
    elif square[Row_msg][Col_msg]==u"\u25A1":
        square[Row_msg][Col_msg]=u"\u25A0"

def changeSquareGrid(square):
 
    Row_msg= int(input("Please choose a row number (0-4): "))
    Col_msg= int(input("Please choose a column number (0-4): "))

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
        
    for i in range(5):
        for r in range(5):
            print(square[i][r],end=" ")
        print("\n")

def checkForBlackSquares(square):
    for row in range(5):
        for column in range(5):
            if square[row][column]==u"\u25A1":
                return False
    return True

def loopUntilWon():

    square =[
        ["x","x","x","x","x"],
        ["x","x","x","x","x"],
        ["x","x","x","x","x"],
        ["x","x","x","x","x"],
        ["x","x","x","x","x"],
    ]

    for i in range(5):
        for r in range(5):
            coloredBox=random.choice(['white','black'])
            if coloredBox=='black':
                square[i][r]=u"\u25A1"
            elif coloredBox=='white':
                square[i][r]=u"\u25A0"

    for i in range(5):
        for r in range(5):
            print(square[i][r], end=" ")
        print("\n")

    while checkForBlackSquares(square)==False:
        changeSquareGrid(square)

def main():
    loopUntilWon()

main()
