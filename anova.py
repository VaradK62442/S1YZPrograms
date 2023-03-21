from scipy import stats
from genTables import displayTable
from math import sqrt
import tkinter as tk


# def anova():
#     sig_level = float(input("Enter significance level: "))
#     k = int(input("Enter number of groups: "))

#     # avgs and sizes
#     avgs = [float(input(f"Enter mean for group {i+1}: ")) for i in range(k)]
#     sizes = [float(input(f"Enter size for group {i+1}: ")) for i in range(k)]

#     # total size and overall average
#     n = sum(sizes)
#     x_bar = sum([avgs[i] * sizes[i] for i in range(len(avgs))]) / sum(sizes)

#     # degrees of freedom
#     dfg = k - 1 # groups
#     dft = n - 1 # total
#     dfe = dft - dfg # error

#     # sum of squares
#     SSG = sum([sizes[i] * (avgs[i] - x_bar)**2 for i in range(k)])
#     print(f"Calculated SSG is {round(SSG, 4)}")
#     # SST is too tedious to enter information by hand
#     print("SST (total sum of squares) is the sum from i=1 to n of (x_i - x_bar)^2.")
#     print("It is also known as the total variability.")
#     SST = input("Enter SST for the sample (press enter if unknown): ")
#     SSE = input("Enter SSE for the sample (press enter if unknown): ")

#     if SST == '':
#         SSE = float(SSE)
#         SST = SSE + SSG

#     elif SSE == '':
#         SST = float(SST)
#         SSE = SST - SSG

#     # mean squares
#     MSG = SSG / dfg
#     MSE = SSE / dfe

#     # F value
#     F = MSG / MSE

#     # p value
#     p = 1 - stats.f.cdf(F, dfg, dfe)

#     table = [
#         ['', 'df', 'sum sq', 'mean sq', 'F value', 'Pr(>F)'],
#         ['Group', dfg, round(SSG, 4), round(MSG, 4), round(F, 4), round(p, 4)],
#         ['Error', dfe, round(SSE, 4), round(MSE, 4), '', ''],
#         ['Total', dft, round(SST, 4), '', '', '']
#     ]

#     print(f'''
#     Averages: {avgs}
#     Sizes: {sizes}
#     Total size: {n}
#     Overall average: {round(x_bar, 4)}

#     Table of anova results:
#     ''')
#     displayTable(table)
#     print()

#     if p > sig_level:
#         print("Fail to reject H0.")
#         print(f"p value of {round(p, 4)} is more than significance level of {sig_level}")

#     else:
#         print("Reject H0.")
#         print(f"p value of {round(p, 4)} is less than significance level of {sig_level}")

#         print("If pairwise tests were carried out on these groups,")
#         K = k*(k-1)/2
#         a_star = sig_level / K
#         print(f'''
#         {int(K)} pairwise comparisons would be made with a new significance level of {round(a_star, 4)}.
#         The appropriate estimate for the standard deviation for each group is {round(sqrt(MSE), 4)}.
#         In tests, use MSE ({MSE}) as the variance, dfe ({dfe}) as the degrees of freedom and {round(a_star, 4)}.
#         ''')


def display(root, sig_level, avgs, sizes, n, x_bar, k, dfg, dfe, dft, SSG, SSE, SST, MSG, MSE, F, p):    
    output_frame = tk.Frame(root)
    output_frame.pack()

    basic_info = f'''Averages: {avgs}
    Sizes: {sizes}
    Total size: {n}
    Overall average: {round(x_bar, 4)}
    
    Table of ANOVA results: '''
    basic_label = tk.Label(output_frame, text=basic_info)
    basic_label.grid(row=k+9, column=0, columnspan=6)

    table = [
        ['', 'df', 'sum sq', 'mean sq', 'F value', 'Pr(>F)'],
        ['Group', dfg, round(SSG, 4), round(MSG, 4), round(F, 4), round(p, 4)],
        ['Error', dfe, round(SSE, 4), round(MSE, 4), '', ''],
        ['Total', dft, round(SST, 4), '', '', '']
    ]
    for r_i, row in enumerate(table):
        for c_i, elt in enumerate(row):
            entry = tk.Label(output_frame, text=str(elt))
            entry.grid(row=k+10+r_i, column=c_i)

    conclusion = ''
    if p > sig_level:
        conclusion += "Fail to reject H0.\n"
        conclusion += f"p value of {round(p, 4)} is more than significance level of {sig_level}."
    else:
        conclusion += "Reject H0.\n"
        conclusion += f"p value of {round(p, 4)} is less than significance level of {sig_level}.\n"

        conclusion += "If pairwise tests were carried out on these groups,"
        K = k*(k-1)/2
        a_star = sig_level / K
        conclusion += f'''
        {int(K)} pairwise comparisons would be made with a new significance level of {round(a_star, 4)}.
        The appropriate estimate for the standard deviation for each group is {round(sqrt(MSE), 4)}.
        In tests, use MSE ({MSE}) as the variance, dfe ({dfe}) as the degrees of freedom and {round(a_star, 4)}.
        '''
    conclusion_label = tk.Label(output_frame, text=conclusion)
    conclusion_label.grid(row=k+15, column=0, columnspan=6)


