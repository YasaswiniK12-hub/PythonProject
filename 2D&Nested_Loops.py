number_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
# Accessing elements in 2D grid
print(number_grid[2][1])
for i in range(len(number_grid)):
    print(number_grid[i])
    for j in range(len(number_grid[i])):
        print(number_grid[i][j])
# or very simple
for i in number_grid:
    for j in i:
        print(j)