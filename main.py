def dec1(file_name: str) -> tuple[int, int]:
    sums: list[int] = []
    count: int = 0
    with open(file_name) as f:
        for line in f:
            if line == '\n':
                sums.append(count)
                sums.sort()
                sums = sums[-3:]  # Only keep the top 3 in memory
                count = 0
            else:
                count += int(line)
        return sums[-1:][0], sum(sums)


def dec2(file_name: str) -> int:
    player_points = {
        "X": 1,
        "Y": 2,
        "Z": 3
    }
    hand = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors"
    }
    beat = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    def beats(h1, h2):
        if h1 == h2:
            return 3
        if beat[h1] == h2:
            return 0
        return 6

    def points_part1(p1: str, p2: str):
        p1 = hand[p1]
        p2 = hand[p2]
        return beats(p1, p2)

    score_part1: int = 0
    with open(file_name) as f:
        for line in f:
            a, x = line.split()
            score_part1 += points_part1(a, x) + player_points[x]
    return score_part1


if __name__ == '__main__':
    print(dec1('input1.txt'))
    print(dec2('input2.txt'))
