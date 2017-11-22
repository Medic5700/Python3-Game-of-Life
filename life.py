import random
import math
import time
gameMap = [[(False) for i in range(32)] for i in range(32)]
delta = [[(False) for i in range(32)] for i in range(32)]


for i in range(32):
    for j in range(32):
        if random.randint(0,7) <= 3:
            gameMap[i][j] = True
            
def printScreen(gameMap):
    temp = ""
    for i in range(32):
        for j in range(32):
            if gameMap[i][j] == False:
                temp += "0"
            else:
                temp += "1"
        temp += "\n"
    print(temp)

def rules(gameMap):
    t1 = [[(0) for i in range(32)] for i in range(32)]
    
    for i in range(32):
        for j in range(32):
            temp = 0
            if gameMap[(i - 1) % 32][(j - 1) % 32] == True:
                temp += 1
            if gameMap[(i - 0) % 32][(j - 1) % 32] == True:
                temp += 1
            if gameMap[(i + 1) % 32][(j - 1) % 32] == True:
                temp += 1
            if gameMap[(i - 1) % 32][(j - 0) % 32] == True:
                temp += 1
            if gameMap[(i + 1) % 32][(j - 0) % 32] == True:
                temp += 1
            if gameMap[(i - 1) % 32][(j + 1) % 32] == True:
                temp += 1
            if gameMap[(i - 0) % 32][(j + 1) % 32] == True:
                temp += 1
            if gameMap[(i + 1) % 32][(j + 1) % 32] == True:
                temp += 1
                
            t1[i][j] = temp
    
    for i in range(32):
        for j in range(32):
            if gameMap[i][j] == False:
                if t1[i][j] == 3:
                    delta[i][j] = True
                else:
                    delta[i][j] = False
            if gameMap[i][j] == True:
                if t1[i][j] < 2 or t1[i][j] > 3:
                    delta[i][j] = False
                else:
                    delta[i][j] = True
    
    return delta
                
def toLife(gameMap):
    for i in range(32):
        for j in range(32):
            if gameMap[i][j] == False and random.randint(0,63) <= 0:
                gameMap[i][j] = True
    return gameMap

while(True):
    printScreen(gameMap)
    gameMap = rules(gameMap)
    #gameMap = toLife(gameMap)
    time.sleep(0.1)
    