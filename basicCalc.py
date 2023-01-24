# find sum
# find mean
# find variance
# find quartiles
# find upper and lower fence
# find outliers

from math import sqrt
import numpy as np

def get_list():
    n = int(input("Enter number of elements in data: "))
    return [int(input(f"Enter element {i+1}: ")) for i in range(n)]


def main():
    # l = [0, 100, 500, 600, 1000, 100000]
    l = sorted(get_list())
    total = sum(l)
    n = len(l)
    mean = total / n
    stdev = round(sum([(elt - mean)**2 for elt in l]) / (n-1), 4)
    var = round(sqrt(stdev), 4)

    q1, q2, q3 = np.quantile(l, [0.25,0.5,0.75]) 

    IQR = q3 - q1
    upper_fence = q3 + 1.5 * IQR
    lower_fence = q1 - 1.5 * IQR

    outliers = [elt for elt in l if (elt > upper_fence or elt < lower_fence)]

    print(f'''
    Inputted values: {l}\n
    Sum: {total}\n
    Mean: {mean}\n 
    Standard deviation: {stdev}\n 
    Variance: {var}\n 
    Q1 - {q1}, Q2 - {q2}, Q3 - {q3}\n
    IQR: {IQR}\n
    Upper fence: {upper_fence}\n
    Lower fence: {lower_fence}\n
    Outliers: {outliers}
    ''')


if __name__ == "__main__":
    main()