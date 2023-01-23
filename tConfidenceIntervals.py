from scipy import stats
from math import sqrt

def single_mean():
    x_bar = float(input("Enter value for x bar: "))
    n = int(input("Enter value for n: "))
    sd = float(input("Enter value for standard deviation: "))
    sig_level = float(input("Enter value for significance level: "))
    tailed = int(input("Enter if the test is [1] tailed or [2] tailed: "))

    df = n - 1
    t_val = stats.t.ppf(sig_level/tailed, df) # n tailed in tables
    se = sd / (sqrt(n))

    upper_bound = x_bar + t_val * se
    lower_bound = x_bar - t_val * se

    print(f'''{tailed}-tailed confidence interval with 
    x bar: {x_bar}
    n: {n}
    Significance level: {100 * (1 - round(sig_level, 4))}%
    t value: {round(t_val, 4)}
    Standard error: {round(se, 4)}

    upper bound: {round(upper_bound, 4)}
    lower bound: {round(lower_bound, 4)}
    ''')


def two_means_paired():
    x_bar1 = float(input("Enter value for x bar 1: "))
    n1 = int(input("Enter value for n 1: "))
    sd1 = float(input("Enter value for standard deviation 1: "))

    x_bar2 = float(input("Enter value for x bar 2: "))
    n2 = int(input("Enter value for n 2: "))
    sd2 = float(input("Enter value for standard deviation 2: "))

    sig_level = float(input("Enter value for significance level: "))
    tailed = int(input("Enter if the test is [1] tailed or [2] tailed: "))

    df = min(n1-1, n2-1)
    t_val = stats.t.ppf(sig_level/tailed, df)
    se = sqrt((sd1**2 / n1) + (sd2**2 / n2))

    x_bar = x_bar1 - x_bar2

    upper_bound = x_bar + t_val * se
    lower_bound = x_bar - t_val * se

    print(f'''{tailed}-tailed confidence interval with 
    x bar 1 - x bar 2: {x_bar}
    Significance level: {100 * (1 - round(sig_level, 4))}%
    t value: {-1 * round(t_val, 4)}
    Standard error: {round(se, 4)}
    Degrees of freedom: {df}

    upper bound: {round(upper_bound, 4)}
    lower bound: {round(lower_bound, 4)}
    ''')


def two_means_independent():
    # do not use unless clearly stated 
    # use pooled sd only after careful consideration    
    x_bar1 = float(input("Enter value for x bar 1: "))
    n1 = int(input("Enter value for n 1: "))
    sd1 = float(input("Enter value for standard deviation 1: "))

    x_bar2 = float(input("Enter value for x bar 2: "))
    n2 = int(input("Enter value for n 2: "))
    sd2 = float(input("Enter value for standard deviation 2: "))

    sig_level = float(input("Enter significance level: "))
    tailed = int(input("Enter if the test is [1] tailed or [2] tailed: "))

    df = n1 + n2 - 2
    t_val = stats.t.ppf(sig_level/tailed, df)
    s_2_pooled = ((n1-1) * sd1**2 + (n2-1) * sd2**2) / (n1 + n2 - 2)
    se = sqrt(s_2_pooled * (1/n1 + 1/n2))

    x_bar = x_bar1 - x_bar2

    upper_bound = x_bar + t_val * se
    lower_bound = x_bar - t_val * se

    print(f'''{tailed}-tailed confidence interval with 
    x bar 1 - x bar 2: {x_bar}
    Significance level: {100 * (1 - round(sig_level, 4))}%
    t value: {-1 * round(t_val, 4)}
    Standard error: {round(se, 4)}
    Degrees of freedom: {df}

    upper bound: {round(upper_bound, 4)}
    lower bound: {round(lower_bound, 4)}
    ''')


def main():
    choice = int(input('''\n[1] Single mean
    \n[2] Difference of two means (paired data)
    \n[3] Difference of two means (independent data)
    \nChoose type: '''))

    if choice == 1:
        single_mean()
    elif choice == 2:
        two_means_paired()
    elif choice == 3:
        two_means_independent()


if __name__ == "__main__":
    main()