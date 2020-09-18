from typing import List
import random


def bucket_sort(numbers: List[int], lowest: int, highest: int) -> List[int]:
  buckets = {i: 0 for i in range(lowest, highest + 1)}
  for num in numbers:
    buckets[num] += 1
  result = []
  for i in range(lowest, highest + 1):
    j = 0
    while j < buckets[i]:
      result.append(i)
      j += 1
  return result

l = [random.randint(-90, 110) for i in range(10)]
print(l)
print(bucket_sort(l, -90, 110))
