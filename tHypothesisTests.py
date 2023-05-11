from scipy import stats
from math import sqrt
import tkinter as tk


# def single_mean():
#     sig_level = float(input("Enter significance level: "))
#     x_bar = float(input("Enter value for x bar: "))
#     n = int(input("Enter sample size: "))
#     sd = float(input("Enter standard deviation: "))
#     mu = float(input("Enter hypothesis mean: "))
#     tailed = int(input("Enter if the test is [1] tailed or [2] tailed: "))

#     df = n - 1
#     se = sd / (sqrt(n))
#     t_score = (x_bar - mu)/se

#     rejection_region = stats.t.ppf(sig_level/tailed, df) # n tailed in tables
#     p_val = stats.t.cdf(-1 * t_score if t_score > 0 else t_score, df) * tailed

#     print(f'''{tailed}-tail hypothesis test with:
#     Degrees of Freedom: {df}
#     Significance level: {sig_level/tailed}
#     Standard error: {round(se, 4)}
#     T score: {round(t_score, 4)}
#     Rejection region: {-1 * round(rejection_region, 4)}
#     p value: {round(p_val, 4)}''')

#     # decision
#     if sig_level > p_val or sig_level < -1 * p_val:
#         print(f"Reject null hypothesis.")
#         print(f"T score is inside the rejection region.")
#         print(f"p value is less than significance level.")
#     else:
#         print(f"Fail to reject null hypothesis.")
#         print(f"T score is not inside the rejection region.")
#         print(f"p value is more than significance level.")


# def two_means():
#     x_bar1 = float(input("Enter value for x bar 1: "))
#     n1 = int(input("Enter value for n 1: "))
#     sd1 = float(input("Enter value for standard deviation 1: "))

#     x_bar2 = float(input("Enter value for x bar 2: "))
#     n2 = int(input("Enter value for n 2: "))
#     sd2 = float(input("Enter value for standard deviation 2: "))

#     sig_level = float(input("Enter significance level: "))
#     mu = float(input("Enter hypothesis mean difference: "))
#     tailed = int(input("Enter if the test is [1] tailed or [2] tailed: "))

#     x_bar = x_bar1 - x_bar2
#     df = min(n1-1, n2-1)
#     se = sqrt((sd1**2 / n1) + (sd2**2 / n2))
#     t_score = (x_bar - mu)/se

#     rejection_region = stats.t.ppf(sig_level/tailed, df) # n tailed in tables
#     p_val = stats.t.cdf(-1 * t_score if t_score > 0 else t_score, df) * tailed

#     print(f'''{tailed}-tail hypothesis test with:
#     Difference in means: {x_bar}
#     Degrees of Freedom: {df}
#     Significance level: {sig_level/tailed}
#     Standard error: {round(se, 4)}
#     T score: {round(t_score, 4)}
#     Rejection region: {-1 * round(rejection_region, 4)}
#     p value: {round(p_val, 4)}''')

#     # decision
#     if sig_level > p_val or sig_level < -1 * p_val:
#         print(f"Reject null hypothesis.")
#         print(f"T score is inside the rejection region.")
#         print(f"p value is less than significance level.")
#     else:
#         print(f"Fail to reject null hypothesis.")
#         print(f"T score is not inside the rejection region.")
#         print(f"p value is more than significance level.")


# def two_means_pooled():
#     # do not use unless clearly stated 
#     # use pooled sd only after careful consideration    
#     x_bar1 = float(input("Enter value for x bar 1: "))
#     n1 = int(input("Enter value for n 1: "))
#     sd1 = float(input("Enter value for standard deviation 1: "))
#     IQR1 = float(input("Enter IQR for sample 1: "))

#     x_bar2 = float(input("Enter value for x bar 2: "))
#     n2 = int(input("Enter value for n 2: "))
#     sd2 = float(input("Enter value for standard deviation 2: "))
#     IQR2 = float(input("Enter IQR for sample 2: "))

#     sig_level = float(input("Enter significance level: "))
#     mu = float(input("Enter hypothesis mean difference: "))
#     tailed = int(input("Enter if the test is [1] tailed or [2] tailed: "))

