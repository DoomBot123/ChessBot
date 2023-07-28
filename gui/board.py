#Visual GUI for the chess board
import tkinter as tk
from PIL import Image
def on_square_click(row, col):
    print(f"Clicked on square: {row}, {col}")

root = tk.Tk()
root.title("Chessboard")

square_size = 50
canvas = tk.Canvas(root, width=square_size*8, height=square_size*8)
canvas.pack()
for row in range(8):
    for col in range(8):
        color = "#d6c8c5" if (row + col) % 2 == 0 else "#433431"
        x0, y0 = col * square_size, row * square_size
        x1, y1 = x0 + square_size, y0 + square_size
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        canvas.tag_bind(f"square_{row}_{col}", "<Button-1>", on_square_click)


root.mainloop()