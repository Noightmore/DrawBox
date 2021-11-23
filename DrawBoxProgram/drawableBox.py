import random

def drawBox(height,lenght):
    box = ""
    for i in range(0,height):
        if i == 0 or i == height-1:
            box += drawEndLine(lenght)               
        else:
            box += drawLine(height,lenght,i)
        box += '\n'
    return box

def drawEndLine(lenght):
    line = ""
    for i in range(0,lenght):
        if i == 0 or i == lenght-1 :
            line += "."
        else:
            line += "-"
    return line

def drawLine(height,lenght,depth):
    line = ""
    for i in range(0,lenght):
        if i == 0 or i == lenght-1 :
            line += "|"
        else:
            line += filling(depth,height)
    return line

def filling(depth,height):
    randomNum = random.randrange(1,10)
    if depth < height/3:
        return " "
    elif depth < (4*height)/9 and depth > (2*height)/9:       
        if randomNum < 4:
            return "o"
        else:
            return " "
    else:
        if randomNum < 7:
            return "o"
        else:
            return " "