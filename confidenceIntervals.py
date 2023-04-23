# single proportion
#     get p hat, n, significance level
#     check success failure condition
#     calculate confidence interval
# two proportions
#     calculate X% confidence interval given
#         p1, p2, n1, n2, p1-hat, p2-hat, significance level

from scipy import stats # to find z_val
from math import sqrt
import tkinter as tk


# def single_proportion():
#     p_hat = float(input("Enter value for p hat: "))
#     n = int(input("Enter value for n: "))
#     sig_level = float(input("Enter value for significance level: "))

#     # check sf condition
#     if p_hat * n > 5 and (1-p_hat) * n > 5:
#         print(f'''Success-failure condition satisfied.''')
#     else:
#         print(f'''Success-failure condition not satisfied.''')

#     z_val = -1 * (stats.norm.ppf(sig_level/2))
#     se = sqrt(p_hat * (1-p_hat) / n)

#     upper_bound = p_hat + z_val * se
#     lower_bound = p_hat - z_val * se

#     print(f'''Confidence interval with 
#     p hat: {p_hat}
#     n: {n}
#     significance level: {round(sig_level, 4)}
#     z value: {round(z_val, 4)}
#     standard error: {round(se, 4)}

#     upper bound: {round(upper_bound, 4)}
#     lower bound: {round(lower_bound, 4)}
#     ''')


# def two_proportion():
#     p1 = float(input("Enter proportion for sample 1: "))
#     n1 = int(input("Enter sample size for sample 1: "))
#     p2 = float(input("Enter proportion for sample 2: "))
#     n2 = int(input("Enter sample size for sample 2: "))
#     sig_level = float(input("Enter significance level: "))

#     # check sf condition
#     sf1 = True if p1*n1 > 5 and (1-p1)*n1 > 5 else False
#     sf2 = True if p2*n2 > 5 and (1-p2)*n2 > 5 else False
#     if sf1 and sf2:
#         print("Success-failure condition satisfied.")
#     else:
#         print("Success-failure condition not satisfied.")

#     z_val = -1 * (stats.norm.ppf(sig_level/2))
#     se = sqrt((p1 * (1-p1) / n1) + (p2 * (1-p2) / n2))
#     diff = p1 - p2

#     upper_bound = diff + z_val * se
#     lower_bound = diff - z_val * se

#     print(f'''Confidence interval with 
#     p1: {p1}
#     n1: {n1}
#     p2: {p2}
#     n2: {n2}
#     significance level: {round(sig_level, 4)}
#     z value: {round(z_val, 4)}
#     standard error: {round(se, 4)}
#     p1 - p2: {round(diff, 4)}

#     upper bound: {round(upper_bound, 4)}
#     lower bound: {round(lower_bound, 4)}
#     ''')


# def margin_of_error():
#     pass


# def main():
#     choice = int(input('''\n[1] Single proportion
#     \n[2] Two proportions
#     \n[3] Margin of error
#     \nChoose type: '''))

#     if choice == 1:
#         single_proportion()
#     elif choice == 2:
#         two_proportion()
#     elif choice == 3:
#         margin_of_error()


