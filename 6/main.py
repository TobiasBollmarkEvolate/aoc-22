def unique_list(data: list):
    return len(data) == len(set(data))


def unique_string(string: str, no: int = 4):
    counter: int = 0
    chars: list[str] = []
    for char in string:
        counter += 1
        chars.append(char)
        if len(chars) < no:
            continue
        if unique_list(chars):
            break
        chars.pop(0)
    return counter


def main(file_name: str) -> tuple[int, int]:
    with open(file_name) as f:
        line = f.readline()
    return unique_string(line, 4), unique_string(line, 14)


if __name__ == '__main__':
    print(main('input.txt'))
