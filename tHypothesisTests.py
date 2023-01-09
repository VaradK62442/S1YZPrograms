from scipy import stats
from math import sqrt


def single_proportion():
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
    print(f"T score: {round(t_score, 4)}")
    print(f"p value: {round(p_val, 4)}")

    # decision
    if sig_level > p_val or sig_level < -1 * p_val:
        print(f"Reject null hypothesis.")
    else:
        print(f"Fail to reject null hypothesis.")


def two_proportion():
    pass


def menu():
    print("Choose type of test:\n[1] Single proportion\n[2] Two proportions")
    choice = input()
    if choice == "1":
        single_proportion()
    elif choice == "2":
        two_proportion()


def main():
    menu()


if __name__ == "__main__":
    main()