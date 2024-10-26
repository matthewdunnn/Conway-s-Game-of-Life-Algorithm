#Game of Life
from random import randint; import tkinter as tk; import time, os
def clearTerm():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
clearTerm()
original_grid = []
y, x = 0, 0
neighbors = [(-1, -1), (0, 1), (0, 1), (1, 0), (1, 0), (0, -1), (0, -1), (-1, 0)]
alive = bool
while True:
    inpt = input("What size do you want game of life: ")
    try:
        inpt = abs(int(inpt))
    except:
        clearTerm()
        print("Enter a number...\n")
        time.sleep(0.75)
        continue
    if inpt <= 2:
        clearTerm()
        print("Enter a number greater than 2...\n")
        time.sleep(0.75)
        continue
    all_cells = (inpt**2)
    for i in range(inpt):
        original_grid.append([])
    break
for i in range(all_cells):
    rando = randint(0, 1)
    if len(original_grid[y]) == inpt:
        y += 1
    original_grid[y].append(rando)
dimen = 250/len(original_grid)
def create_button():
    button = tk.Button(text="Click Me", command=solve, fg="red")
    button.grid(column=(inpt//2), row =inpt)
def solve():
    new_grid = []
    y, x = 0, 0
    for i in range(len(original_grid)):
        new_grid.append([])
    for i in range(all_cells):
        if len(new_grid[y]) == len(original_grid):
            y += 1
            x = 0
        new_grid[y].append(original_grid[y][x])
        x += 1
    y, x = 0, 0
    for i in range(all_cells):
        total = 0
        if y == len(original_grid):
            y = 0
            x += 1
        if original_grid[y][x] == 1:
            alive = True
            colour = "black"
        else:
            alive = False
            colour = "white"
        canvas = tk.Canvas(root, bg=colour, height=dimen, width=dimen)
        canvas.grid(column=x, row=y)
        for i, j in neighbors:
            y += i
            x += j
            if ((y < 0) or (x < 0)) or (y < 0 and x < 0):
                continue
            if (y == len(original_grid)) or (x == len(original_grid)) or (y == len(original_grid) and x == len(original_grid)):
                continue
            else:
                total += original_grid[y][x]
        x += 1
        if alive == True:
            if total != 2 and total != 3:
                new_grid[y][x] = 0
        if alive == False:
            if total == 3:
                new_grid[y][x] = 1
        y += 1
    y, x = 0, 0
    for i in range(all_cells):
        if y == len(original_grid):
            y = 0
            x += 1
        original_grid[y][x] = new_grid[y][x]
        y += 1
    create_button()
root = tk.Tk()
root.title("Game of Life")
solve()
root.mainloop()