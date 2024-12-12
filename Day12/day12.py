data_path = './day12_data_test.txt'

with open(data_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

grid = file_content.split()

print(grid)

# Plan
# Write a function that finds the total area for a square
# It will recursively search for all conjoined squares and record their position
# I think we use DFS again because it is best at finding all possible paths
# We need to record all the squares that have already been assigned to a group so that we don't 
# calculate it's group again
# Once we have all the group coordinates we can work out their area and perimeter

rows, cols = len(grid), len(grid[0])

# def find_group(x, y):
#     # implement DFS
# copy day 10 