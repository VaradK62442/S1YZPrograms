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

    se = sqrt(p * (1-p) / n)
    z_score = (p_hat - p) / se
    if z_score < 0:
        p_val = norm.cdf(z_score)
    else:
        p_val = norm.cdf(-z_score)

    if sided == '2':
        rejection_region = norm.ppf(sig_level/2)
        p_val *= 2
    else:
        rejection_region = norm.ppf(sig_level)

    print(f"Standard error: {round(se, 4)}")
    print(f"Z score: {round(z_score, 4)}")
    print(f"p value: {round(p_val, 4)}")
    print(f"Rejection region: {round(rejection_region, 4)}")

    # decision
    if z_score < rejection_region or z_score > -1 * rejection_region:
        print(f"Reject null hypothesis.")
    else:
        print(f"Fail to reject null hypothesis.")


def two_proportion():
    sig_level = float(input("Enter significance level: "))
    p1 = float(input("Enter sample proportion for sample 1: "))
    n1 = int(input("Enter sample size for sample 1: "))
    p2 = float(input("Enter sample proportion for sample 2: "))
    n2 = int(input("Enter sample size for sample 2: "))
    p_null = float(input("Enter hypothesis proportion: "))
    sided = input("Enter if the test is [1]-sided or [2]-sided: ")

    # find p pooled for sf condition
    ppool = (p1 * n1 + p2 * n2) / (n1 + n2)
    n_total = n1 + n2

    # check success failure condition
    if ppool * n_total >= 10 and (1-ppool) * n_total >= 10:
        print("Success-failure condition satisfied.")
    else:
        print("Success-failure condition not satisfied.")

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

    print(f"Pooled proportion: {round(ppool, 4)}")
    print(f"Standard error: {round(se, 4)}")
    print(f"Z score: {round(z_score, 4)}")
    print(f"p value: {round(p_val, 4)}")
    print(f"Rejection region: {round(rejection_region, 4)}")

    # decision
    if z_score < rejection_region or z_score > -1 * rejection_region:
        print(f"Reject null hypothesis.")
    else:
        print(f"Fail to reject null hypothesis.")


def main():
    print("Choose type of test:\n[1] Single proportion\n[2] Two proportions")
    choice = input()
    if choice == "1":
        single_proportion()
    elif choice == "2":
        two_proportion()


if __name__ == "__main__":
    main()