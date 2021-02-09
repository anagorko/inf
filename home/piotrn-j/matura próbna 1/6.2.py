"""6.1"""

file = open('dane.txt', mode='r')
data = file.read()


def create_list(f):
    l = []
    number = []
    for byte in f:
        if byte in (str(x) for x in range(10)):
            number.append(byte)
        else:
            if len(number) != 0:
                temp_string = "".join(number)
                current_int = int(temp_string)
                l.append(current_int)
                number = []

    return l


def create_rows(f):
    l = create_list(f)

    temp_row = []
    result = []

    for element in l:
        if len(temp_row) != 320:
            temp_row.append(element)
        else:
            result.append(temp_row)
            temp_row = []

    print(len(result))

    return result


create_rows(data)