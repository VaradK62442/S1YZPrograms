# form a table with n rows and m cols
# calculate given probability
# incl using bayes theorem

def create_empty_table():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of cols: "))
    # include row and col for titles
    # also include total col and row
    table = []
    for i in range(rows+2): # +2 accounting for title and total row
        temp = []
        for j in range(cols+2):# +2 accounting for title and total cols
            # if title row:
            if i == 0 or j == 0:
                # check if total row/col or not:
                if i == rows+1 or j == cols+1:
                    temp.append("totals")
                else:
                    temp.append("x")
            # otherwise:
            else:
                temp.append(0)
        table.append(temp)

    return table


def set_titles(table):
    for i in range(1, len(table[0])-1): # -1 accounting for total col and row
        table[0][i] = input(f"Enter title for column {i}: ")

    for j in range(1, len(table)-1):
        table[j][0] = input(f"Enter title for row {j}: ")

    table[0][0] = input("Enter title for entire table: ")

    return table


def populate_table(table):
    # loop through values, excluding title and total cols and rows
    for i in range(1, len(table)-1):
        for j in range(1, len(table[i])-1):
            table[i][j] = int(input(f"Enter value for value ({table[i][0]},{table[0][j]}): "))

    return table


def calculate_totals(table):
    # totals for rows
    for i in range(1, len(table)-1):
        for j in range(1, len(table[i])-1):
            # add value to end of respective row and col
            table[i][-1] += table[i][j]
            table[-1][j] += table[i][j]

    # add in final total
    # aka total of totals row/col
    for t in range(1, len(table[-1])-1):
        table[-1][-1] += table[-1][t]

    return table


def displayTable(table):
    s = [[str(e) for e in row] for row in table]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))
    

def main():
    table = create_empty_table()
    table = set_titles(table)
    table = populate_table(table)
    table = calculate_totals(table)
    displayTable(table)

    return table


table = main()