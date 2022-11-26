# find sum
# find mean
# find variance
# find quartiles
# find upper and lower fence
# find outliers

from math import sqrt

def get_list():
    n = int(input("Enter number of elements in data: "))
    return [int(input(f"Enter element {i+1}: ")) for i in range(n)]


def find_quartiles(l):
    quartiles = []
    

    return quartiles


def main():
    l = get_list()
    total = sum(l)
    n = len(l)
    mean = total / n
    stdev = sum([(elt - mean) for elt in l]) / (n-1)
    var = sqrt(stdev)

    print(f'''
    Inputted values: {l}\n
    Sum: {total}\n
    Mean: {mean}\n 
    Standard deviation: {stdev}\n 
    Variance: {var}\n 
    ''')


if __name__ == "__main__":
    main()