import sys
import time
import random
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui
import game_of_life_grid

class GameOfLifeApp(QWidget):

    def __init__(self, gol_size_x, gol_size_y, zoom, grid_logic_engine, bg_color = 'black', fill_color = 'white'):
        super().__init__()

        # Board settings
        self.gol_size_y = gol_size_y
        self.gol_size_x = gol_size_x
        self.zoom = zoom
        self.bg_color = QColor(bg_color)
        self.fill_color = QColor(fill_color)

        # Game of Life logic
        self.grid_logic_engine = grid_logic_engine

        # FPS calculation
        self.time_calculation_interval = 100
        self.epochs_before_time_calculation = self.time_calculation_interval
        self.previous_time = time.time()

        self.__InitializeGuiSettings()
        self.__InitializeTimer()


    def PaintGolCell(self, x, y):
        painter = QPainter(self.pixmap)
        painter.fillRect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size, self.fill_color)


    def calculate_new_gol_iteration(self):
        self.grid_logic_engine.calculate_next_grid_epoch()

        # Calculate FPS
        if self.epochs_before_time_calculation == 0:
            current_time = time.time()
            print(f"FPS: {self.time_calculation_interval / (current_time - self.previous_time):.2f}. " +
                  f"Avg time per epoch: {(current_time - self.previous_time) / self.time_calculation_interval:.2f}s")
            self.epochs_before_time_calculation = self.time_calculation_interval
            self.previous_time = current_time
        else:
            self.epochs_before_time_calculation -= 1
        

        self.pixmap.fill(self.bg_color)

        for row in range(self.grid_logic_engine.grid_size): # Iterate through index of row and column below
            for column in range(self.grid_logic_engine.grid_size):
                if self.grid_logic_engine.grid[row][column] == 1:
                    self.PaintGolCell(row, column)

        self.label.setPixmap(self.pixmap)    


    def __InitializeGuiSettings(self):
        #self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setWindowTitle("Nexuher's Conway's Game Of Life Adaptation")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel()
        layout.addWidget(self.label)

        self.pixmap = QPixmap(self.gol_size_x * self.zoom, self.gol_size_y * self.zoom)
        self.cell_size = self.zoom

        self.pixmap.fill(self.bg_color)
        self.label.setPixmap(self.pixmap)


    def __InitializeTimer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.calculate_new_gol_iteration)
        self.timer.start(0)


def CreateNewGui(size_x, size_y, zoom, grid_logic_engine, bg_color = 'black', fill_color = 'yellow'):
    app = QApplication(sys.argv)
    pixel_painter_app = GameOfLifeApp(size_x, size_y, zoom, grid_logic_engine, bg_color, fill_color)
    pixel_painter_app.show()

    sys.exit(app.exec_())
