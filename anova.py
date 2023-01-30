from scipy import stats
from genTables import displayTable


def anova():
    k = int(input("Enter number of groups: "))

    # avgs and sizes
    avgs = [float(input(f"Enter mean for group {i+1}: ")) for i in range(k)]
    sizes = [float(input(f"Enter size for group {i+1}: ")) for i in range(k)]

    # total size and overall average
    n = sum(sizes)
    x_bar = sum(avgs)/k

    # degrees of freedom
    dfg = k - 1 # groups
    dft = n - 1 # total
    dfe = dft - dfg # error

    # sum of squares
    SSG = sum([(sizes[i] * (avgs[i] - x_bar)**2) for i in range(k)])
    # SST is too tedious to enter information by hand
    print("SST (total sum of squares) is the sum from i=1 to n of (x_i - x_bar)^2")
    SST = float(input("Enter SST for the sample: "))
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


def main():
    anova()


if __name__ == "__main__":
    main()