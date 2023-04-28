def change_row_vals(fname, val):
    # increment value of rows by given val
    with open(fname) as f, open("./rowValueAutomation/output.txt", "w") as w:
        for line in f.readlines():
            if "row=" in line:
                row_index = line.index("row=")
                equals_index = row_index + 3
                cur_val_index = line[row_index:].index(",") + row_index
                cur_val = int(line[equals_index+1:cur_val_index])
                new_val = cur_val + val
                line = line.replace("row="+str(cur_val), "row="+str(new_val))
            w.writelines(line)


change_row_vals("./rowValueAutomation/rows.txt", -1)