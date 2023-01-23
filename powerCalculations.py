from scipy import stats
from math import sqrt
from math import ceil


def power_cal():
    sig_result = float(input("Enter practically significant result: "))
    sig_level = float(input("Enter significance level: "))
    sd = float(input("Enter standard deviation: "))
    power_level = float(input("Enter desired power (%): ")) / 100

    z_score = stats.norm.ppf(power_level)
    rejection_region = stats.norm.ppf(1 - sig_level/2)
    moe = z_score + rejection_region

    # might need to add choices for different types of data
    # but should work for now
    n = (moe**2 / sig_result**2) * (sd**2 + sd**2)

    print(f'''
    Z score: {round(z_score, 4)}
    Rejection region: {round(rejection_region, 4)}
    Total margin of error: {round(moe, 4)} * SE
    Calculated n: {round(n, 4)}
    Result: {ceil(n)}
    ''')


def main():
    power_cal()


if __name__ == "__main__":
    main()