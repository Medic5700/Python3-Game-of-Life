import random
import math
import time

#settings
mapX = 64
mapY = 32
timeout = 512 # -1 for infinit

def generateMap():
    """Generates the map, returns a two dimensional array of True or False"""
    gameMap = [[(False) for x in range(mapX)] for y in range(mapY)]
    for y in range(mapY):
        for x in range(mapX):
            if random.randint(0,7) <= 3:
                gameMap[y][x] = True
    return gameMap
            
def strScreen(gameMap):
    """Takes the gameMap, returns string representing gameMap"""
    temp = ""
    for y in range(mapY):
        for x in range(mapX):
            if gameMap[y][x] == False:
                temp += "0"
            else:
                temp += "1"
        temp += "\n"
    return temp

def rules(gameMap):
    """Takes the gameMap, returns gameMap iterated one step"""
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
                    gameMap[y][x] = True
                else:
                    gameMap[y][x] = False
            if gameMap[y][x] == True:
                if t1[y][x] < 2 or t1[y][x] > 3:
                    gameMap[y][x] = False
                else:
                    gameMap[y][x] = True
    return gameMap

if __name__ == "__main__":
    gameMap = generateMap()
    step = 0
    while(step != timeout):
        print(strScreen(gameMap))
        gameMap = rules(gameMap)
        time.sleep(0.1)
        step += 1
