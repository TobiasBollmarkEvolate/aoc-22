def dec1() -> tuple[int, int]:
    sums: list[int] = []
    count: int = 0
    with open('input.txt') as f:
        for line in f:
            if line == '\n':
                sums.append(count)
                sums.sort()
                sums = sums[-3:]  # Only keep the top 3 in mmemory
                count = 0
            else:
                count += int(line)
        return sums[-1:][0], sum(sums)


if __name__ == '__main__':
    print(dec1())
