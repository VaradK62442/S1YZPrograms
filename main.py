import tkinter as tk

from anova import anova

root = tk.Tk()
root.title("Main menu")

WIDTH = 30
HEIGHT = 10

anova_but = tk.Button(root, text="ANOVA", height=HEIGHT, width=WIDTH, command=anova)
anova_but.grid(row=0, column=0)

chi_sq_but = tk.Button(root, text="Chi Square", height=HEIGHT, width=WIDTH)
chi_sq_but.grid(row=0, column=1)

chi_sq_but = tk.Button(root, text="Confidence Intervals", height=HEIGHT, width=WIDTH)
chi_sq_but.grid(row=0, column=2)

chi_sq_but = tk.Button(root, text="Hypothesis Testing", height=HEIGHT, width=WIDTH)
chi_sq_but.grid(row=0, column=3)

chi_sq_but = tk.Button(root, text="Linear Regression", height=HEIGHT, width=WIDTH)
chi_sq_but.grid(row=1, column=0)

chi_sq_but = tk.Button(root, text="Random Variables", height=HEIGHT, width=WIDTH)
chi_sq_but.grid(row=1, column=1)

chi_sq_but = tk.Button(root, text="T test Confidence Intervals", height=HEIGHT, width=WIDTH)
chi_sq_but.grid(row=1, column=2)

chi_sq_but = tk.Button(root, text="T test Hypothesis Testing", height=HEIGHT, width=WIDTH)
chi_sq_but.grid(row=1, column=3)

root.mainloop()