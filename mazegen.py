import maze

mymaze = maze.Maze(50, 50)

print(f"Width: {mymaze.width}")
print(f"Height: {mymaze.height}")

print(mymaze.cells)

mymaze.draw()
