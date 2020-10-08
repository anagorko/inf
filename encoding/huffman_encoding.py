from typing import Dict


def encode(text: str, table: Dict[str, str]) -> str:
    """1 + 2 -> 3"""
    output = []
    for letter in text:
        output.append(table[letter])
    return ''.join(output)


def decode(text: str, tree: Dict) -> str:
    """3 + 4 -> 1"""
    i = iter(text)
    result = []
    t = tree
    while True:
        if isinstance(t, str):
            result.append(t)
            t = tree
        else:
            bit = next(i, None)
            if bit is None:
                break
            elif bit == "0":
                t = t[0]
            elif bit == "1":
                t = t[1]
    return "".join(result)


def code_to_tree(code: Dict) -> dict:
    tree = dict()


    def str_to_tree_rec(value: str, key: str, drzewo: Dict):
        if len(drzewo) is 1:
            drzewo[value[0]] = key

        if drzewo.get(value[0], False) is not None:
            str_to_tree_rec(value[1:], key, drzewo[value[0]])
        else:
            drzewo[value[0]] = {}
            str_to_tree_rec(value[1:], key, drzewo[value[0]])

    



def main():
    text = 'abbabc'
    table = {'a': '10', 'b': '0', 'c': '11'}
    htree = {0: "b", 1: {0: "a", 1: "c"}}

    print(encode(text, table))
    print(decode(encode(text, table), htree))


if __name__ == '__main__':
    main()
