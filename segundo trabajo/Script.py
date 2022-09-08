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

CrearMalla(5)
window.mainloop()
