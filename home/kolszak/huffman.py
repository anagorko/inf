
from typing import List, Dict
import copy


class Branch:
    def __init__(self, child0: 'Branch' = None, child1: 'Branch' = None, character: chr = None):
        self.child0 = child0
        self.child1 = child1
        self.character = character
        self.top = False

    def get_character(self, code: str) -> chr:
        if self.top:
            code = code + '0'
        if self.character is not None:
            return self.character
        elif len(code) == 1:
            return None
        else:
            if code[0] == '0':
                return self.child0.get_character(code[1:])
            elif code[0] == '1':
                return self.child1.get_character(code[1:])
            else:
                return None

    def get_characters_codes(self) -> Dict[chr, str]:
        if self.character is not None:
            return {self.character: ''}
        else:
            a = {k: '0' + v for k, v in self.child0.get_characters_codes().items()}
            b = {k: '1' + v for k, v in self.child1.get_characters_codes().items()}
            return {**a, **b}


def _get_occurrences(text: str) -> Dict[chr, int]:
    result = dict()
    for c in text:
        if result.get(c, None) is None:
            result[c] = 0
        result[c] += 1
    return result


def _generate_tree(occurrences: Dict[chr, int]) -> Branch:
    b_dict = {Branch(character=k): v for k, v in occurrences.items()}
    branches = list(sorted(b_dict.items(), key=lambda item: item[1], reverse=True))
    while len(branches) > 1:
        new_branch = Branch(child0=branches[-1][0], child1=branches[-2][0])
        new_occurrence = branches[-1][1] + branches[-2][1]
        branches = branches[:-2]
        if len(branches) == 0:
            branches.append((new_branch, new_occurrence))
        else:
            for i in range(-1, len(branches)):
                if i + 1 == len(branches) or new_occurrence >= branches[i + 1][1]:
                    branches.insert(i + 1, (new_branch, new_occurrence))
                    break
        del new_branch
        del new_occurrence
    branches[0][0].top = True
    return branches[0][0]


def encode_to_file(text: str, path: str):
    pass


def decode_from_file(path: str) -> str:
    pass


sample_text = 'ala ma kota zjadla koze itd'
occ = _get_occurrences(sample_text)
tree = _generate_tree(occ)
print(occ)
print(tree.get_characters_codes())
