import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.geometry('800x800')
window.title('IA Juego del N en raya')

def CambiarColor(frame):
    frame.configure(bg="red")

def CrearMalla(N):
    for i in range(N):
        window.columnconfigure(i, weight=1, minsize=50)
        window.rowconfigure(i, weight=1, minsize=40)

        for j in range(0,N):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1,
            )
            frame.grid(row=i, column=j, padx=5, pady=5)
            label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
            label.pack(padx=5, pady=5)

            boton = tk.Button(master=frame, text="Boton", command= lambda: CambiarColor(frame))
            boton.pack(padx=5, pady=5)

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

 
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()
            



    def InOrder(self):
        if self.left:
            self.left.InOrder()
        print( self.data),
        if self.right:
            self.right.InOrder()

#imprimir el arbol
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(8)
root.insert(13)
root.insert(15)

root.PrintTree()
CrearMalla(5)
window.mainloop()
