from scipy import stats


def correlation():
    n = int(input("Enter number of observations: "))
    for i in range(x):
        x.append(float(input(f"Enter predictor (x) {i+1}: ")))
        y.append(float(input(f"Enter response (y) {i+1}: ")))

    x_bar = sum(x)/n # avg of x
    y_bar = sum(y)/n # avg of y

    s_x = stats.tstd(x) # st dev for x
    s_y = stats.tstd(y) # st dev for y

    R = (1 / (n-1)) * sum([((x[i] - x_bar) / s_x) * ((y[i] - y_bar) / s_y) for i in range(n)])

    print(f'''
    Avg of x: {x_bar}
    Avg of y: {y_bar}
    St dev of x: {s_x}
    St dev of y: {s_y}

    Correlation: {R}
    ''')


def lin_reg():
    pass


def main():
    choice = int(input('''\n[1] Find correlation
    \n[2] Linear regression
    \nChoose type: '''))
    
    if choice == 1:
        correlation()
    elif choice == 2:
        lin_reg()


if __name__ == "__main__":
    main()