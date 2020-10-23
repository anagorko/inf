
from typing import List, Dict
import copy


def _to_bytes(data: str) -> bytes:
    b = bytearray()
    for i in range(0, len(data), 8):
        b.append(int(data[i:i+8], 2))
    return bytes(b)


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


def _generate_tree_from_occurrences(occurrences: Dict[chr, int]) -> Branch:
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


def _generate_tree_from_characters_codes(data: Dict[chr, str]) -> Branch:
    tree = Branch()
    tree.top = True
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


def _encode(text: str, tree: Branch) -> str:
    codes = tree.get_characters_codes()
    result = ''
    for c in text:
        result += codes[c]
    return result


def _decode(text: str, tree: Branch) -> str:
    codes = tree.get_characters_codes()
    t = copy.deepcopy(text)
    result = ''
    i = 0
    while i < len(t) - 1:
        result += tree.get_character(t[i:])
        i += len(codes[result[-1]])
    return result


def compress(text: str, path: str):
    tree = _generate_tree_from_occurrences(_get_occurrences(text))
    codes = tree.get_characters_codes()
    encoded = _encode(text, tree)
    with open(path, 'w') as file:
        file.write(f'{str(len(codes))}\n')
        file.write(f'{str(len(encoded))}\n')
        for k, v in codes.items():
            file.write(f'{k} {v} ')
        file.write('\n')
        file.close()
    with open(path, 'a+b') as file:
        file.write(_to_bytes(encoded))
        file.close()


def decompress(path: str) -> str:
    codes = dict()
    with open(path, 'rb') as file_b:
        file_b.seek(0)
        fb_lines_reader = file_b.readlines()
        file_b.seek(0)
        fb_reader = file_b.read()
        character_count = int(fb_lines_reader[0].decode())
        data_len = int(fb_lines_reader[1].decode())
        i = len(fb_lines_reader[0].decode()) + len(fb_lines_reader[1].decode())
        for kv in range(character_count):
            key = chr(fb_reader[i])
            if key == '\r' and chr(fb_reader[i+1]) == '\n':
                key = '\n'
                i += 1
            i += 2
            value = ''
            while chr(fb_reader[i]) != ' ':
                value += chr(fb_reader[i])
                i += 1
            codes[key] = value
            i += 1
        tree = _generate_tree_from_characters_codes(codes)
        i += 2
        encoded = ''
        for byte in fb_reader[i:]:
            bits = bin(byte)[2:].rjust(8, '0')
            encoded += bits
        last = encoded[-8:]
        encoded = encoded[:data_len - data_len % 8]
        encoded += last[-data_len % 8:] if data_len % 8 > 0 else ''
        file_b.close()
        decoded = _decode(encoded, tree)
        return decoded


sample_text = 'przykladowy tekst itd\n w to jest tekst do testow zobaczmy jak skutecznie sie kompresuje test test test\r\n ' \
              'adsasd hadkjas \n\r' \
              'afdsdhjhjkf uiof  fk dfa hjkl dfgs gk kajf  a   sjhkdfdhjfjdhfhfjdjhfdhjfhdjfdjhfhjdfdjhfdhjfjhdfhjdfdfhjdhjfdhj  djsdalsdiaos  alksdj' \
              'dfsdfsdffds\r\n asdyyyyyyyyyyyyyybmn     aljksdjklas  alksdjjjjjjjjjj smn              skdjsdjsipoqe;iuasjkdlasd  das' \
              'sdasjhd \n\n\n\n\n asdjasd asdjkasdh \r\n\r\n\r\n jsdjyhuwdhbcbuyshxbywhbbcy asjhd gdsbhj jdfghs sdjh fdjshcx quw ashk128973  4739 qowui9120o ' \
              '012-3  sioa asd\s df\n\r\n ijasd io18975 8293 adsj asdlk ajhsd lajkds haskj jk asjk dsajhk sadk jasjkh aksjd ' \
              'asd' \
              'ad' \
              'asd' \
              'asdasdasasdasdasdasdasdasdasdasdasdasdasdasdasdasdasasdqweasdasdasdasdasdasdasddasadsadsdasadsadsda' \
              'adsasdadsasdadsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsdsds' \
              'eqweqweqweqweqweqweqweqweqweqweqw' \
              '12323232323232323' \
              '4532 to jest duzy przykladowy tekst im wiekszy tym bardzie kompresja huffmana ma sens'

t1 = _generate_tree_from_occurrences(_get_occurrences(sample_text))
t2 = _generate_tree_from_characters_codes(_generate_tree_from_occurrences(_get_occurrences(sample_text)).get_characters_codes())
print(t1.get_characters_codes() == t2.get_characters_codes())
p = 'C:/Users/IChri/Downloads/lollol.bin'
compress(sample_text, p)
print(sample_text == decompress(p))
p2 = 'C:/Users/IChri/Downloads/lollol2.bin'
f = open(p2, 'w')
f.write(sample_text)
f.close()
f = open(p2, 'r')
