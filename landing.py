import tkinter as tk
from tkinter import simpledialog
import os
import spacetimevisual, graphs
from PIL import Image, ImageTk


def getMass():
    mass1 = simpledialog.askfloat("Parameter Input", "Enter mass for cb1 (solar mass): ", parent=root)
    mass2 = simpledialog.askfloat("Parameter Input", "Enter mass for cb2 (solar mass): ", parent=root)
    return (mass1,mass2)

def getSpin():
    angular_momentum_x1 = simpledialog.askfloat("Parameter Input", "Enter spinZ for cb1:", parent=root)
    angular_momentum_y1 = simpledialog.askfloat("Parameter Input", "Enter spinY  for cb1:", parent=root)
    angular_momentum_x2 = simpledialog.askfloat("Parameter Input", "Enter spinZ for cb2:", parent=root)
    angular_momentum_y2 = simpledialog.askfloat("Parameter Input", "Enter spinY for cb2:", parent=root)
    return ((angular_momentum_x1, angular_momentum_y1), (angular_momentum_x2, angular_momentum_y2))

def getSep():
     sep = float(simpledialog.askfloat("Parameter Input", "Enter the separation between the bodies (au): ", parent=root))
     return sep
    
def run_spacetimevisual():
    masses = getMass()
    spins = getSpin()
    sep = getSep()
    # positions = getPos()

    spacetimevisual.run_simulation(masses, spins, sep)


def run_graphs():
    masses = getMass()
    spins = getSpin()
    # positions = getPos()
    
    graphs.run_simulation(masses, spins)
    

root = tk.Tk()
root.geometry("1920x1080")
root.title("Choose script and enter parameters")

image = Image.open("cover.png")
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.image = photo  # Keep a reference to avoid garbage collection
label.pack()
# btns
btn_spacetime = tk.Button(root, text="Spacetime contour of bodies", command=run_spacetimevisual)
btn_spacetime.pack(pady=10)

btn_graphs = tk.Button(root, text="Waveform and spectogram of grav. waves (h+/hc polarization)", command=run_graphs)
btn_graphs.pack(pady=10)

# gui loop
root.mainloop()
