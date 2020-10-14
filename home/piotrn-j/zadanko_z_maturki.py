"""Anagramy cyfrowe"""


def number_of_lines(file):
    file = open(file=file, mode='r')

    result = 0

    for line in file:
        number = 0
        a = []
        b = []

        for symbol in line:
            if symbol != ' ' and number == 0:
                a.append(symbol)
            elif symbol == ' ':
                number += 1
            elif symbol != ' ' and number == 1:
                if symbol != '\n':
                    b.append(symbol)

            a = sorted(a)
            b = sorted(b)

        if a == b:
            result += 1

    return result


def biggest_anagram(file):
    file = open(file=file, mode='r')

    num_list = []

    for line in file:
        number = 0
        a = []
        b = []

        for symbol in line:
            if symbol != ' ' and number == 0:
                a.append(symbol)
            elif symbol == ' ':
                number += 1
            elif symbol != ' ' and number == 1:
                if symbol != '\n':
                    b.append(symbol)

        num_list.append("".join(a))
        num_list.append("".join(b))

    num_dict = {}

    for num in num_list:
        if "".join(sorted(num)) not in num_dict.keys():
            num_dict["".join(sorted(num))] = 0
        if "".join(sorted(num)) in num_dict.keys():
            num_dict["".join(sorted(num))] += 1

    return max(num_dict.values())


print(number_of_lines('dane_anagramy.txt'))
print(biggest_anagram('dane_anagramy.txt'))
