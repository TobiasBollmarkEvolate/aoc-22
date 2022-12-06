def unique_list(data: list):
    print(data)
    return len(data) == len(set(data))


def main(file_name: str) -> tuple[int, str]:
    with open(file_name) as f:
        instructions = []
        counter = 0
        while True:
            char = f.read(1)
            if not char:
                break
            counter += 1
            instructions.append(char)
            if len(instructions) < 4:
                continue
            if unique_list(instructions):
                break
            instructions.pop(0)
    return counter, ""


if __name__ == '__main__':
    print(main('input.txt'))
