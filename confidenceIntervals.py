# single proportion
#     get p hat, n, significance level
#     check success failure condition
#     calculate confidence interval
# two proportions
#     calculate X% confidence interval given
#         p1, p2, n1, n2, p1-hat, p2-hat, significance level

from scipy import stats # to find z_val
from math import sqrt

def single_proportion():
    p_hat = float(input("Enter value for p hat: "))
    n = int(input("Enter value for n: "))
    sig_level = float(input("Enter value for significance level: "))

    # check sf condition
    if p_hat * n > 5 and (1-p_hat) * n > 5:
        print(f'''Success-failure condition satisfied.''')
    else:
        print(f'''Success-failure condition not satisfied.''')

    z_val = -1 * (stats.norm.ppf(sig_level/2))
    se = sqrt(p_hat * (1-p_hat) / n)

    upper_bound = p_hat + z_val * se
    lower_bound = p_hat - z_val * se

    print(f'''Confidence interval with 
    p hat: {p_hat}
    n: {n}
    significance level: {round(sig_level, 4)}
    z value: {round(z_val, 4)}
    standard error: {round(se, 4)}

    upper bound: {round(upper_bound, 4)}
    lower bound: {round(lower_bound, 4)}
    ''')


def two_proportion():
    p1 = float(input("Enter proportion for sample 1: "))
    n1 = int(input("Enter sample size for sample 1: "))
    p2 = float(input("Enter proportion for sample 2: "))
    n2 = int(input("Enter sample size for sample 2: "))
    sig_level = float(input("Enter significance level: "))

    # check sf condition
    sf1 = True if p1*n1 > 5 and (1-p1)*n1 > 5 else False
    sf2 = True if p2*n2 > 5 and (1-p2)*n2 > 5 else False
    if sf1 and sf2:
        print("Success-failure condition satisfied.")
    else:
        print("Success-failure condition not satisfied.")

    z_val = -1 * (stats.norm.ppf(sig_level/2))
    se = sqrt((p1 * (1-p1) / n1) + (p2 * (1-p2) / n2))
    diff = p1 - p2

    upper_bound = diff + z_val * se
    lower_bound = diff - z_val * se

    print(f'''Confidence interval with 
    p1: {p1}
    n1: {n1}
    p2: {p2}
    n2: {n2}
    significance level: {round(sig_level, 4)}
    z value: {round(z_val, 4)}
    standard error: {round(se, 4)}
    p1 - p2: {round(diff, 4)}

    upper bound: {round(upper_bound, 4)}
    lower bound: {round(lower_bound, 4)}
    ''')


def margin_of_error():
    pass


def menu():
    choice = int(input('''\n[1] Single proportion
    \n[2] Two proportions
    \n[3] Margin of error
    \nChoose type: '''))

    if choice == 1:
        single_proportion()
    elif choice == 2:
        two_proportion()
    elif choice == 3:
        margin_of_error()


def main():
    menu()


if __name__ == "__main__":
    main()