def anova():
    root = tk.Tk()
    root.title("ANOVA")
    root.geometry("800x600")

    def get_sig_k():

        def get_avgs_sizes():

            def get_final_vals():
                SST = SST_in.get()
                SSE = SSE_in.get()

                if SST == '':
                    SSE = float(SSE)
                    SST = SSE + SSG

                elif SSE == '':
                    SST = float(SST)
                    SSE = SST - SSG

                # mean squares
                MSG = SSG / dfg
                MSE = SSE / dfe

                # F value
                F = MSG / MSE

                # p value
                p = 1 - stats.f.cdf(F, dfg, dfe)

                display(root, sig_level, avgs, sizes, n, x_bar, k, dfg, dfe, dft, SSG, SSE, SST, MSG, MSE, F, p)


            # averages and sizes
            avgs = [float(elt.get()) for elt in avgs_vals]
            sizes = [float(elt.get()) for elt in sizes_vals]

            # total size and overall average
            n = sum(sizes)
            x_bar = sum([avgs[i] * sizes[i] for i in range(len(avgs))]) / sum(sizes)

            # degrees of freedom
            dfg = k - 1 # groups
            dft = n - 1 # total
            dfe = dft - dfg # error

            # sum of squares
            SSG = sum([sizes[i] * (avgs[i] - x_bar)**2 for i in range(k)])  

            sum_sq_text = f'''Calculated SSG is {round(SSG, 4)}
            SST (total sum of squares is the sum from i=1 to n of (x_i - x_bar)^2).
            It is also known as the total variability.'''
            sum_sq_info = tk.Label(input_frame, text=sum_sq_text)
            sum_sq_info.grid(row=k+5, column=0, columnspan=4)

            SST_lab = tk.Label(input_frame, text="SST for the sample (leave blank if unknown)")
            SST_in = tk.Entry(input_frame, text="", width=30)
            SST_lab.grid(row=k+6, column=0, columnspan=2)
            SST_in.grid(row=k+6, column=2, columnspan=2)

            SSE_lab = tk.Label(input_frame, text="SSE for the sample (leave blank if unknown)")
            SSE_in = tk.Entry(input_frame, text="", width=30)
            SSE_lab.grid(row=k+7, column=0, columnspan=2)
            SSE_in.grid(row=k+7, column=2, columnspan=2)

            next_but = tk.Button(input_frame, text="Next", width=20, command=get_final_vals)
            next_but.grid(row=k+8, column=0, columnspan=4)


        sig_level = float(sig_level_in.get())
        k = int(k_in.get())

        avgs_vals = []
        sizes_vals = []

        for i in range(k):
            avg_lab = tk.Label(input_frame, text=f"Mean for group {i+1}")
            avg_in = tk.Entry(input_frame, text="", width=30)
            avg_lab.grid(row=i+3, column=0)
            avg_in.grid(row=i+3, column=1, padx=(0, 20))

            avgs_vals.append(avg_in)

            size_lab = tk.Label(input_frame, text=f"Size for group {i+1}")
            size_in = tk.Entry(input_frame, text="", width=30)
            size_lab.grid(row=i+3, column=2, sticky='e', padx=(20,0))
            size_in.grid(row=i+3, column=3)

            sizes_vals.append(size_in)

        next_but = tk.Button(input_frame, text="Next", width=20, command=get_avgs_sizes)
        next_but.grid(row=k+4, column=0, columnspan=4)


    input_frame = tk.Frame(root)
    input_frame.pack()

    sig_level_lab = tk.Label(input_frame, text="Significance level")
    sig_level_in = tk.Entry(input_frame, text="", width=30)
    sig_level_lab.grid(row=0, column=0, sticky="e", columnspan=2)
    sig_level_in.grid(row=0, column=2, columnspan=2)

    k_lab = tk.Label(input_frame, text="Number of groups")
    k_in = tk.Entry(input_frame, text="", width=30)
    k_lab.grid(row=1, column=0, sticky="e", columnspan=2)
    k_in.grid(row=1, column=2, columnspan=2)

    next_but = tk.Button(input_frame, text="Next", width=20, command=get_sig_k)
    next_but.grid(row=2, column=1, columnspan=2)    

    root.mainloop()


if __name__ == "__main__":
    anova()