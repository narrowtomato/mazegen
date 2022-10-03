import random
from turtle import Turtle,Screen
import pygame

# Define colors for drawing
WHITE = (255,255,255)
class Maze:
    def __init__(self, width, height):
        # Width and Height of maze
        self.width = width
        self.height = height

        # Collection of cells (2-dimensional list)
        # Each is represented by a binary value of initially decimal 15 (1111) for 4 walls
        self.cells = [[15 for i in range(height)] for j in range(width)]
        
        # Robot that will carve out the maze
        # Coordinates of the robot's current position, initially set to a random y and x value
        robot_y = random.randint(0, self.height - 1)
        robot_x = random.randint(0, self.width - 1)
        # List of tuples representing visited cells (to append to and verify when maze is complete)
        robot_visited = [(robot_x, robot_y)]
        # List of tuples representing visited cells that are forkable (to append and pop from to go back when the robot cannot find an unvisited cell)
        robot_visited_forkable = []

        # Loop to carve out the maze
        while len(robot_visited) < self.width * self.height:

            # List of possible directions the robot can move
            available_directions = []

            # Add possible directions based on conditions
            if (robot_x > 0) and ((robot_x - 1, robot_y) not in robot_visited):
                available_directions.append("left")
            if (robot_x < self.width - 1) and ((robot_x + 1, robot_y) not in robot_visited):
                available_directions.append("right")
            if (robot_y > 0) and ((robot_x, robot_y - 1) not in robot_visited):
                available_directions.append("up")
            if (robot_y < self.height - 1) and ((robot_x, robot_y + 1) not in robot_visited):
                available_directions.append("down")

            # If no directions were possible, revert to the previous value in robot_visited_forkable
            #   and restart the loop
            if len(available_directions) == 0:
                robot_visited_forkable.pop()
                robot_x = robot_visited_forkable[-1][0]
                robot_y = robot_visited_forkable[-1][1]
                continue

            # Choose a direction to move
            choice = random.choice(available_directions)

            # Update the walls of the current cell, move the robot, and update the walls of the new cell all based on the direction of movement
            if choice == "left":
                self.cells[robot_x][robot_y] -= 1
                robot_x -=  1
                self.cells[robot_x][robot_y] -= 4
            elif choice == "right":
                self.cells[robot_x][robot_y] -= 4
                robot_x += 1
                self.cells[robot_x][robot_y] -= 1
            elif choice == "up":
                self.cells[robot_x][robot_y] -= 8
                robot_y -= 1
                self.cells[robot_x][robot_y] -= 2
            elif choice == "down":
                self.cells[robot_x][robot_y] -= 2
                robot_y += 1
                self.cells[robot_x][robot_y] -= 8

            # Add the new cell to the lists of visited cells
            robot_visited.append((robot_x, robot_y))
            robot_visited_forkable.append((robot_x, robot_y))

    def draw(self):
        # Initialize Pygame
        pygame.init()

        # Define the screen to draw on
        screen = pygame.display.set_mode((self.width * 10 + 20, self.height * 10 + 20))

        # Loop through all cells and draw walls
        for i in range(self.width):
            for j in range(self.height):
                # If there's a top line
                if format(self.cells[i][j], '#06b')[2] == '1':
                    pygame.draw.line(screen, WHITE, (i * 10 + 10, j * 10 + 10), (i * 10 + 20, j * 10 + 10))
                # If there's a right line
                if format(self.cells[i][j], '#06b')[3] == '1':
                    pygame.draw.line(screen, WHITE, (i * 10 + 20, j * 10 + 10), (i * 10 + 20, j * 10 + 20))
                # If there's a bottom line
                if format(self.cells[i][j], '#06b')[4] == '1':
                    pygame.draw.line(screen, WHITE, (i * 10 + 20, j * 10 + 20), (i * 10 + 10, j * 10 + 20))
                # If there's a left line
                if format(self.cells[i][j], '#06b')[5] == '1':
                    pygame.draw.line(screen, WHITE, (i * 10 + 10, j * 10 + 20), (i * 10 + 10, j * 10 + 10))

        # Display, wait 10 seconds, then exit
        pygame.display.flip()
        pygame.time.wait(10000)
        pygame.quit()