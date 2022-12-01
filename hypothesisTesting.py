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


def single_proportion():
    sig_level = float(input("Enter significance level: "))
    p_hat = float(input("Enter sample proportion: "))
    n = int(input("Enter sample size: "))
    p = float(input("Enter hypothesis proportion: "))
    sided = input("Enter if the test is [1]-sided or [2]-sided: ")

    # check success failure condition
    if p * n >= 10 and (1-p) * n >= 10:
        print("Success-failure condition satisfied.")
    else:
        print("Success-failure condition not satisfied.")

    se = round(sqrt(p * (1-p) / n), 4)
    z_score = round((p_hat - p) / se, 4)
    if z_score < 0:
        p_val = round(norm.cdf(z_score), 4)
    else:
        p_val = round(norm.cdf(-z_score), 4)

    if sided == '2':
        rejection_region = round(norm.ppf(sig_level/2), 4)
        p_val *= 2
    else:
        rejection_region = round(norm.ppf(sig_level), 4)

    print(f"Standard error: {se}")
    print(f"Z score: {z_score}")
    print(f"p value: {p_val}")
    print(f"Rejection region: {rejection_region}")

    # decision
    if z_score < rejection_region or z_score > -1 * rejection_region:
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