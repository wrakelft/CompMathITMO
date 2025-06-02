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
    for row in table[:-1]:  # Все строки кроме последней
        print(f" {row},")
    print(f" {table[-1]}")  # Последняя строка без запятой
    print("]")
