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

def iterate(gameMap):
    """Takes the gameMap, returns gameMap iterated one step"""
    neighbors = [[(0) for x in range(mapX)] for y in range(mapY)]
    
    for y in range(mapY):
        for x in range(mapX):
            temp = 0
            t = [0, 1, 1, 1, 0, -1, -1, -1]
            for i in range(8):
                if gameMap[(t[(i+2)%8]+y) % mapY][(t[(i+0)%8]+x) % mapX] == True:
                    temp += 1
            neighbors[y][x] = temp
    
    for y in range(mapY):
        for x in range(mapX):
            if (gameMap[y][x] == False) and (neighbors[y][x] == 3):
                gameMap[y][x] = True
            if (gameMap[y][x] == True) and (neighbors[y][x] < 2 or neighbors[y][x] > 3):
                gameMap[y][x] = False
    return gameMap

if __name__ == "__main__":
    gameMap = generateMap()
    step = 0
    while(step != timeout):
        print(strScreen(gameMap))
        gameMap = iterate(gameMap)
        time.sleep(0.1)
        step += 1
