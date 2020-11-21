with open('data.csv', 'r', encoding='utf-8-sig') as f:
    csv_lines = f.readlines()

rows = []

for line in csv_lines:
    rows.append(line.strip().split(';'))

row_length = len(rows[0])
max_col_lengths = [0] * row_length

for i in range(0, row_length):
    for row in rows:
        element_length = len(row[i])
        if element_length > max_col_lengths[i]:
            max_col_lengths[i] = element_length

for row in rows:
    for i in range(0, row_length):
        element_length = len(row[i])
        if element_length < max_col_lengths[i]:
            row[i] = row[i] + " "*(max_col_lengths[i] - element_length)


col_alignments = "l" + "c"*(row_length-1)

latex_table = """\\begin{table}[htbp]
\\centering
    \\caption{}
    \\label{}
    \\begin{tabular}{""" + col_alignments + """} \\toprule
"""

for i in range(0, len(rows)):
    latex_table += "        " + "  &  ".join(rows[i])
    if i < len(rows) - 1:
        latex_table += "  \\\\ \\addlinespace \n"
    else:
        latex_table += "  \\\\ \\bottomrule \n"


latex_table += """    \\end{tabular}
\\end{table}
"""

with open("table.txt", "w") as f:
    f.write(latex_table)
