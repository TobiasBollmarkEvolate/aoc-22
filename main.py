from typing import TextIO


def dec1(f: TextIO) -> tuple[int, int]:
    sums: list[int] = []
    count: int = 0
    for line_number, line in enumerate(f):
        if line == '\n':
            sums.append(count)
            sums.sort()
            sums = sums[-3:]
            count = 0
        else:
            count += int(line)
    sums.sort()
    return sums[-1:][0], sum(sums)


if __name__ == '__main__':
    with open('input.txt') as fp:
        print(dec1(fp))
