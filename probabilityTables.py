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
                # check if total row or not:
                if i == rows+1 or j == cols+1:
                    temp.append("t")
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

table = create_empty_table()
table = set_titles(table)

for i in table:
    print(i)