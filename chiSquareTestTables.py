from genProbabilityTables import main as make_table, displayTable
from scipy.stats import chi2
from copy import deepcopy
from pprint import pprint

table = make_table()

# table = [['test', '<5 yrs', '5-10 yrs', '>10 yrs', 'totals'],
#         ['widow', 25, 42, 33, 100],
#         ['widowed', 78, 80, 42, 200],
#         ['totals', 103, 122, 75, 300]]

# perform chi square test on inputted table
# steps:
# 1. create table of expected values, based on totals
# 2. find and sum contributions for each value
# 3. find degrees of freedom
# 4. find p-value using scipy
# 5. output 
# - expected value table, 
# - chi square value, 
# - degrees of freedom, 
# - p-value

def create_expected_value_table(table):
    expected_table = deepcopy(table)
    for row in range(1, len(expected_table)-1):
        for col in range(1, len(expected_table[row])-1):
            # set current value to rowTotal * colTotal / total
            row_total = expected_table[-1][col]
            col_total = expected_table[row][-1]
            total = expected_table[-1][-1]
            expected_table[row][col] =  round(row_total * col_total / total, 2)

    return expected_table 


def find_chisq(o_table, e_table):
    chisq = 0
    for row in range(1, len(o_table)-1):
        for col in range(1, len(o_table[row])-1):
            observed_val = o_table[row][col]
            expected_val = e_table[row][col]
            chisq += ((observed_val - expected_val) ** 2) / expected_val

    return chisq


def find_df(table):
    return (len(table)-3) * (len(table[0])-3)


def find_p_val(chisq, df):
    return 1 - chi2.cdf(chisq, df)


def main():
    # functions
    expected_table = create_expected_value_table(table)
    chisq = find_chisq(table, expected_table)
    df = find_df(table)
    p_val = find_p_val(chisq, df)

    # output
    displayTable(table)
    print()
    displayTable(expected_table)
    print()
    print(f"Chi square t stat: {chisq}\nDegrees of freedom: {df}\np-value: {p_val}")


if __name__ == "__main__":
    main()