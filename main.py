def dec1_part1(lines: list[str]) -> int:
    highest: int = 0
    count: int = 0
    for line in lines:
        if not line:
            if count > highest:
                highest = count
            count = 0
        else:
            count += int(line)
    return highest


def dec1_part2(lines: list[str]) -> int:
    sums: list[int] = []
    count: int = 0
    for line in lines:
        if not line:
            sums.append(count)
            count = 0
        else:
            count += int(line)
    sums.sort()
    return sum(sums[-3:])


if __name__ == '__main__':
    with open('input.txt') as f:
        file_lines: list[str] = f.read().splitlines()
    result1: int = dec1_part1(file_lines)
    print(result1)
    result2: int = dec1_part2(file_lines)
    print(result2)
