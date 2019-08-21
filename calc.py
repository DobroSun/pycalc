#!/usr/bin/env python3

from tkinter import *
from functools import partial



class Main():
    def __init__(self, root):
        self.WIDTH = self.HEIGHT = 125
        self.stack = ""
        self.var = StringVar()

        root.title("Calculator")
        root.geometry("500x600")
        root.resizable(False, False)
        label = Label(root, textvariable=self.var, bg='white', height=6, font = "Verdana 10 bold")
        label.pack(fill=BOTH)
        self.make_buttons()        


    def make_buttons(self):
        arr = []

        # numeric buttons
        for i in range(3):
            for j in range(1, 4):
                text = i*3 + j
                btn = Button(root, command=partial(self.clicked, arr, i, j), text=str(text))
                btn.i, btn.j = i, j
                arr.append(btn)
                self.button_place(btn, i, j)
        
        i += 1
        # -, +, *, // buttons
        for ind, sym in enumerate(['-', '+', '*', '//']):
            j = ind + 1 
            
            btn = Button(root, command=partial(self.clicked, arr, i, j), text=sym)
            btn.i, btn.j = i, ind + 1

            arr.append(btn)
            self.button_place(btn, i, j)
            
        # submit button
        btn = Button(root, command=self.calculate, text="OK")
        btn.i, btn.j = 0, j
        i = 0
        arr.append(btn)
        self.button_place(btn, i, j)

        # delete button
        btn = Button(root, command=self.delete, text="Del")
        btn.i, btn.j = i + 1, j
        i += 1
        arr.append(btn)
        self.button_place(btn, i, j)
        
        
        # exit button
        btn = Button(root, command=self.exit, text="Exit")
        btn.i, btn.j = i + 1, j
        i += 1
        arr.append(btn)
        self.button_place(btn, i, j)
        
    def button_place(self, btn, i, j):
        btn.place(x=self.WIDTH * (j - 1), y=600 - self.HEIGHT*(i + 1), width=self.WIDTH, height=self.HEIGHT)
        

    def clicked(self, arr, i, j):
        for item in arr:
            if item.i == i and item.j == j:
                self.stack += item["text"]
                self.label_update()


    def calculate(self):
        self.stack = "b=" + self.stack
        try:
            loc = {'stack': self.stack}
            glb = {}
            exec(self.stack, glb, loc)
            b = loc['b']
            self.label_update(b)
            self.stack = f"{b}"
        except:
            error = "Uncorrect input"
            self.label_update(error)
            self.stack = ""

    
    def delete(self):
        self.stack = ""
        self.label_update()


    def exit(self):
        exit(0)


    def label_update(self, b=None):
        if b is not None:
            self.var.set(b)
        else:
            self.var.set(self.stack)


if __name__ == "__main__":
    root = Tk()
    main = Main(root)
    root.mainloop()