#     # check IQR ratios
#     if max(IQR1, IQR2) / min(IQR1, IQR2) < 2:
#         print("Safe to assume equal variances.")
#         print("Ratio of IQRs is less than 2.")
#         equal_var = True
#     else:
#         print("Not safe to assume equal variances.")
#         print("Ratio of IQRs is not less than 2.")
#         equal_var = False

#     if not equal_var:
#         df = min(n1-1, n2-1)
#         se = sqrt(sd1**2/n1 + sd2**2/n2)
#     else:
#         df = n1 + n2 - 2
#         s_2_pooled = ((n1-1) * sd1**2 + (n2-1) * sd2**2) / (n1 + n2 - 2)
#         se = sqrt(s_2_pooled*(1/n1 + 1/n2))

#     t_score = ((x_bar1 - x_bar2) - mu) / se 

#     rejection_region = stats.t.ppf(sig_level/tailed, df) # n tailed in tables
#     p_val = stats.t.cdf(-1 * t_score if t_score > 0 else t_score, df) * tailed

#     print(f'''{tailed}-tail hypothesis test with:
#     Degrees of Freedom: {df}
#     Significance level: {sig_level/tailed}
#     Standard error pooled: {round(s_2_pooled, 4)}
#     T score: {round(t_score, 4)}
#     Rejection region: {-1 * round(rejection_region, 4)}
#     p value: {round(p_val, 4)}''')

#     # decision
#     if sig_level > p_val or sig_level < -1 * p_val:
#         print(f"Reject null hypothesis.")
#         print(f"T score is inside the rejection region.")
#         print(f"p value is less than significance level.")
#     else:
#         print(f"Fail to reject null hypothesis.")
#         print(f"T score is not inside the rejection region.")
#         print(f"p value is more than significance level.")


# def main():
#     choice = int(input('''\n[1] Single mean
#     \n[2] Difference of two means
#     \n[3] Difference of two means (pooled data)
#     \nChoose type: '''))
    
#     if choice == 1:
#         single_mean()
#     elif choice == 2:
#         two_means()
#     elif choice == 3:
#         two_means_pooled()


