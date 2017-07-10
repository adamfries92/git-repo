#!/usr/bin/python3
import os
import sys
import math
import time

def clear_screen():
    os.system('clear')
    return

def print_grid(grid):
    for line in grid:
        disp = ""
        for num in line:
            disp = disp + "{:4} ".format(num)
        print(disp)
    print("")
    return

def create_grid(grid_size = 3):
    # Create square grid, must be odd number
    if grid_size % 2 == 0:
        grid_size = 3
    return [[0 for x in range(grid_size)] for y in range(grid_size)]

def fill_grid(grid = create_grid()):
    direction = 'start'
    grid_size = len(grid)
    ind_x = math.floor(grid_size/2)
    ind_y = math.floor(grid_size/2)

    for val in range(1,grid_size**2 + 1):
        #print("x: {0}, y:{1}, direction: {2}".format(ind_x,ind_y,direction))
        grid[ind_y][ind_x] = val
        if direction == 'start':
            ind_x += 1
            direction = 'right'
        elif direction == 'right':
            if grid[ind_y+1][ind_x] == 0:
                ind_y +=1
                direction = 'down'
            else:
                ind_x +=1
        elif direction == 'down':
            if grid[ind_y][ind_x-1] == 0:
                ind_x -=1
                direction = 'left'
            else:
                ind_y +=1
        elif direction == 'left':
            if grid[ind_y-1][ind_x] == 0:
                ind_y -=1
                direction = 'up'
            else:
                ind_x -=1
        elif direction == 'up':
            if grid[ind_y][ind_x+1] == 0:
                ind_x +=1
                direction = 'right'
            else:
                ind_y -=1
        #print_grid(grid)

    return grid

def quick_diag_grid_sum(grid_size):
    if grid_size < 3:
        grid_size = 3

    total = 1
    # Only want odd numbers, up to grid_size (have to add +1)
    for x in range(3,grid_size+1,2):
        total += 4*x**2 - 6*x + 6

    return total

def diag_grid_sum(grid):
    total = 0
    grid_mid = math.floor(len(grid)/2)
    l_ind = 0
    r_ind = -1
    for x in range(0,len(grid)):
        if x < grid_mid:
            total += grid[x][l_ind] + grid[x][r_ind]
            l_ind += 1
            r_ind -= 1
        elif x > grid_mid:
            l_ind -= 1
            r_ind += 1
            total += grid[x][l_ind] + grid[x][r_ind]
        else:
            total += 1

    return total

def grid_result(grid_size = 3):
    start = time.time()
    total_grid = diag_grid_sum(fill_grid(create_grid(grid_size)))
    end = time.time()
    print("Slow {0}x{0} Diagonal Total: {1}, time: {2}".format(grid_size,total_grid,end-start))
    speed_up = end-start

    start = time.time()
    total_grid = quick_diag_grid_sum(grid_size)
    end = time.time()
    print("Fast {0}x{0} Diagonal Total: {1}, time: {2}".format(grid_size,total_grid,end-start))
    speed_up /= (end-start)
    print("Speed Up: {0}".format(speed_up))
    print("")
    return

########
# MAIN #
########

clear_screen()

grid_result(3)
grid_result(5)
grid_result(7)
grid_result(9)
grid_result(7001)
