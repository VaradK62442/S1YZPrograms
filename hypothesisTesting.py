# single proportion
#     given significance level, p-hat, n, p, (one or two)-sided test
#         check success-failure condition
#         calculate Z-score
#         calculate p-value
# two proportions
#     given significance level, p-hat, n, p, (one or two)-sided test
#         find pooled proportion
#         check success-failure condition
#         calculate Z-score
#         calculate p-value

from math import sqrt
from scipy.stats import norm
import tkinter as tk


# def single_proportion():
#     sig_level = float(input("Enter significance level: "))
#     p_hat = float(input("Enter sample proportion: "))
#     n = int(input("Enter sample size: "))
#     p = float(input("Enter hypothesis proportion: "))
#     sided = input("Enter if the test is [1]-sided or [2]-sided: ")

#     # check success failure condition
#     if p * n >= 10 and (1-p) * n >= 10:
#         print("Success-failure condition satisfied.")
#     else:
#         print("Success-failure condition not satisfied.")

#     se = sqrt(p * (1-p) / n)
#     z_score = (p_hat - p) / se
#     if z_score < 0:
#         p_val = norm.cdf(z_score)
#     else:
#         p_val = norm.cdf(-z_score)

#     if sided == '2':
#         rejection_region = norm.ppf(sig_level/2)
#         p_val *= 2
#     else:
#         rejection_region = norm.ppf(sig_level)

#     print(f"Standard error: {round(se, 4)}")
#     print(f"Z score: {round(z_score, 4)}")
#     print(f"p value: {round(p_val, 4)}")
#     print(f"Rejection region: {round(rejection_region, 4)}")

#     # decision
#     if z_score < rejection_region or z_score > -1 * rejection_region:
#         print(f"Reject null hypothesis.")
#     else:
#         print(f"Fail to reject null hypothesis.")


# def two_proportion():
#     sig_level = float(input("Enter significance level: "))
#     p1 = float(input("Enter sample proportion for sample 1: "))
#     n1 = int(input("Enter sample size for sample 1: "))
#     p2 = float(input("Enter sample proportion for sample 2: "))
#     n2 = int(input("Enter sample size for sample 2: "))
#     p_null = float(input("Enter hypothesis proportion: "))
#     sided = input("Enter if the test is [1]-sided or [2]-sided: ")

#     # find p pooled for sf condition
#     ppool = (p1 * n1 + p2 * n2) / (n1 + n2)
#     n_total = n1 + n2

#     # check success failure condition
#     if ppool * n_total >= 10 and (1-ppool) * n_total >= 10:
#         print("Success-failure condition satisfied.")
#     else:
#         print("Success-failure condition not satisfied.")

#     se = sqrt((p1 * (1-p1) / n1) + (p2 * (1-p2) / n2))
#     z_score = ((p1 - p2) - p_null) / se
#     if z_score < 0:
#         p_val = norm.cdf(z_score)
#     else:
#         p_val = norm.cdf(-z_score)

#     if sided == '2':
#         rejection_region = norm.ppf(sig_level/2)
#         p_val *= 2
#     else:
#         rejection_region = norm.ppf(sig_level)

#     print(f"Pooled proportion: {round(ppool, 4)}")
#     print(f"Standard error: {round(se, 4)}")
#     print(f"Z score: {round(z_score, 4)}")
#     print(f"p value: {round(p_val, 4)}")
#     print(f"Rejection region: {round(rejection_region, 4)}")

#     # decision
#     if z_score < rejection_region or z_score > -1 * rejection_region:
#         print(f"Reject null hypothesis.")
#     else:
#         print(f"Fail to reject null hypothesis.")


# def main():
#     print("Choose type of test:\n[1] Single proportion\n[2] Two proportions")
#     choice = input()
#     if choice == "1":
#         single_proportion()
#     elif choice == "2":
#         two_proportion()


