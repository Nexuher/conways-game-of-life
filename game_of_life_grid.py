import time
import gui

class GameOfLifeGrid:

    def __init__(self, size):
        self.grid_size = size
        self.grid = self.create_grid()
        self.generation_number = 1
    

    def print_grid(self):
        for row in range(self.grid_size): # Iterate through index of row and column below
            row_string = ""
            for column in range(self.grid_size):
                to_print  = "- " if self.grid[row][column] == 0 else "# "
                row_string += to_print
            print(row_string)


    def calculate_next_grid_epoch(self):
        self.generation_number += 1

        new_grid = [[0] * self.grid_size for _ in range(self.grid_size)]

        for row in range(self.grid_size):
            for column in range(self.grid_size):
                pixel_state = self.grid[row][column] 

                neighbours = self.count_neighbours(self.grid, row, column)
                pixel_state = GameOfLifeGrid.get_next_pixel_state(neighbours, pixel_state)
                new_grid[row][column] = pixel_state 
                
        # print(f"\n<------ {self.generation_number} Generation ------>")
        # self.print_grid()

        self.grid = new_grid 


    def count_neighbours(self, universe, row, column):
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
        if(row - 1 >= 0 and column + 1 < self.grid_size):
            pixel_number = universe[row - 1][column + 1]  
            
            if(pixel_number == 1): 
                amount_of_neighbours += 1        

        # Left
        if(column - 1 >= 0):
            pixel_number = universe[row][column -1]

            if(pixel_number == 1): #4
                amount_of_neighbours += 1
        
        # Right
        if(column + 1 < self.grid_size):
            pixel_number = universe[row][column + 1]   

            if(pixel_number == 1): 
                amount_of_neighbours += 1

        # Bottom Left
        if(row + 1 < self.grid_size and column - 1 >= 0):
            pixel_number = universe[row + 1][column -1]

            if(pixel_number == 1): 
                amount_of_neighbours += 1

        # Bottom Middle
        if(row + 1 < self.grid_size):
            pixel_number = universe[row + 1][column]

            if(pixel_number == 1): 
                amount_of_neighbours += 1

        # Bottom Right
        if(row + 1 < self.grid_size and column + 1 < self.grid_size):
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


    def create_grid(self):
        new_grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        return new_grid
    

    def run_simulation(self):
        while(True):
            self.calculate_next_grid_epoch()
            time.sleep(0.2)


    def add_pattern(self, template, x, y):
        print(f"Adding {template.__name__} to grid in position {x},{y}")

        if x + template.size_xx >= len(self.grid):
            print("Pattern that you tried to add has gone beyond the bounds of the grid on the X axis.")
            return
        elif y + template.size_yy >= len(self.grid[0]):
            print("Pattern that you tried to add has gone beyond the bounds of the grid on the Y axis.")
            return

        for xx in range(template.size_xx):
            for yy in range(template.size_yy):
                self.grid[x + xx][y + yy] = template.pattern[xx][yy]
    