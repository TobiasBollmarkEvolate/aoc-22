def unique_list(data: list):
    return len(data) == len(set(data))


def unique_string(string: str, count: int = 4) -> int:
    chars: list[str] = list(string[:count])
    for char in string[count:]:
        chars.append(char)
        if unique_list(chars):
            return count
        count += 1
        chars.pop(0)


def main(file_name: str) -> tuple[int, int]:
    with open(file_name) as f:
        line = f.readline()
    return unique_string(line, 4), unique_string(line, 14)  # Yes I'm looping the string twice here, lazy ;)


if __name__ == '__main__':
    print(main('input.txt'))
