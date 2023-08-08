import random
import time


grid_size = 7
generation_number = 1


def create_grid():
    universe = [[0] * grid_size for _ in range(grid_size)]

    # Testing setups of pixels below

    #grid_set_one_U(universe)
    #grid_set_two_X(universe)
    #grid_set_three_star(universe)
    final_grid_test(universe)

    for row in range(grid_size): # Iterate through index of row and column below
        for column in range(grid_size):
            #To get more pixels in universe, simply lower the second number in randint
            # Randomise do we put live pixel in there
            """
                1 represents live pixel / on
                0 represents void / off
            """

            #chance = random.randint(0,1) 
            

            #if chance == 1:
                #universe[row][column] = 1

            print(universe[row][column], end=" ")
        print("")
    
    return universe


def print_grid(grid):
    for row in range(grid_size): # Iterate through index of row and column below
        for column in range(grid_size):
            print(grid[row][column], end=" ")
        print("")


def pixel_survivability(grid):
    global generation_number

    generation_number += 1

    new_grid = [[0] * grid_size for _ in range(grid_size)]

    for row in range(grid_size): # Iterate through index of row and column below
        for column in range(grid_size):
            single_pixel = grid[row][column] # Define single pixel that its neighbours will be checked

            neighbours = count_neighbours(grid, row, column)
            
            # Below is a list of neighbours of every pixel in a row
            # if single_pixel == 1:
            #     print(f"Row: {row} & Column: {column}\nNeighbours: {neighbours}\n")
           
            single_pixel = get_next_pixel_state(neighbours, single_pixel)

            new_grid[row][column] = single_pixel 

    print(f"\n<------ {generation_number} Generation ------>")
    print_grid(new_grid)

    return new_grid 


def count_neighbours(universe, row, column):
    amount_of_neighbours = 0
    pixel_number = universe[row][column]

    # Top Left
    if(row - 1 >= 0 and column - 1 >= 0):
        pixel_number = universe[row - 1][column - 1]  

        if(pixel_number == 1): 
            amount_of_neighbours += 1

    # Top Middle
    if(row - 1 >= 0):
        pixel_number = universe[row - 1][column]  

        if(pixel_number == 1): 
            amount_of_neighbours += 1
    
    # Top Right
    if(row - 1 >= 0 and column + 1 < grid_size):
        pixel_number = universe[row - 1][column + 1]  
        
        if(pixel_number == 1): 
            amount_of_neighbours += 1        

    # Left
    if(column - 1 >= 0):
        pixel_number = universe[row][column -1]

        if(pixel_number == 1): #4
            amount_of_neighbours += 1
    
    # Right
    if(column + 1 < grid_size):
        pixel_number = universe[row][column + 1]   

        if(pixel_number == 1): 
            amount_of_neighbours += 1

    # Bottom Left
    if(row + 1 < grid_size and column - 1 >= 0):
        pixel_number = universe[row + 1][column -1]

        if(pixel_number == 1): 
            amount_of_neighbours += 1

    # Bottom Middle
    if(row + 1 < grid_size):
        pixel_number = universe[row + 1][column]

        if(pixel_number == 1): 
            amount_of_neighbours += 1

    # Bottom Right
    if(row + 1 < grid_size and column + 1 < grid_size):
        pixel_number = universe[row + 1][column + 1]

        if(pixel_number == 1): 
           amount_of_neighbours += 1            

    return amount_of_neighbours                     


def get_next_pixel_state(neighbour_count, single_pixel):
    if single_pixel == 1 and neighbour_count < 2:
        return 0 #Underpopulation

    if single_pixel == 1 and neighbour_count == 2 or neighbour_count == 3:
        return 1 #Normal

    if single_pixel == 1 and neighbour_count > 3:
        return 0 #Next population

    if single_pixel == 0 and neighbour_count == 3:
        return 1             

    return single_pixel


def grid_set_one_U(grid):
    #Full grid

    global grid_size
    grid_size = 5

    grid[0][0] = 1
    grid[0][1] = 1
    grid[0][2] = 1

    grid[1][0] = 1
    grid[1][1] = 1
    grid[1][2] = 1
    
    grid[2][0] = 1
    grid[2][1] = 1
    grid[2][2] = 1    

    return grid


def grid_set_two_X(grid):
    #Full grid

    global grid_size
    grid_size = 3

    grid[0][0] = 1
    grid[0][2] = 1

    grid[1][1] = 1
    
    grid[2][0] = 1
    grid[2][2] = 1    

    return grid


def grid_set_three_star(grid):
    #Full grid

    global grid_size
    grid_size = 3

    grid[0][1] = 1

    grid[1][0] = 1
    grid[1][2] = 1

    grid[2][1] = 1   

    return grid


def final_grid_test(grid):
    #Full grid

    global grid_size
    grid_size = 5

    grid[0][1] = 1
    grid[1][2] = 1
    grid[2][0] = 1 
    grid[2][1] = 1 
    grid[2][2] = 1 

    return grid


grid = create_grid()

while(True):
    grid = pixel_survivability(grid)
    time.sleep(1.5)