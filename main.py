import numpy as np
import random

# steps:
# - calculate positions for the ships (random for start)
# - Create grid, print it
# - check for win
# - ask user for input
# - for every input, check and update grid
# - print updated grid

def create_cordinates(x, y, dir, size):
    cordinates = []
    if (dir == 0):
        for s in range(size):
            cordinates.append([x + s*1, y])
    elif (dir==1):
        for s in range(size):
            cordinates.append([x - s*1, y])
    elif (dir==2):
        for s in range(size):
            cordinates.append([x, y + s*1])
    else:
        for s in range(size):
            cordinates.append([x, y - s*1])

    return cordinates

def check_inbounds(cordinates, cordinate_map):
    # check for in bounds
    for cor in cordinates:
        if cor[0] > 9 or cor[0] < 0 or cor[1] > 9 or cor[1] < 0:
            return False
        
    # check for repetetion
    for cor in cordinates:
        # print(cor, cordinate_map.values())
        for c in cordinate_map.values():
            if cor in c:
                return False
    return True

def get_ship_cordinates(ships):
    # out of 10X10 grids 
    # give cordinates for each ship

    # get random x and random y
    # get random direction
    # use ship length
    # generate cordinates
    # check for overlap
    cordinate_map = {}
    for ship, size in ships.items():
        cordinates = []
        # get random cordiante (x, y)
        ran_x = random.randint(0, 9)
        ran_y = random.randint(0, 9)
        ran_dir = random.choice([0, 1, 2, 3])
        
        # call the create cordinates function
        cordinates = create_cordinates(ran_x, ran_y, ran_dir, size)
        # print(cordinates)

        # while cordinates not in bounds and repeted
        #   call function again
        while check_inbounds(cordinates, cordinate_map) == False:
            # get random cordiante (x, y)
            ran_x = random.randint(0, 9)
            ran_y = random.randint(0, 9)
            ran_dir = random.choice([0, 1, 2, 3])
            cordinates = create_cordinates(ran_x, ran_y, ran_dir, size)
            # print(cordinates)

        cordinate_map[ship] = cordinates

    return cordinate_map

# Creating the play grid
def create_grid(cordinate_map):
    play_grid = np.zeros((10, 10), dtype = int)
    # play_grid[:] = " "
    for ship, cordinate in cordinate_map.items():
        for x, y in cordinate:
            play_grid[x][y] = 1 #ship[0]
    return play_grid

def game_won(play_grid):
    # check if all the values are zero
    if play_grid.any() == 1:
        return False
    return True

# TODO: Inderdeep 5/05/2024
# Function that takes in np.zeros grid and prints it for the user as a viewable thing on the terminal.
def print_grid_for_player(play_grid):
    user_grid = np.zeros((10, 10), dtype = "U1")

    for x in range(10):
        for y in range(10):

            # used to print x for hit target, - for unknown, and * for miss
            if play_grid[x][y] == 2:
                user_grid[x][y] = 'x'
            elif play_grid[x][y] == 3:
                user_grid[x][y] = '*'
            else:
                user_grid[x][y] = '-'

            # used to print grid with ship visible
            # if play_grid[x][y] == 0:
            #     user_grid[x][y] = '-'
            # else:
            #     user_grid[x][y] = 'S'

    print(user_grid)


def get_user_input():
    while True:
        try:
            x = int(input('X: '))
            y = int(input('Y: '))
            if x < 0 or x > 9: raise ValueError
            return int(x), int(y)
        except ValueError:
            print("Invalid Index.The index of target can be in range 0-9.")
    
def user_hit_ship(x, y, play_grid):
    if play_grid[x][y] == 1:
        return True
    else:
        play_grid[x][y] = 3
        return False

def update_play_grid(x, y, play_grid):
    play_grid[x][y] = 2
    return play_grid


if __name__ == "__main__":
    # print(play_grid)

    ships = {
            "carrier" : 5,
            "battleship" : 4,
            "destroyer" : 3,
            "submarine" : 3,
            "patrol_boat" : 2
            }
    
    ship_cordinates = get_ship_cordinates(ships)
    play_grid = create_grid(ship_cordinates)

    while not game_won(play_grid):
        print_grid_for_player(play_grid)
        x, y = get_user_input()
        if (user_hit_ship(x, y, play_grid)):
            print("HIT!")
            play_grid = update_play_grid(x, y, play_grid)
        else:
            print("MISS!")
        
