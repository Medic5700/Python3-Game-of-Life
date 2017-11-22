import random
import time

#settings
mapX = 80
mapY = 20
timeout = 512 # max run time in steps, -1 for infinite runtime

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
        temp += "\n"
        for x in range(mapX):
            temp += ('-' if (gameMap[y][x] == False) else '8')
    return temp

def iterate(gameMap):
    """Takes the gameMap, returns gameMap iterated one step"""
    neighbors = [[(0) for x in range(mapX)] for y in range(mapY)]
    
    for y in range(mapY):
        for x in range(mapX):
            t = [0, 1, 1, 1, 0, -1, -1, -1] #checks 8 adjacent cells
            for i in range(8):
                if gameMap[(t[(i+2)%8]+y) % mapY][(t[(i+0)%8]+x) % mapX] == True:
                    neighbors[y][x] += 1
    
    for y in range(mapY):
        for x in range(mapX):
            if (gameMap[y][x] == False) and (neighbors[y][x] == 3):
                gameMap[y][x] = True
            elif (gameMap[y][x] == True) and (neighbors[y][x] < 2 or neighbors[y][x] > 3):
                gameMap[y][x] = False
    
    return gameMap

if __name__ == "__main__":
    gameMap = generateMap()
    while(timeout != 0):
        print(strScreen(gameMap))
        gameMap = iterate(gameMap)
        time.sleep(0.1)
        timeout += -1
