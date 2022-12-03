import itertools


def get_score(char: str) -> int:
    ascii_code = ord(char)
    return ascii_code - 96 if ascii_code > 96 else ascii_code - 38


def split_middle(data: str) -> tuple[str, str]:
    middle = int(len(data) / 2)
    return data[:middle], data[middle:]


def find_common_char(string1: str, string2: str) -> str:
    for char in string1:
        if char in string2:
            return char


def find_common_char_iterativly(strings: list[str], chars: list[str] = None):
    if chars is None:
        chars = strings.pop(0)
    for char in chars:
        if char in strings[0]:
            strings.pop(0)
            if not strings:
                return char
            char = find_common_char_iterativly(strings, [char])
            if char:
                return char
    return False


def main(file_name: str) -> tuple[int, int]:
    score1: int = 0
    score2: int = 0
    with open(file_name) as f:
        for line in f:
            compartment1, compartment2 = split_middle(line.strip('\n'))
            score1 += get_score(find_common_char_iterativly([compartment1, compartment2]))
    with open(file_name) as f:
        for line1, line2, line3 in itertools.zip_longest(*[f] * 3):
            score2 += get_score(find_common_char_iterativly([line1, line2, line3]))
    return score1, score2


if __name__ == '__main__':
    print(main('input.txt'))
