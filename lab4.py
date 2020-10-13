import random

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

#for i in range(5):
#    print(u"\u25A1", end=" ")
#for i in square:
#    Square = [[print(u"\u25A1")]*5 for i in range(5)]
#25A0 is white square

#for i in square:
#    for r in i:
#        print(r, end=" ")
#    print("\n")
