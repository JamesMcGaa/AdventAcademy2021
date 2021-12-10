import os 
f = open("input9.txt", "r")
grid = [[int(digit) for digit in line.strip()] for line in  f.readlines()]


def is_low(x, y, grid):
    val = grid[x][y]

    for x_offset in [-1, 1]:
        if 0 <= x + x_offset and x + x_offset < len(grid) and grid[x + x_offset][y] <= val:
            return False

    for y_offset in [-1, 1]:
        if 0 <= y + y_offset and y + y_offset < len(grid[x]) and grid[x][y + y_offset] <= val:
            return False
    
    return True

counter = 0 
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if is_low(x, y, grid):
            counter += grid[x][y] + 1

print(counter)

