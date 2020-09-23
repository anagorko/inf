from typing import Dict
from typing import List
from typing import Set


def sort_word(a: str) -> List[int]:
    min_value, max_value = 0, 127
    values = [ord(c) for c in a]
    buckets = {i: 0 for i in range(min_value, max_value + 1)}
    for value in values:
        buckets[value] += 1
    result = list()
    for i in range(min_value, max_value + 1):
        for _ in range(buckets[i]):
            result.append(i)
    return result


def is_anagram(a: str, b: str) -> bool:
    return sort_word(a) == sort_word(b)


def get_anagrams(data: List[str]) -> Dict[str, Set[str]]:
    result = dict()
    for value in data:
        v = [chr(i) for i in sort_word(value)]
        v_str = ''.join(v)
        if result.get(v_str, 0) == 0:
            result[v_str] = set()
        result[v_str].add(value)
    return result


path = 'C:/Users/IChri/Downloads/words.txt' #file path
f = open(path, 'r')
data = f.readlines()
anagrams = get_anagrams(data)

most_common_anagram = ''
longest_anagram = ''
for k, v in anagrams.items():
    if len(v) > len(most_common_anagram):
        most_common_anagram = k
    if len(v) > 1:
        if len(k) > len(longest_anagram):
            longest_anagram = k

print(f'most common anagram: {most_common_anagram} : {len(most_common_anagram) - 1}') #len returns 1 higher value
print()
print(f'longest anagram: {longest_anagram} : {len(longest_anagram) - 1}') #len returns 1 higher value

