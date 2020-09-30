"""Group all anagrams from a word list."""

with open('words.polish', 'r') as word_list_file:
    word_list = word_list_file.readlines()

groups = dict()
for key, word in [(''.join(sorted(word[:-1])), word[:-1]) for word in word_list]:
    if key not in groups:
        groups[key] = []
    groups[key].append(word)

for key, group in groups.items():
    if len(group) > 5:
        print(key, group)