def confidence_interval():

    def prop_chosen():
        print("prop chosen called")
        def one_prop():
            print("one prop called")
            def perform_one_prop():
                # clear previous outputs
                for widgets in output_frame.winfo_children():
                    widgets.destroy()

                sig_level = float(sig_level_val.get())
                p_hat = float(p_hat_val.get())
                n = int(n_val.get())

                res = ''

                # check sf condition
                if p_hat * n > 5 and (1-p_hat) * n > 5:
                    res += "Success-failure condition satisfied.\n"
                else:
                    res += "Success-failure condition not satisfied.\n"

                z_val = -1 * (stats.norm.ppf(sig_level / 2))
                se = sqrt(p_hat * (1-p_hat) / n)

                upper_bound = p_hat + z_val * se
                lower_bound = p_hat - z_val * se

                res += f"Confidence interval with\n"
                res += f"p hat: {p_hat}\n"
                res += f"n: {n}\n"
                res += f"Significance level: {round(sig_level, 4)}\n"
                res += f"Z value: {round(z_val, 4)}\n"
                res += f"Standard error: {round(se, 4)}\n"
                res += "\n"
                res += f"Full equation: {p_hat} ± {round(z_val, 4)} * {round(se, 4)}\n"
                res += f"Confidence interval: ({round(lower_bound, 4)}, {round(upper_bound, 4)})"

                conclusion_label = tk.Label(output_frame, text=res)
                conclusion_label.grid(row=6, column=0, columnspan=2)


            # clear previous inputs
            for widgets in input_frame.winfo_children():
                widgets.destroy()

            sig_level_lab = tk.Label(input_frame, text="Significance level")
            sig_level_val = tk.Entry(input_frame, width=30)

            sig_level_lab.grid(row=2, column=0, sticky="e")
            sig_level_val.grid(row=2, column=1)

            p_hat_lab = tk.Label(input_frame, text="Sample proportion")
            p_hat_val = tk.Entry(input_frame, width=30)

            p_hat_lab.grid(row=3, column=0, sticky="e")
            p_hat_val.grid(row=3, column=1)

            n_lab = tk.Label(input_frame, text="Sample size")
            n_val = tk.Entry(input_frame, width=30)

            n_lab.grid(row=4, column=0, sticky="e")
            n_val.grid(row=4, column=1)

            next_but = tk.Button(input_frame, text="Next", width=20, command=perform_one_prop)
            next_but.grid(row=5, column=0, columnspan=2) 

        
        def two_prop():
            print("two prop called")
            def perform_two_prop():
                # clear previous outputs
                for widgets in output_frame.winfo_children():
                    widgets.destroy()

                sig_level = float(sig_level_val.get())
                p1 = float(p1_val.get())
                p2 = float(p2_val.get())
                n1 = int(n1_val.get())
                n2 = int(n2_val.get())

                res = ''

                # check sf condition
                sf1 = True if p1*n1 > 5 and (1-p1)*n1 > 5 else False
                sf2 = True if p2*n2 > 5 and (1-p2)*n2 > 5 else False

                if sf1 and sf2:
                    res += "Success-failure condition satisfied.\n"
                else:
                    res += "Success-failure condition not satisfied.\n"

                z_val = -1 * (stats.norm.ppf(sig_level/2))
                se = sqrt((p1 * (1-p1) / n1) + (p2 * (1-p2) / n2))
                diff = p1 - p2
                
                upper_bound = diff + z_val * se
                lower_bound = diff - z_val * se

                res += f"Confidence interval with\n"
                res += f"p1: {p1}\n"
                res += f"n1: {n1}\n"
                res += f"p2: {p2}\n"
                res += f"n2: {n2}\n"
                res += f"Significance level: {round(sig_level, 4)}\n"
                res += f"Z value: {round(z_val, 4)}\n"
                res += f"Standard error: {round(se, 4)}\n"
                res += f"p1 - p2: {round(diff, 4)}\n"
                res += "\n"
                res += f"Full equation: {round(diff, 4)} ± {round(z_val, 4)} * {round(se, 4)}\n"
                res += f"Confidence interval: ({round(lower_bound, 4)}, {round(upper_bound, 4)})"

                conclusion_label = tk.Label(output_frame, text=res)
                conclusion_label.grid(row=6, column=0, columnspan=2)


            # clear previous inputs
            for widgets in input_frame.winfo_children():
                widgets.destroy()

            sig_level_lab = tk.Label(input_frame, text="Significance level")
            sig_level_val = tk.Entry(input_frame, width=30)

            sig_level_lab.grid(row=2, column=0, sticky="e")
            sig_level_val.grid(row=2, column=1)

            p1_lab = tk.Label(input_frame, text="Sample proportion for sample 1")
            p1_val = tk.Entry(input_frame, width=30)

            p1_lab.grid(row=3, column=0, sticky="e")
            p1_val.grid(row=3, column=1)

            p2_lab = tk.Label(input_frame, text="Sample proportion for sample 2")
            p2_val = tk.Entry(input_frame, width=30)

            p2_lab.grid(row=4, column=0, sticky="e")
            p2_val.grid(row=4, column=1)

            n1_lab = tk.Label(input_frame, text="Sample size for sample 1")
            n1_val = tk.Entry(input_frame, width=30)

            n1_lab.grid(row=5, column=0, sticky="e")
            n1_val.grid(row=5, column=1)

            n2_lab = tk.Label(input_frame, text="Sample size for sample 2")
            n2_val = tk.Entry(input_frame, width=30)

            n2_lab.grid(row=6, column=0, sticky="e")
            n2_val.grid(row=6, column=1)

            next_but = tk.Button(input_frame, text="Next", width=20, command=perform_two_prop)
            next_but.grid(row=7, column=0, columnspan=2)


        sided = prop_val.get()
        print(f"got sided val: {sided}")
        if sided == 1:
            print("sided 1")
            one_prop()
        elif sided == 2:
            print("sided 2")
            two_prop()


    root = tk.Tk()
    root.title("Confidence Intervals")
    root.geometry("400x450")

    type_frame = tk.Frame(root)
    type_frame.pack()

    input_frame = tk.Frame(root)
    input_frame.pack()

    output_frame = tk.Frame(root, relief=tk.GROOVE, borderwidth=3)
    output_frame.pack()

    prop_val = tk.IntVar()
    test_type_lab = tk.Label(type_frame, text="Type of test")
    test_type_lab.grid(row=0, column=0, columnspan=2)

    one_prop = tk.Radiobutton(type_frame, text="One proportion", variable=prop_val, value=1, command=prop_chosen)
    two_prop = tk.Radiobutton(type_frame, text="Two proportion", variable=prop_val, value=2, command=prop_chosen)

    one_prop.grid(row=1, column=0)
    two_prop.grid(row=1, column=1) 

    root.mainloop()


if __name__ == "__main__":
    confidence_interval()