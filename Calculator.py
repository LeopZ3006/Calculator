

import tkinter

button_values = [
    ["AC", "+/-", "%", "/"],
    ["7", "8", "9", "X"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", ":)", "="],
]

right_symbols = ["/", "X", "-", "+", "="]
top_symbols = ["AC", "+/-", "%" ]

row_count = len(button_values) 
top_symbols = len(button_values[0])

color_dark_blue = "#EF77B4"
color_yellow = "#E4C023"
color_light_blue = "#8CD2D3"
color_gray = "#9F9E9F"
color_white = "#F9FCFD"

#I am colorblind :3


window = tkinter.Tk()
window.title("Project Calculator")
window.resizable(False, False)
window.mainloop()