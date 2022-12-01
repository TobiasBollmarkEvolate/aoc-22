def dec1_part1(data):
    highest = 0
    count = 0
    for item in data:
        if not item:
            if count > highest:
                highest = count
            count = 0
        else:
            count += int(item)
    return highest


def dec1_part2(data):
    sums = []
    count = 0
    for item in data:
        if not item:
            sums.append(count)
            count = 0
        else:
            count += int(item)
    sums.sort()
    return sum(sums[-3:])


if __name__ == '__main__':
    # 1
    with open('input.txt') as f:
        lines = f.read().splitlines()
    result1 = dec1_part1(lines)
    print(result1)
    result2 = dec1_part2(lines)
    print(result2)

    # 2

