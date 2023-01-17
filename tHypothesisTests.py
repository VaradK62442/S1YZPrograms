from scipy import stats
from math import sqrt


def single_mean():
    sig_level = float(input("Enter significance level: "))
    x_bar = float(input("Enter value for x bar: "))
    n = int(input("Enter sample size: "))
    sd = float(input("Enter standard deviation: "))
    mu = float(input("Enter hypothesis mean: "))
    tailed = int(input("Enter if the test is [1] tailed or [2] tailed: "))

    df = n - 1
    se = sd / (sqrt(n))
    t_score = (x_bar - mu)/se

    if t_score > 0:
        t_score *= -1

    rejection_region = stats.t.ppf(sig_level/tailed, df) # n tailed in tables
    p_val = stats.t.cdf(t_score, df) * tailed

    print(f'''Hypothesis test with:
    Degrees of Freedom: {df}
    Standard error: {round(se, 4)}
    T score: {-1 * round(t_score, 4)}
    Rejection region: {-1 * round(rejection_region, 2)}
    p value: {round(p_val, 4)}''')

    # decision
    if sig_level > p_val or sig_level < -1 * p_val:
        print(f"Reject null hypothesis.")
        print(f"T score is inside the rejection region.")
        print(f"p value is less than significance level.")
    else:
        print(f"Fail to reject null hypothesis.")
        print(f"T score is not inside the rejection region.")
        print(f"p value is more than significance level.")


def two_mean():
    x_bar1 = float(input("Enter value for x bar 1: "))
    n1 = int(input("Enter value for n 1: "))
    sd1 = float(input("Enter value for standard deviation 1: "))

    x_bar2 = float(input("Enter value for x bar 2: "))
    n2 = int(input("Enter value for n 2: "))
    sd2 = float(input("Enter value for standard deviation 2: "))

    sig_level = float(input("Enter significance level: "))
    mu = float(input("Enter hypothesis mean difference: "))
    tailed = int(input("Enter if the test is [1] tailed or [2] tailed: "))

    x_bar = x_bar1 - x_bar2
    df = min(n1-1, n2-1)
    se = sqrt((sd1**2 / n1) + (sd2**2 / n2))
    t_score = (x_bar - mu)/se

    if t_score > 0:
        t_score *= -1

    p_val = stats.t.cdf(t_score, df) * tailed

    print(f"Difference in means: {x_bar}")
    print(f"Degrees of Freedom: {df}")
    print(f"Standard error: {round(se, 4)}")
    print(f"T score: {-1 * round(t_score, 4)}")
    print(f"p value: {round(p_val, 4)}")

    # decision
    if sig_level > p_val or sig_level < -1 * p_val:
        print(f"Reject null hypothesis.")
        print(f"T score is inside the rejection region.")
        print(f"p value is less than significance level.")
    else:
        print(f"Fail to reject null hypothesis.")
        print(f"T score is not inside the rejection region.")
        print(f"p value is more than significance level.")
    


def main():
    print("Choose type of test:\n[1] Single mean\n[2] Difference of two means")
    choice = input()
    if choice == "1":
        single_mean()
    elif choice == "2":
        two_mean()


if __name__ == "__main__":
    main()