import tkinter as tk

from anova import anova

root = tk.Tk()
root.title("Main menu")
root.geometry("880x50")

WIDTH = 30

anova_but = tk.Button(root, text="ANOVA", width=WIDTH, command=anova)
anova_but.grid(row=0, column=0)

chi_sq_but = tk.Button(root, text="Chi Square", width=WIDTH)
chi_sq_but.grid(row=0, column=1)

chi_sq_but = tk.Button(root, text="Confidence Intervals", width=WIDTH)
chi_sq_but.grid(row=0, column=2)

chi_sq_but = tk.Button(root, text="Hypothesis Testing", width=WIDTH)
chi_sq_but.grid(row=0, column=3)

chi_sq_but = tk.Button(root, text="Linear Regression", width=WIDTH)
chi_sq_but.grid(row=1, column=0)

chi_sq_but = tk.Button(root, text="Random Variables", width=WIDTH)
chi_sq_but.grid(row=1, column=1)

chi_sq_but = tk.Button(root, text="T test Confidence Intervals", width=WIDTH)
chi_sq_but.grid(row=1, column=2)

chi_sq_but = tk.Button(root, text="T test Hypothesis Testing", width=WIDTH)
chi_sq_but.grid(row=1, column=3)

root.mainloop()