def t_hypothesis_test():

    def one_mean():
        
        def perform_one_mean():
            # clear previous outputs
            for widgets in output_frame.winfo_children():
                widgets.destroy()

            sig_level = float(sig_level_val.get())
            x_bar = float(x_bar_val.get())
            n = int(n_val.get())
            
            sd = float(sd_val.get())
            mu = float(mu_val.get())
            tailed = int(tailed_val.get())

            res = ''

            df = n - 1
            se = sd / (sqrt(n))
            t_score = (x_bar - mu)/se

            rejection_region = stats.t.ppf(sig_level / tailed, df) # n tailed in tables
            p_val = stats.t.cdf(-1 * t_score if t_score > 0 else t_score, df) * tailed

            res += f"{tailed}-tailed hypothesis test with \n"
            res += f"Degrees of freedom: {df}\n"
            res += f"Significance level: {sig_level/tailed}\n"
            res += f"Standard error: {round(se, 4)}\n"
            res += f"T score: {round(t_score, 4)}\n"
            res += f"Rejection region: {-1 * round(rejection_region, 4)}\n"
            res += f"p value: {round(p_val, 4)}\n"
            res += "\n"

            # decision
            if sig_level > p_val or sig_level < -1 * p_val:
                res += "Reject null hypothesis.\n"
                res += "T score is inside the rejection region.\n"
                res += "p value is less than significance level."
            else:
                res += "Fail to reject null hypothesis.\n"
                res += "T score is not inside the rejection region.\n"
                res += "p value is more than significance level."

            conclusion_label = tk.Label(output_frame, text=res)
            conclusion_label.grid(row=8, column=0, columnspan=2)


        # clear previous inputs
        for widgets in input_frame.winfo_children():
            widgets.destroy()

        sig_level_lab = tk.Label(input_frame, text="Significance level")
        sig_level_val = tk.Entry(input_frame, width=30)

        sig_level_lab.grid(row=1, column=0, sticky="e")
        sig_level_val.grid(row=1, column=1)

        x_bar_lab = tk.Label(input_frame, text="x bar")
        x_bar_val = tk.Entry(input_frame, width=30)

        x_bar_lab.grid(row=2, column=0, sticky="e")
        x_bar_val.grid(row=2, column=1)

        n_lab = tk.Label(input_frame, text="Sample size")
        n_val = tk.Entry(input_frame, width=30)

        n_lab.grid(row=3, column=0, sticky="e")
        n_val.grid(row=3, column=1)

        sd_lab = tk.Label(input_frame, text="Standard deviation")
        sd_val = tk.Entry(input_frame, width=30)

        sd_lab.grid(row=4, column=0, sticky="e")
        sd_val.grid(row=4, column=1)

        mu_lab = tk.Label(input_frame, text="Hypothesis mean")
        mu_val = tk.Entry(input_frame, width=30)

        mu_lab.grid(row=5, column=0, sticky="e")
        mu_val.grid(row=5, column=1)

        tailed_lab = tk.Label(input_frame, text="[1] or [2] tailed")
        tailed_val = tk.Entry(input_frame, width=30)

        tailed_lab.grid(row=6, column=0, sticky="e")
        tailed_val.grid(row=6, column=1)

        next_but = tk.Button(input_frame, text="Next", width=20, command=perform_one_mean)
        next_but.grid(row=7, column=0, columnspan=2) 

    
    def two_mean():
        
        def perform_two_mean():
            # clear previous outputs
            for widgets in output_frame.winfo_children():
                widgets.destroy()

            sig_level = float(sig_level_val.get())
            
            x_bar1 = float(x1_val.get())
            x_bar2 = float(x2_val.get())
            
            n1 = int(n1_val.get())
            n2 = int(n2_val.get())
            
            sd1 = float(sd1_val.get())
            sd2 = float(sd2_val.get())
            
            mu = float(mu_val.get())
            tailed = int(tailed_val.get())                

            res = ''

            x_bar = x_bar1 - x_bar2
            df = min(n1-1, n2-1)
            se = sqrt((sd1**2 / n1) + (sd2**2 / n2))
            t_score = (x_bar - mu)/se

            rejection_region = stats.t.ppf(sig_level / tailed, df) # n tailed in tables
            p_val = stats.t.cdf(-1 * t_score if t_score > 0 else t_score, df) * tailed

            res += f"{tailed}-tail hypothesis test with:\n"
            res += f"Difference in means: {x_bar}\n"
            res += f"Degrees of freedom: {df}\n"
            res += f"Significance level: {sig_level/tailed}\n"
            res += f"Standard error: {round(se, 4)}\n"
            res += f"T score: {round(t_score, 4)}\n"
            res += f"Rejection region: {-1 * round(rejection_region, 4)}\n"
            res += f"p value: {round(p_val, 4)}\n"
            res += "\n"

            # decision
            if sig_level > p_val or sig_level < -1 * p_val:
                res += "Reject null hypothesis.\n"
                res += "T score is inside the rejection region.\n"
                res += "p value is less than significance level."
            else:
                res += "Fail to reject null hypothesis.\n"
                res += "T score is not inside the rejection region.\n"
                res += "p value is more than significance level."


            conclusion_label = tk.Label(output_frame, text=res)
            conclusion_label.grid(row=11, column=0, columnspan=2)


        # clear previous inputs
        for widgets in input_frame.winfo_children():
            widgets.destroy()

        sig_level_lab = tk.Label(input_frame, text="Significance level")
        sig_level_val = tk.Entry(input_frame, width=30)

        sig_level_lab.grid(row=1, column=0, sticky="e")
        sig_level_val.grid(row=1, column=1)

        x1_lab = tk.Label(input_frame, text="x bar value for sample 1")
        x1_val = tk.Entry(input_frame, width=30)

        x1_lab.grid(row=2, column=0, sticky="e")
        x1_val.grid(row=2, column=1)

        x2_lab = tk.Label(input_frame, text="x bar value for sample 2")
        x2_val = tk.Entry(input_frame, width=30)

        x2_lab.grid(row=3, column=0, sticky="e")
        x2_val.grid(row=3, column=1)

        n1_lab = tk.Label(input_frame, text="Sample size for sample 1")
        n1_val = tk.Entry(input_frame, width=30)

        n1_lab.grid(row=4, column=0, sticky="e")
        n1_val.grid(row=4, column=1)

        n2_lab = tk.Label(input_frame, text="Sample size for sample 2")
        n2_val = tk.Entry(input_frame, width=30)

        n2_lab.grid(row=5, column=0, sticky="e")
        n2_val.grid(row=5, column=1)

        sd1_lab = tk.Label(input_frame, text="Standard deviation for sample 1")
        sd1_val = tk.Entry(input_frame, width=30)

        sd1_lab.grid(row=6, column=0, sticky="e")
        sd1_val.grid(row=6, column=1)

        sd2_lab = tk.Label(input_frame, text="Standard deviation for sample 2")
        sd2_val = tk.Entry(input_frame, width=30)

        sd2_lab.grid(row=7, column=0, sticky="e")
        sd2_val.grid(row=7, column=1)

        mu_lab = tk.Label(input_frame, text="Hypothesis mean difference")
        mu_val = tk.Entry(input_frame, width=30)

        mu_lab.grid(row=8, column=0, sticky="e")
        mu_val.grid(row=8, column=1)

        tailed_lab = tk.Label(input_frame, text="[1] or [2] tailed")
        tailed_val = tk.Entry(input_frame, width=30)

        tailed_lab.grid(row=9, column=0, sticky="e")
        tailed_val.grid(row=9, column=1)

        next_but = tk.Button(input_frame, text="Next", width=20, command=perform_two_mean)
        next_but.grid(row=10, column=0, columnspan=2)


    def two_mean_pooled():

        def perform_two_mean_pooled():
            # clear previous outputs
            for widgets in output_frame.winfo_children():
                widgets.destroy()

            sig_level = float(sig_level_val.get())

            x_bar1 = float(x1_val.get())
            x_bar2 = float(x2_val.get())
            
            n1 = int(n1_val.get())
            n2 = int(n2_val.get())
            
            sd1 = float(sd1_val.get())
            sd2 = float(sd2_val.get())
            
            IQR1 = float(IQR1_val.get())
            IQR2 = float(IQR2_val.get())
            
            mu = float(mu_val.get())
            tailed = int(tailed_val.get())                

            res = ''

            # check IQR ratios
            if max(IQR1, IQR2) / min(IQR1, IQR2) < 2:
                res += f"Safe to assume equal variances.\n"
                res += f"Ratio of IQRs is less than 2.\n"
                equal_var = True
            else:
                res += f"Not safe to assume equal variances.\n"
                res += f"Ratio of IQRs is not less than 2.\n"
                equal_var = False

            if not equal_var:
                df = min(n1-1, n2-2)
                se = sqrt(sd1**2/n1 + sd2**2/n2)
            else:
                df = n1 + n2 - 2
                s_2_pooled = ((n1-1) * sd1**2 + (n2-1) * sd2**2) / (n1 + n2 - 2)
                se = sqrt(s_2_pooled * (1/n1 + 1/n2))

            t_score = ((x_bar1 - x_bar2) - mu)/se

            rejection_region = stats.t.ppf(sig_level/tailed, df) # n atiled in tables
            p_val = stats.t.cdf(-1 * t_score if t_score > 0 else t_score, df) * tailed

            res += f"{tailed}-tail hypothesis test with:\n"
            res += f"Degrees of freedom: {df}\n"
            res += f"Significance level: {sig_level/tailed}\n"
            res += f"Standard error pooled: {round(se, 4)}\n"
            res += f"T score: {round(t_score, 4)}\n"
            res += f"Rejection region: {-1 * round(rejection_region, 4)}\n"
            res += f"p value: {round(p_val, 4)}\n"
            res += "\n"

            # decision
            if sig_level > p_val or sig_level < -1 * p_val:
                res += f"Reject null hypothesis.\n"
                res += f"T score is inside the rejection region.\n"
                res += "p value is less than significance level."
            else:
                res += f"Fail to reject null hypothesis.\n"
                res += f"T score is not inside the rejection region.\n"
                res += "p value is more than significance level."


            conclusion_label = tk.Label(output_frame, text=res)
            conclusion_label.grid(row=13, column=0, columnspan=2)

        # clear previous inputs
        for widgets in input_frame.winfo_children():
            widgets.destroy()

        sig_level_lab = tk.Label(input_frame, text="Significance level")
        sig_level_val = tk.Entry(input_frame, width=30)

        sig_level_lab.grid(row=1, column=0, sticky="e")
        sig_level_val.grid(row=1, column=1)

        x1_lab = tk.Label(input_frame, text="x bar value for sample 1")
        x1_val = tk.Entry(input_frame, width=30)

        x1_lab.grid(row=2, column=0, sticky="e")
        x1_val.grid(row=2, column=1)

        x2_lab = tk.Label(input_frame, text="x bar value for sample 2")
        x2_val = tk.Entry(input_frame, width=30)

        x2_lab.grid(row=3, column=0, sticky="e")
        x2_val.grid(row=3, column=1)

        n1_lab = tk.Label(input_frame, text="Sample size for sample 1")
        n1_val = tk.Entry(input_frame, width=30)

        n1_lab.grid(row=4, column=0, sticky="e")
        n1_val.grid(row=4, column=1)

        n2_lab = tk.Label(input_frame, text="Sample size for sample 2")
        n2_val = tk.Entry(input_frame, width=30)

        n2_lab.grid(row=5, column=0, sticky="e")
        n2_val.grid(row=5, column=1)

        sd1_lab = tk.Label(input_frame, text="Standard deviation for sample 1")
        sd1_val = tk.Entry(input_frame, width=30)

        sd1_lab.grid(row=6, column=0, sticky="e")
        sd1_val.grid(row=6, column=1)

        sd2_lab = tk.Label(input_frame, text="Standard deviation for sample 2")
        sd2_val = tk.Entry(input_frame, width=30)

        sd2_lab.grid(row=7, column=0, sticky="e")
        sd2_val.grid(row=7, column=1)

        IQR1_lab = tk.Label(input_frame, text="IQR for sample 1")
        IQR1_val = tk.Entry(input_frame, width=30)

        IQR1_lab.grid(row=8, column=0, sticky="e")
        IQR1_val.grid(row=8, column=1)

        IQR2_lab = tk.Label(input_frame, text="IQR for sample 2")
        IQR2_val = tk.Entry(input_frame, width=30)

        IQR2_lab.grid(row=9, column=0, sticky="e")
        IQR2_val.grid(row=9, column=1)

        mu_lab = tk.Label(input_frame, text="Hypothesis mean difference")
        mu_val = tk.Entry(input_frame, width=30)

        mu_lab.grid(row=10, column=0, sticky="e")
        mu_val.grid(row=10, column=1)

        tailed_lab = tk.Label(input_frame, text="[1] or [2] tailed")
        tailed_val = tk.Entry(input_frame, width=30)

        tailed_lab.grid(row=11, column=0, sticky="e")
        tailed_val.grid(row=11, column=1)

        next_but = tk.Button(input_frame, text="Next", width=20, command=perform_two_mean_pooled)
        next_but.grid(row=12, column=0, columnspan=2)


    root = tk.Tk()
    root.title("T Hypothesis Testing")
    root.geometry("500x450")

    type_frame = tk.Frame(root)
    type_frame.pack()

    input_frame = tk.Frame(root)
    input_frame.pack()

    output_frame = tk.Frame(root, relief=tk.GROOVE, borderwidth=3)
    output_frame.pack()

    next_but = tk.Button(type_frame, text="One mean", width=20, command=one_mean)
    next_but.grid(row=0, column=0)

    next_but = tk.Button(type_frame, text="Two mean", width=20, command=two_mean)
    next_but.grid(row=0, column=1)

    next_but = tk.Button(type_frame, text="Two mean pooled", width=20, command=two_mean_pooled)
    next_but.grid(row=0, column=2)

    root.mainloop()


if __name__ == "__main__":
    t_hypothesis_test()