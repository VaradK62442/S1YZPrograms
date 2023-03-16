from scipy import stats
from math import sqrt
from math import ceil


def power_level():
    sig_level = float(input("Enter significance level: "))
    se = float(input("Enter standard error: "))
    df = int(input("Enter degrees of freedom: "))
    tailed = int(input("Enter if test is [1] or [2] tailed: "))
    effect_interest = float(input("Enter the size effect of interest: "))

    t_score = stats.t.ppf(sig_level/tailed, df)
    effect_size = t_score * se
    z_score = (effect_size - effect_interest) / (se**2)
    power = round(stats.norm.cdf(z_score), 4)

    print(f'''
    T score: {round(t_score, 4)}
    Effect size should be < {round(effect_size, 4)}
    P(Y < {round(effect_size, 4)}) = P(Z < {round(z_score, 4)}) = {power}
    The power of this test is around {power * 100}%
    ''')


def calc_n():
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
    choice = int(input('''\n[1] Find power level
    \n[2] Find n
    \nChoose type: '''))
    
    if choice == 1:
        power_level()
    elif choice == 2:
        calc_n()


if __name__ == "__main__":
    main()