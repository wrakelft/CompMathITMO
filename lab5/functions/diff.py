def diff_table(x, y):
    n = len(x)
    table = []
    for i in range(n):
        row = [x[i], y[i]]
        table.append(row)

    for difs in range(1, n):
        for row in range(n - difs):
            diff = table[row + 1][difs] - table[row][difs]
            table[row].append(diff)

    return table


def print_diff_table(table):
    print("Таблица конечных разностей:")
    print("[")
    for row in table[:-1]:
        print(f" {row},")
    print(f" {table[-1]}")
    print("]")


def convert_table(table):
    n = len(table)
    diffs = []
    for order in range(n):
        diffs_order = []
        for i in range(n - order):
            diffs_order.append(table[i][order + 1])
        diffs.append(diffs_order)
    return diffs
