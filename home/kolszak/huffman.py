
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


def _character_codes_to_tree(data: Dict[chr, str]) -> Branch:
    tree = Branch()
    current_branch = tree
    for k, v in data.items():
        for i in range(len(v)):
            if v[i] == '0':
                if current_branch.child0 is None:
                    current_branch.child0 = Branch()
                current_branch = current_branch.child0
            elif v[i] == '1':
                if current_branch.child1 is None:
                    current_branch.child1 = Branch()
                current_branch = current_branch.child1
            if i + 1 == len(v):
                current_branch.character = k
        current_branch = tree
    return tree


def _encode(text: str, b: Branch) -> str:
    codes = b.get_characters_codes()
    result = ''
    for c in text:
        result += codes[c]
    return result


def _decode(text: str, b: Branch) -> str:
    codes = b.get_characters_codes()
    t = copy.deepcopy(text)
    result = ''
    i = 0
    while i < len(t) - 1:
        result += b.get_character(t[i:])
        i += len(codes[result[-1]])
    return result


def encode_to_file(text: str, path: str):
    pass


def decode_from_file(path: str) -> str:
    pass


sample_text = 'ala ma kota zjadla koze itd'
occ = _get_occurrences(sample_text)
tree = _generate_tree(occ)
codes = tree.get_characters_codes()
print(occ)
print(codes)
print(_decode(_encode(sample_text, tree), tree))
