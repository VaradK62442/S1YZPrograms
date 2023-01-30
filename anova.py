from scipy import stats
from genTables import displayTable


def anova():
    k = int(input("Enter number of groups: "))

    avgs = []
    sizes = []
    for i in range(k):
        avgs.append(float(input(f"Enter mean for group {i+1}: ")))
        sizes.append(int(input(f"Enter size for group {i+1}: ")))

    n = sum(sizes)
    x_bar = sum(avgs)/k # overall avg

    dfg = k - 1 # groups
    dft = n - 1 # total
    dfe = dft - dfg # error

    # sum of squares
    # SSG = sum([(sizes[i] * (avgs[i] - x_bar)) for i in range(k)])
    SSG = 0
    for i in range(k):
        SSG += (sizes[i] * (avgs[i] - x_bar)**2)
    print("SST is the sum from i=1 to n of (x_i - x_bar)^2")
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