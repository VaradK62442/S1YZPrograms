from scipy import stats
from math import sqrt


def single_mean():
    sig_level = float(input("Enter significance level: "))
    x_bar = float(input("Enter value for x bar: "))
    n = int(input("Enter sample size: "))
    sd = float(input("Enter standard deviation: "))
    mu = float(input("Enter hypothesis mean: "))

    df = n - 1
    se = sd / (sqrt(n))
    t_score = (x_bar - mu)/se

    if t_score > 0:
        t_score *= -1

    p_val = stats.t.cdf(t_score, df) * 2

    print(f"Degrees of Freedom: {df}")
    print(f"Standard error: {round(se, 4)}")
    print(f"T score: {-1 * round(t_score, 4)}")
    print(f"p value: {round(p_val, 4)}")

    # decision
    if sig_level > p_val or sig_level < -1 * p_val:
        print(f"Reject null hypothesis.")
    else:
        print(f"Fail to reject null hypothesis.")


def two_mean():
    x_bar1 = float(input("Enter value for x bar 1: "))
    n1 = int(input("Enter value for n 1: "))
    sd1 = float(input("Enter value for standard deviation 1: "))

    x_bar2 = float(input("Enter value for x bar 2: "))
    n2 = int(input("Enter value for n 2: "))
    sd2 = float(input("Enter value for standard deviation 2: "))

    sig_level = float(input("Enter significance level: "))
    mu = float(input("Enter hypothesis mean difference: "))

    x_bar = x_bar1 - x_bar2
    df = min(n1-1, n2-1)
    se = sqrt((sd1**2 / n1) + (sd2**2 / n2))
    t_score = (x_bar - mu)/se

    if t_score > 0:
        t_score *= -1

    p_val = stats.t.cdf(t_score, df) * 2

    print(f"Difference in means: {x_bar}")
    print(f"Degrees of Freedom: {df}")
    print(f"Standard error: {round(se, 4)}")
    print(f"T score: {-1 * round(t_score, 4)}")
    print(f"p value: {round(p_val, 4)}")

    # decision
    if sig_level > p_val or sig_level < -1 * p_val:
        print(f"Reject null hypothesis.")
    else:
        print(f"Fail to reject null hypothesis.")
    


def menu():
    print("Choose type of test:\n[1] Single mean\n[2] Difference of two means")
    choice = input()
    if choice == "1":
        single_mean()
    elif choice == "2":
        two_mean()


def main():
    menu()


if __name__ == "__main__":
    main()