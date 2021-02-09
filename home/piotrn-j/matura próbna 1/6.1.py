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


file_list = create_list(data)


def brightest(f):
    current_max = 0

    for pixel in f:
        if int(pixel) > current_max:
            current_max = pixel

    return current_max


def darkest(f):
    current_min = 255

    for pixel in f:
        if int(pixel) < current_min:
            current_min = pixel

    return current_min


print(brightest(file_list), max(file_list), darkest(file_list), min(file_list))
