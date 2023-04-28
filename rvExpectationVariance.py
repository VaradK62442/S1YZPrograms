# program to calculate expected value and variance value
# given probabilities and outcomes

from math import sqrt
import tkinter as tk

# def get_inputs():
#     outcome_count = int(input("Enter how many outcomes you have: "))

#     outcomes, probabilities = [], []

#     for i in range(outcome_count):
#         outcomes.append(int(input(f"Enter value of outcome {i+1}: ")))
#         probability_i = (input(f"Enter probability of outcome {i+1}: "))
#         # convert probability to float
#         if '/' in probability_i:
#             num, denom = probability_i.split('/')
#             probabilities.append(float(num)/float(denom))
#         else:
#             probabilities.append(float(probability_i))

#     return outcomes, probabilities


# def get_expected_value(outcomes, probabilities):
#     expected_val = 0
#     for i in range(len(outcomes)):
#         expected_val += outcomes[i] * probabilities[i]

#     return expected_val


# def get_variance_value(outcomes, probabilities, expected_val):
#     variance_val = 0
#     for i in range(len(outcomes)):
#         variance_val += (outcomes[i]-expected_val)**2 * probabilities[i]

#     return variance_val


# out, prob = get_inputs()
# exp = get_expected_value(out, prob)
# var = get_variance_value(out, prob, exp)
# std = sqrt(var)

# print(f"Expected value: {exp}\nVariance value: {var}\nStandard deviation: {std}")


def rv():

    def get_outcomes():

        def get_exp_var():
            # clear previous inputs
            for widgets in output_frame.winfo_children():
                widgets.destroy() 

            outcome_vals = [int(elt.get()) for elt in outcomes]
            prob_vals = []

            # convert probabilities to floats
            for elt in probabilities:
                if '/' in elt.get():
                    num, denom = elt.get().split('/')
                    prob_vals.append(float(num)/float(denom))
                else:
                    prob_vals.append(float(elt.get()))

            expected_val = 0
            variance_val = 0

            for i in range(len(outcome_vals)):
                expected_val += outcome_vals[i] * prob_vals[i]

            for i in range(len(outcome_vals)):
                variance_val += (outcome_vals[i] - expected_val) ** 2 * prob_vals[i]

            # display(root, expected_val, variance_val, outcome_count)

            std = sqrt(variance_val)

            res = ''

            res += f"Expected value: {round(expected_val, 4)}\n"
            res += f"Variance value: {round(variance_val, 4)}\n"
            res += f"Standard deviation: {round(std, 4)}"

            info_label = tk.Label(output_frame, text=res)
            info_label.grid(row=outcome_count+5, column=0, columnspan=4)


        # clear previous inputs
        for widgets in table_frame.winfo_children():
            widgets.destroy() 

        outcome_count = int(outcomes_in.get())
        outcomes, probabilities = [], []

        for i in range(outcome_count):
            outcome_lab = tk.Label(table_frame, text=f"Value of outcome {i+1}")
            outcome_in = tk.Entry(table_frame, width=30)
            outcome_lab.grid(row=i+3, column=0)
            outcome_in.grid(row=i+3, column=1, padx=(0, 20))

            outcomes.append(outcome_in)

            prob_lab = tk.Label(table_frame, text=f"Probability of outcome {i+1}")
            prob_in = tk.Entry(table_frame, width=30)
            prob_lab.grid(row=i+3, column=2, sticky='e', padx=(20, 0))
            prob_in.grid(row=i+3, column=3)

            probabilities.append(prob_in)
            
        # for i in range(outcome_count):
        #     n_lab = tk.Label(input_frame, text=f"Entry {i+1}")
        #     n_lab.grid(row=3, column=i+1)

        # outcome_lab = tk.Label(input_frame, text="Outcomes")
        # outcome_lab.grid(row=4, column=0)
        # prob_lab = tk.Label(input_frame, text="Probabilities")
        # prob_lab.grid(row=5, column=0)

        # for i in range(outcome_count):
        #     outcome_in = tk.Entry(input_frame, width=10)
        #     outcome_in.grid(row=4, column=i+1, padx=(0, 20))

        #     outcomes.append(outcome_in)

        #     prob_in = tk.Entry(input_frame, width=10)
        #     prob_in.grid(row=5, column=i+1, padx=(0, 20))

        #     probabilities.append(prob_in)

        next_but = tk.Button(table_frame, text="Next", width=20, command=get_exp_var)
        next_but.grid(row=outcome_count+4, column=0, columnspan=4)

    
    root = tk.Tk()
    root.title("Random variables")
    root.geometry("700x350")

    input_frame = tk.Frame(root)
    input_frame.pack()

    table_frame = tk.Frame(root)
    table_frame.pack()

    output_frame = tk.Frame(root, relief=tk.GROOVE, borderwidth=3)
    output_frame.pack()

    outcomes_lab = tk.Label(input_frame, text="Number of groups")
    outcomes_in = tk.Entry(input_frame, text="", width=30)

    outcomes_lab.grid(row=1, column=0, sticky="e")
    outcomes_in.grid(row=1, column=1)

    next_but = tk.Button(input_frame, text="Next", width=20, command=get_outcomes)
    next_but.grid(row=2, column=0, columnspan=2)    

    root.mainloop()


if __name__ == "__main__":
    rv()