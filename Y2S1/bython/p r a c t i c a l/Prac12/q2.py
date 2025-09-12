import tkinter as tk
from tkinter import messagebox
import math

class CylinderCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Cylinder Calculator Demo")

        self.label_radius = tk.Label(master, text="Radius:")
        self.label_radius.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_radius = tk.Entry(master)
        self.entry_radius.grid(row=0, column=1, padx=5, pady=5)
        self.entry_radius.focus_set() 

        self.label_height = tk.Label(master, text="Height:")
        self.label_height.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.entry_height = tk.Entry(master)
        self.entry_height.grid(row=0, column=3, padx=5, pady=5)

        self.label_area = tk.Label(master, text="Area:")
        self.label_area.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_area = tk.Entry(master, state="disabled")
        self.entry_area.grid(row=1, column=1, padx=5, pady=5)

        self.label_volume = tk.Label(master, text="Volume:")
        self.label_volume.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.entry_volume = tk.Entry(master, state="disabled")
        self.entry_volume.grid(row=1, column=3, padx=5, pady=5)

        self.calculate_button = tk.Button(master, text="Calculate!", command=self.calculate_cylinder_properties)
        self.calculate_button.grid(row=2, column=0, columnspan=4, pady=10)

    def calculate_cylinder_properties(self):
        try:
            radius = float(self.entry_radius.get())
            height = float(self.entry_height.get())

            if radius < 0 or height < 0:
                messagebox.showerror("Input Error", "Radius and Height cannot be negative.")
                return

            area = 2 * math.pi * radius * height + 2 * math.pi * (radius ** 2)

            volume = math.pi * (radius ** 2) * height

            self.entry_area.config(state="normal")
            self.entry_area.delete(0, tk.END)
            self.entry_area.insert(0, f"{area:.2f}")
            self.entry_area.config(state="disabled")

            self.entry_volume.config(state="normal")
            self.entry_volume.delete(0, tk.END)
            self.entry_volume.insert(0, f"{volume:.2f}")
            self.entry_volume.config(state="disabled")

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numeric values for Radius and Height.")
        except Exception as e:
            messagebox.showerror("An Error Occurred", str(e))

root = tk.Tk()
my_gui = CylinderCalculator(root)
root.mainloop()