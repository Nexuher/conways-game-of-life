import game_of_life_grid
import template_patterns
import gui

def cool_setup_one(grid):
    # grid.add_pattern(template_patterns.GliderPattern, 2, 8)
    grid.add_pattern(template_patterns.GliderGunPattern, 20, 20)
    # grid.add_pattern(template_patterns.GliderPattern, 20, 8)
    # grid.add_pattern(template_patterns.GliderPattern, 30, 8)
    # grid.add_pattern(template_patterns.ToadPattern, 2, 2)
    # grid.add_pattern(template_patterns.ToadPattern, 7, 9)
    grid.add_pattern(template_patterns.PulsarPattern, 60, 15)

if __name__ == "__main__":
    grid_size = 150
    grid = game_of_life_grid.GameOfLifeGrid(size=grid_size)
    cool_setup_one(grid)
    
    gui.CreateNewGui(grid_size, grid_size, 6, grid)

    #grid.add_pattern(template_patterns.GliderGunPattern, 3, 8)
    # cool_setup_one(grid)

    # grid.run_simulation()