def hypothesis_test():

    def prop_chosen():

        def one_prop():

            def perform_one_prop():
                # clear previous outputs
                for widgets in output_frame.winfo_children():
                    widgets.destroy() 

                # get all values
                sig_level = float(sig_level_val.get())
                p_hat = float(p_hat_val.get())
                n = int(n_val.get())
                p = float(p_val.get())
                sided = sided_val.get()

                res = ''

                # check success failure condition
                if p * n >= 10 and (1-p) * n >= 10:
                    res += "Success-failure condition satisfied.\n"
                else:
                    res += "Success-failure condition not satisfied.\n"

                se = sqrt(p * (1-p) / n)
                z_score = (p_hat - p) / se
                if z_score < 0:
                    p_value = norm.cdf(z_score)
                else:
                    p_value = norm.cdf(-z_score)

                if sided == '2':
                    rejection_region = norm.ppf(sig_level/2)
                    p_value *= 2
                else:
                    rejection_region = norm.ppf(sig_level)

                res += f"Standard error: {round(se, 4)}\n"
                res += f"Z score: {round(z_score, 4)}\n"
                res += f"p value: {round(p_value, 4)}\n"
                res += f"Rejection region: {round(rejection_region, 4)}\n"

                # decision
                if z_score < rejection_region or z_score > -1 * rejection_region:
                    res += f"Reject null hypothesis.\n"
                else:
                    res += f"Fail to reject null hypothesis.\n"

                conclusion_label = tk.Label(output_frame, text=res)
                conclusion_label.grid(row=8, column=0, columnspan=2)


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

            p_lab = tk.Label(input_frame, text="Hypothesis proportion")
            p_val = tk.Entry(input_frame, width=30)

            p_lab.grid(row=5, column=0, sticky="e")
            p_val.grid(row=5, column=1)

            sided_lab = tk.Label(input_frame, text="[1] sided or [2] sided")
            sided_val = tk.Entry(input_frame, width=30)

            sided_lab.grid(row=6, column=0, sticky="e")
            sided_val.grid(row=6, column=1)

            next_but = tk.Button(input_frame, text="Next", width=20, command=perform_one_prop)
            next_but.grid(row=7, column=0, columnspan=2) 


        def two_prop():

            def perform_two_prop():
                # clear previous outputs
                for widgets in output_frame.winfo_children():
                    widgets.destroy() 

                # get all values
                sig_level = float(sig_level_val.get())
                p1 = float(p1_val.get())
                p2 = float(p2_val.get())
                n1 = int(n1_val.get())
                n2 = int(n2_val.get())
                p_null = float(p_null_val.get())
                sided = sided_val.get()

                res = ''

                # find p pooled for sf condition
                ppool = (p1 * n1 + p2 * n2) / (n1 + n2)
                n_total = n1 + n2

                # check success failure condition
                if ppool * n_total >= 10 and (1-ppool) * n_total >= 10:
                    res += "Success-failure condition satisfied.\n"
                else:
                    res += "Success-failure condition not satisfied.\n"

                se = sqrt((p1 * (1-p1) / n1) + (p2 * (1-p2) / n2))
                z_score = ((p1 - p2) - p_null) / se
                if z_score < 0:
                    p_val = norm.cdf(z_score)
                else:
                    p_val = norm.cdf(-z_score)

                if sided == '2':
                    rejection_region = norm.ppf(sig_level/2)
                    p_val *= 2
                else:
                    rejection_region = norm.ppf(sig_level)

                res += f"Pooled proportion: {round(ppool, 4)}\n"
                res += f"Standard error: {round(se, 4)}\n"
                res += f"Z score: {round(z_score, 4)}\n"
                res += f"p value: {round(p_val, 4)}\n"
                res += f"Rejection region: {round(rejection_region, 4)}\n"

                # decision
                if z_score < rejection_region or z_score > -1 * rejection_region:
                    res += f"Reject null hypothesis.\n"
                else:
                    res += f"Fail to reject null hypothesis.\n"

                conclusion_label = tk.Label(output_frame, text=res)
                conclusion_label.grid(row=8, column=0, columnspan=2)


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

            p_null_lab = tk.Label(input_frame, text="Hypothesis proportion")
            p_null_val = tk.Entry(input_frame, width=30)

            p_null_lab.grid(row=7, column=0, sticky="e")
            p_null_val.grid(row=7, column=1)

            sided_lab = tk.Label(input_frame, text="[1] sided or [2] sided")
            sided_val = tk.Entry(input_frame, width=30)

            sided_lab.grid(row=8, column=0, sticky="e")
            sided_val.grid(row=8, column=1)

            next_but = tk.Button(input_frame, text="Next", width=20, command=perform_two_prop)
            next_but.grid(row=9, column=0, columnspan=2)

        sided = prop_val.get()

        if sided == 1:
            one_prop()
        elif sided == 2:
            two_prop()


    root = tk.Tk()
    root.title("Hypothesis testing")
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
    hypothesis_test()