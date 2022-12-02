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


def dec2(file_name: str) -> tuple[int, int]:
    player_points = {
        "rock": 1,
        "paper": 2,
        "scissors": 3
    }
    hand = {
        "A": "rock",
        "B": "paper",
        "C": "scissors",
        "X": "rock",
        "Y": "paper",
        "Z": "scissors"
    }
    strat = {
        "X": "loose",
        "Y": "draw",
        "Z": "win"
    }
    beat = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }
    loose = {v: k for k, v in beat.items()}  # Creates a reversed "beat"

    def beats(h1, h2):
        if h1 == h2:
            return 3
        if beat[h1] == h2:
            return 0
        return 6

    def points_part2(p, s):
        p = hand[p]
        s = strat[s]
        if s == "draw":
            return 3 + player_points[p]
        elif s == "win":
            return 6 + player_points[loose[p]]
        return 0 + player_points[beat[p]]  # loose

    score_part1: int = 0
    score_part2: int = 0
    with open(file_name) as f:
        for line in f:
            a, x = line.split()
            score_part1 += beats(hand[a], hand[x]) + player_points[hand[x]]
            score_part2 += points_part2(a, x)
    return score_part1, score_part2


if __name__ == '__main__':
    print(dec1('input1.txt'))
    print(dec2('input2.txt'))
