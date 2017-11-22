import random
import math
import time

#settings
mapX = 64
mapY = 32
timeout = 512 # -1 for infinit

#map generation
gameMap = [[(False) for x in range(mapX)] for y in range(mapY)]
delta = [[(False) for x in range(mapX)] for y in range(mapY)]
for y in range(mapY):
    for x in range(mapX):
        if random.randint(0,7) <= 3:
            gameMap[y][x] = True
            
def printScreen(gameMap):
    temp = ""
    for y in range(mapY):
        for x in range(mapX):
            if gameMap[y][x] == False:
                temp += "0"
            else:
                temp += "1"
        temp += "\n"
    print(temp)

def rules(gameMap):
    t1 = [[(0) for x in range(mapX)] for y in range(mapY)]
    
    for y in range(mapY):
        for x in range(mapX):
            temp = 0
            if gameMap[(y - 1) % mapY][(x - 1) % mapX] == True:
                temp += 1
            if gameMap[(y - 0) % mapY][(x - 1) % mapX] == True:
                temp += 1
            if gameMap[(y + 1) % mapY][(x - 1) % mapX] == True:
                temp += 1
            if gameMap[(y - 1) % mapY][(x - 0) % mapX] == True:
                temp += 1
            if gameMap[(y + 1) % mapY][(x - 0) % mapX] == True:
                temp += 1
            if gameMap[(y - 1) % mapY][(x + 1) % mapX] == True:
                temp += 1
            if gameMap[(y - 0) % mapY][(x + 1) % mapX] == True:
                temp += 1
            if gameMap[(y + 1) % mapY][(x + 1) % mapX] == True:
                temp += 1
                
            t1[y][x] = temp
    
    for y in range(mapY):
        for x in range(mapX):
            if gameMap[y][x] == False:
                if t1[y][x] == 3:
                    delta[y][x] = True
                else:
                    delta[y][x] = False
            if gameMap[y][x] == True:
                if t1[y][x] < 2 or t1[y][x] > 3:
                    delta[y][x] = False
                else:
                    delta[y][x] = True
    
    return delta
                
def toLife(gameMap):
    for y in range(mapY):
        for x in range(mapX):
            if gameMap[y][x] == False and random.randint(0,63) <= 0:
                gameMap[y][x] = True
    return gameMap

t = 0
while(t == timeout):
    printScreen(gameMap)
    gameMap = rules(gameMap)
    #gameMap = toLife(gameMap)
    time.sleep(0.1)
    t += 1
    