PLAYER_POINTS: dict[str, int] = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}
PLAY_HANDS: dict[str, str] = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}
PLAY_STRATS: dict[str, str] = {
    "X": "loose",
    "Y": "draw",
    "Z": "win"
}
BEAT: dict[str, str] = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
LOOSE: dict[str, str] = {v: k for k, v in BEAT.items()}  # Creates a reversed "beat"


def beats(h1: str, h2: str) -> int:
    if h1 == h2:
        return 3
    if BEAT[h1] == h2:
        return 0
    return 6


def calculate_strat(p: str, s: str) -> int:
    if s == "draw":
        return 3 + PLAYER_POINTS[p]
    elif s == "win":
        return 6 + PLAYER_POINTS[LOOSE[p]]
    return 0 + PLAYER_POINTS[BEAT[p]]  # loose


def main(file_name: str) -> tuple[int, int]:
    count1: int = 0
    count2: int = 0
    with open(file_name) as f:
        for line in f:
            char1, x = line.split()
            count1 += beats(
                PLAY_HANDS[char1],
                PLAY_HANDS[x]
            ) + PLAYER_POINTS[PLAY_HANDS[x]]
            count2 += calculate_strat(
                PLAY_HANDS[char1],
                PLAY_STRATS[x]
            )
    return count1, count2


if __name__ == '__main__':
    print(main('input.txt'))
