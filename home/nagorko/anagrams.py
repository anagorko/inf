list_words = ["abcd", "abda", "acdb", "abbd", "addb", "acbd", "dcba", "bcda"]

def sort_string(a):
  a = a.lower()
  buckets = {}
  result = []
  for i in range(97, 123):
    buckets[chr(i)] = 0
  for i in a:
    buckets[i] += 1
  for i in buckets:
    result.append(i * buckets[i])
  return "".join(result)


def anagrams(a):
  anagrams_list = []
  result = {}
  for i in a:
    anagrams_list.append(sort_string(i))
  for i in anagrams_list:
    result[i] = result.get(i, 0) + 1
  max_value = max(result.values()) 
  max_keys = [k for k, v in result.items() if v == max_value]
  return(max_keys, max_value)


print(anagrams(list_words))
