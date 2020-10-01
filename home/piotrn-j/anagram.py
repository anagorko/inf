"""Anagrams"""


def bucket_sort(given_word):
    """Bucket sort algorithm implementation"""

    result = [0 for _ in range(127)]
    result_final = []

    for element in given_word:
        result[ord(element)] += 1

    index = 0

    for element in result:
        for _ in range(element):
            result_final.append(chr(index))
        index += 1

    result_final = "".join(result_final)

    return result_final


def is_anagram(pre_sorted_word_1, pre_sorted_word_2):
    """Checks if two given words are anagrams"""

    if pre_sorted_word_1 == pre_sorted_word_2:
        return True
    else:
        return False


def read_and_check(file):
    """Finds all the anagrams in a given text file"""
    f = open(file, 'r')
    dictionary = f.read()
    dictionary_list = []
    temporary_list = []

    for element in dictionary:
        if element == '\n':
            dictionary_list.append(temporary_list)
            temporary_list = []
        else:
            temporary_list.append(element)

    dictionary_list = ["".join(word) for word in dictionary_list]

    proper_dictionary = {}
    anagram_list = []
    temp_index = 0

    for word in dictionary_list:
        sorted_word = bucket_sort(word)
        if sorted_word not in proper_dictionary:
            proper_dictionary[sorted_word] = [word]
        else:
            loop_list = proper_dictionary[sorted_word]
            loop_list.append(word)
            proper_dictionary[sorted_word] = loop_list
        print(temp_index)
        temp_index += 1

    temp_index = 0

    for key in proper_dictionary:
        print(temp_index)
        if len(proper_dictionary[key]) > 1:
            anagram_list.append(proper_dictionary[key])
        temp_index += 1

    max_len = []

    for element in anagram_list:
        if len(element) > len(max_len):
            max_len = element

    max_len = [bucket_sort(max_len[1]) + ':'] + max_len
    final_result = [", ".join(max_len)]

    print('The biggest amount of words for one anagram is: ' + str(len(max_len) - 1))
    print('The anagram and all its words are: ' + final_result[0])


read_and_check('words.txt')
