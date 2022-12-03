def get_score(char: str) -> int:
    ascii_code: int = ord(char)
    return ascii_code - 96 if ascii_code > 96 else ascii_code - 38


def split_middle(data: str) -> list[str]: # don't support odd number of chars
    middle: int = int(len(data) / 2)
    return [data[:middle], data[middle:]]


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
    lines: list[str] = []
    line_counter: int = 0
    with open(file_name) as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip('\n')
            # Part 1
            score1 += get_score(
                find_common_char_iterativly(
                    split_middle(line)
                )
            )
            # Part 2
            lines.append(line)
            line_counter += 1
            if line_counter % 3 == 0:
                score2 += get_score(
                    find_common_char_iterativly(lines)
                )
                lines = []
    return score1, score2


if __name__ == '__main__':
    print(main('input.txt'))
