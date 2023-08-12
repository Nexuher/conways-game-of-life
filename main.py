import game_of_life_grid
import template_patterns

def cool_setup_one(grid):
    grid.add_pattern(template_patterns.GliderPattern, 2, 8)
    grid.add_pattern(template_patterns.ToadPattern, 2, 2)
    grid.add_pattern(template_patterns.ToadPattern, 7, 9)
    grid.add_pattern(template_patterns.ToadPattern, 15, 15)

if __name__ == "__main__":
    grid = game_of_life_grid.GameOfLifeGrid(size=20)

    grid.add_pattern(template_patterns.PulsarPattern, 2, 2)
    #cool_setup_one(grid)

    grid.run_simulation()

