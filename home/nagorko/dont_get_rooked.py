def is_neighbour(x, y, table):
    if x < 0 or y < 0 or x > len(table[0]) - 1 or y > len(table) - 1:
        return False
    else:
        if table[y][x] == ".":
            return True
    return False


def num_of_neighbours(x, y, table):
    result = 0
    if is_neighbour(x-1, y, table):
        result += 1
    if is_neighbour(x+1, y, table):
        result += 1
    if is_neighbour(x, y-1, table):
        result += 1
    if is_neighbour(x, y+1, table):
        result += 1
    return result


def visualize(table):
    for i in table:
        result = ""
        for j in i:
            result += j
        print(result)


def find_first_grade(table):
    counter = 0
    for x, i in enumerate(table):
        for y, j in enumerate(i):
            if num_of_neighbours(x, y, table) <= 1 and table[y][x] is ".":
                counter += 1
                table[y][x] = "R"
                select_impossible(x, y, table)
    return counter


def select_impossible(rook_x, rook_y, table):
    x1 = rook_x + 1
    while is_neighbour(x1, rook_y, table):
        table[rook_y][x1] = "_"
        x1 += 1
    x1 = rook_x - 1
    while is_neighbour(x1, rook_y, table):
        table[rook_y][x1] = "_"
        x1 += -1
    y1 = rook_y + 1
    while is_neighbour(rook_x, y1, table):
        table[y1][rook_x] = "_"
        y1 += 1
    y1 = rook_y - 1
    while is_neighbour(rook_x, y1, table):
        table[y1][rook_x] = "_"
        y1 += -1


def count_num_walls(row):
    result = 0
    last = ""
    for x, i in enumerate(row):
        if x == 0:
            last = i
            if i is not "X":
                result += 1
        else:
            if last == "X" and i is not "X":
                result += 1
            last = i
    return result


def count_cols_and_rows(table):
    cols = 0
    rows = 0
    last = ""
    for i in table:
        rows += count_num_walls(i)

    for x in range(len(table)):
        for y in range(len(table)):
            if y == 0:
                last = table[y][x]
                if table[y][x] is ".":
                    cols += 1
            else:
                if last == "X" and table[y][x] is ".":
                    cols += 1
                last = table[y][x]
    if cols > rows:
        return rows
    else:
        return cols


def count_all(table):
    return find_first_grade(table) + count_cols_and_rows(table)


board = [["X", ".", "X", "."], [".", ".", ".", "."], [".", ".", ".", "X"], [".", ".", "X", "."]]

visualize(board)
print(count_all(board))
