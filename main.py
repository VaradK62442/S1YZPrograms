import tkinter as tk

from anova import anova
from rvExpectationVariance import rv
from hypothesisTesting import hypothesis_test
from confidenceIntervals import confidence_interval
from tConfidenceIntervals import t_confidence_interval
from tHypothesisTests import t_hypothesis_test


def main():
    root = tk.Tk()
    root.title("Main menu")

    WIDTH = 30
    HEIGHT = 10

    anova_but = tk.Button(root, text="ANOVA", height=HEIGHT, width=WIDTH, command=anova)
    anova_but.grid(row=0, column=0)

    chi_sq_but = tk.Button(root, text="Chi Square", height=HEIGHT, width=WIDTH)
    chi_sq_but.grid(row=0, column=1)

    ci_but = tk.Button(root, text="Confidence Intervals", height=HEIGHT, width=WIDTH, command=confidence_interval)
    ci_but.grid(row=0, column=2)

    hypothesis_but = tk.Button(root, text="Hypothesis Testing", height=HEIGHT, width=WIDTH, command=hypothesis_test)
    hypothesis_but.grid(row=0, column=3)

    lin_reg_but = tk.Button(root, text="Linear Regression", height=HEIGHT, width=WIDTH)
    lin_reg_but.grid(row=1, column=0)

    rv_but = tk.Button(root, text="Random Variables", height=HEIGHT, width=WIDTH, command=rv)
    rv_but.grid(row=1, column=1)

    t_ci_but = tk.Button(root, text="T Confidence Intervals", height=HEIGHT, width=WIDTH, command=t_confidence_interval)
    t_ci_but.grid(row=1, column=2)

    t_hypothesis_but = tk.Button(root, text="T Hypothesis Testing", height=HEIGHT, width=WIDTH, command=t_hypothesis_test)
    t_hypothesis_but.grid(row=1, column=3)

    root.mainloop()


if __name__ == "__main__":
    main()