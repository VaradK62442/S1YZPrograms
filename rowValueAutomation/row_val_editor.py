def change_row_vals(fname, val):
    # increment value of rows by given val
    with open(fname) as f, open("output.txt", "w") as w:
        for line in f.readlines():
            print(line)
            if "row=" in line:
                cur_val = int(line[line.index("row=") + 4])
                new_val = cur_val + val
                line = line.replace("row="+str(cur_val), "row="+str(new_val))
            w.writelines(line)


change_row_vals("rows.txt", -1)