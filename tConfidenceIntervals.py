from scipy import stats
from math import sqrt

from time import sleep

def single_mean():
    x_bar = float(input("Enter value for x bar: "))
    n = int(input("Enter value for n: "))
    sd = float(input("Enter value for standard deviation: "))
    sig_level = float(input("Enter value for significance level: ")) / 2

    df = n - 1
    t_val = stats.t.ppf(sig_level, df)
    se = sd / (sqrt(n))

    upper_bound = x_bar + t_val * se
    lower_bound = x_bar - t_val * se

    print(f'''Confidence interval with 
    x bar: {x_bar}
    n: {n}
    significance level: {100 * (1 - round(sig_level, 4) * 2)}%
    t value: {round(t_val, 4)}
    standard error: {round(se, 4)}

    upper bound: {round(upper_bound, 4)}
    lower bound: {round(lower_bound, 4)}
    ''')


def two_means():
    x_bar1 = float(input("Enter value for x bar 1: "))
    n1 = int(input("Enter value for n 1: "))
    sd1 = float(input("Enter value for standard deviation 1: "))

    x_bar2 = float(input("Enter value for x bar 2: "))
    n2 = int(input("Enter value for n 2: "))
    sd2 = float(input("Enter value for standard deviation 2: "))

    sig_level = float(input("Enter value for significance level: ")) / 2

    df = min(n1-1, n2-1)
    t_val = stats.t.ppf(sig_level, df)
    se = sqrt((sd1**2 / n1) + (sd2**2 / n2))

    x_bar = x_bar1 - x_bar2

    upper_bound = x_bar + t_val * se
    lower_bound = x_bar - t_val * se

    print(f'''Confidence interval with 
    x bar 1 - x bar 2: {x_bar}
    significance level: {100 * (1 - round(sig_level, 4) * 2)}%
    t value: {-1 * round(t_val, 4)}
    standard error: {round(se, 4)}
    df: {df}

    upper bound: {round(upper_bound, 4)}
    lower bound: {round(lower_bound, 4)}
    ''')


def margin_of_error():
    pass


def menu():
    choice = int(input('''\n[1] Single mean
    \n[2] Difference of two means
    \n[3] Margin of error
    \nChoose type: '''))

    if choice == 1:
        single_mean()
    elif choice == 2:
        two_means()
    elif choice == 3:
        margin_of_error()


def main():
    menu()
    # for i in range(500):
    #     if i % 2 == 0:
    #         print(":() ", end='\r')
    #     else:
    #         print(":( )", end='\r')
    #     sleep(0.1)


if __name__ == "__main__":
    main()