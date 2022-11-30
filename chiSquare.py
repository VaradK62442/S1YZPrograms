# perform chi square test on inputted values
# steps:
# 1. get inputs for list of values
# 2. find and sum contributions for each value
# 3. find degrees of freedom
# 4. find p-value using scipy
# 5. output 
# - expected value table, 
# - chi square value, 
# - degrees of freedom, 
# - p-value

from scipy.stats import chi2
from pprint import pprint

def get_observed():
    length = input("Enter number of values: ")
    o = []
    print("Observed values")
    for i in range(int(length)):
        val = float(input(f"Enter value number {i+1}: "))
        o.append(val)

    return o


def get_expected(length):
    e = []
    print("Expected values")
    for i in range(int(length)):
        val = float(input(f"Enter value number {i+1}: "))
        e.append(val)

    return e


def find_chisq(o, e):
    chisq = 0
    for i in range(len(o)):
        chisq += (o[i] - e[i])**2 / e[i]

    return round(chisq, 4)


def find_df(o):
    return len(o)-1


def find_p_val(chisq, df):
    return round(1 - chi2.cdf(chisq, df), 4)


def main():
    # functions
    observed = get_observed()
    expected = get_expected(len(observed))
    sig_level = float(input("Enter significance level: "))
    chisq = find_chisq(observed, expected)
    df = find_df(observed)
    p_val = find_p_val(chisq, df)

    # outputs
    print("\nObserved table: ")
    pprint(observed)
    print("\nExpected table: ")
    pprint(expected)

    print("\nIndependence is assumed.")
    if sum([1 if elt > 5 else 0 for elt in expected]) == len(expected):
        print("Success failure condition satisfied.")
    else:
        print("Success failure condition not satisfied.")

    print(f"\nChi square t stat: {chisq}\nDegrees of freedom: {df}\np-value: {p_val}")

    # decision
    if p_val < sig_level:
        print(f"Since {p_val} < {sig_level}, reject null hypothesis.")
        print("Data does not follow expected distribution.")
    else:
        print(f"Since {p_val} >= {sig_level}, fail to reject null hypothesis.")
        print("Evidence to suggest data follows expected distribution.")


if __name__ == "__main__":
    main()