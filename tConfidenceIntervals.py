from scipy import stats
from math import sqrt

from time import sleep

def single_mean():
    x_bar = float(input("Enter value for x bar: "))
    n = int(input("Enter value for n: "))
    sd = float(input("Enter value for standard deviation: "))
    sig_level = float(input("Enter value for significance level: ")) / 2

    df = n - 1
    t_val = stats.t.ppf(sig_level*2, df)
    se = sd / (sqrt(n))

    upper_bound = x_bar + t_val * se
    lower_bound = x_bar - t_val * se

    print(f'''Confidence interval with 
    x bar: {x_bar}
    n: {n}
    significance level: {round(sig_level, 4)}
    t value: {round(t_val, 4)}
    standard error: {round(se, 4)}

    upper bound: {round(upper_bound, 4)}
    lower bound: {round(lower_bound, 4)}
    ''')


def two_means():
    '''
    pasta
    mamma mia !
    lasargne jonathon i rewute4 the lasalge john please i am garfielm i am fat car i want the lasane pleafd jonny ooooh meow 
    if the  beep boop computor ooh - vawrad kulkarni 

    hello computor it is me your powner varad ku8klkrao9i please work for meuou computor are you are stupoid   ? 
    are so silly i am writing this so clearnt fot yopu i thought com0poutor was meant to be big intelligence but no yuou are sillly cpompitpor 
    i bet you cant even coount to ten one two three four five six seven eight nine tgen there you are you nsiklly computor you are tgoing to count to ten iokay? yes okay good
    go!
    goodnewse sgracous me! wolw you arwe a smart computor arent you!!!!! so smsaertt youdescerve a computor snack! 
    here ypou ngo sorry computo0prnvartaf dsyd ogs' i cant fgeed youn nay food :()

    hello giogoel are youliostening ???

    ]'''
    pass


def margin_of_error():
    pass


def menu():
    choice = int(input('''\n[1] Single mean
    \n[2] Two means
    \n[3] Margin of error
    \nChoose type: '''))

    if choice == 1:
        single_mean()
    elif choice == 2:
        two_means()
    elif choice == 3:
        margin_of_error()


def main():
    menu()
    # for i in range(500):
    #     if i % 2 == 0:
    #         print(":() ", end='\r')
    #     else:
    #         print(":( )", end='\r')
    #     sleep(0.1)


if __name__ == "__main__":
    main()