from scipy import stats
from genTables import displayTable
from math import sqrt


def anova():
    sig_level = float(input("Enter significance level: "))
    k = int(input("Enter number of groups: "))

    # avgs and sizes
    avgs = [float(input(f"Enter mean for group {i+1}: ")) for i in range(k)]
    sizes = [float(input(f"Enter size for group {i+1}: ")) for i in range(k)]

    # total size and overall average
    n = sum(sizes)
    x_bar = sum([avgs[i] * sizes[i] for i in range(len(avgs))]) / sum(sizes)

    # degrees of freedom
    dfg = k - 1 # groups
    dft = n - 1 # total
    dfe = dft - dfg # error

    # sum of squares
    SSG = sum([sizes[i] * (avgs[i] - x_bar)**2 for i in range(k)])
    print(f"Calculated SSG is {round(SSG, 4)}")
    # SST is too tedious to enter information by hand
    print("SST (total sum of squares) is the sum from i=1 to n of (x_i - x_bar)^2.")
    print("It is also known as the total variability.")
    SST = input("Enter SST for the sample (press enter if unknown): ")
    SSE = input("Enter SSE for the sample (press enter if unknown): ")

    if SST == '':
        SSE = float(SSE)
        SST = SSE + SSG

    elif SSE == '':
        SST = float(SST)
        SSE = SST - SSG

    # mean squares
    MSG = SSG / dfg
    MSE = SSE / dfe

    # F value
    F = MSG / MSE

    # p value
    p = 1 - stats.f.cdf(F, dfg, dfe)

    table = [
        ['', 'df', 'sum sq', 'mean sq', 'F value', 'Pr(>F)'],
        ['Group', dfg, round(SSG, 4), round(MSG, 4), round(F, 4), round(p, 4)],
        ['Error', dfe, round(SSE, 4), round(MSE, 4), '', ''],
        ['Total', dft, round(SST, 4), '', '', '']
    ]

    print(f'''
    Averages: {avgs}
    Sizes: {sizes}
    Total size: {n}
    Overall average: {round(x_bar, 4)}

    Table of anova results:
    ''')
    displayTable(table)
    print()

    if p > sig_level:
        print("Fail to reject H0.")
        print(f"p value of {round(p, 4)} is more than significance level of {sig_level}")

    else:
        print("Reject H0.")
        print(f"p value of {round(p, 4)} is less than significance level of {sig_level}")

        print("If pairwise tests were carried out on these groups,")
        K = k*(k-1)/2
        a_star = sig_level / K
        print(f'{int(K)} pairwise comparisons would need to be made with a new significance level of {a_star}.')
        print(f"The appropriate estimate for the standard deviation for each group is {round(sqrt(MSE), 4)}")


def main():
    anova()


if __name__ == "__main__":
    main()