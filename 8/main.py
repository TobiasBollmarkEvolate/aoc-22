def check_row(row: list[int], position: int) -> bool:
    check_tree: int = row[position]
    left: bool = True
    for i, tree in enumerate(row):
        if tree >= check_tree:
            if i < position:
                left = False  # TODO: optimize, we don't need to check more on the left side in this row
            elif i > position:
                return False
            elif left:
                return True
    return True


def view_distance(i: int, row: list[int]) -> int:
    distance = 0
    for tree in row:
        distance += 1
        if tree >= i:
            break
    return distance


def scenic_score_row(row: list[int], position: int) -> int:
    check_tree: int = row[position]
    left_view: list = row[:position]
    if len(left_view) > 1:
        left_view.reverse()
    left: int = view_distance(check_tree, left_view)
    if left == 0:
        return 0
    right: int = view_distance(check_tree, row[position + 1:])
    return left * right


def main(file_name: str) -> tuple[int, int]:
    matrix: list[list[int]] = []
    with open(file_name) as f:
        for line in f:
            matrix.append([int(x) for x in list(line.strip())])
    visible: int = (len(matrix[0]) * 2) + (len(matrix) * 2) - 4
    max_score: int = 0
    for i, line in enumerate(matrix[1:-1]):
        for j in range(1, len(line) - 1):
            col_to_row: list = [x[j] for x in matrix]
            if check_row(line, j) or check_row(col_to_row, i + 1):
                visible += 1
            score: int = scenic_score_row(line, j) * scenic_score_row(col_to_row, i + 1)
            if score > max_score:
                max_score = score
    return visible, max_score


if __name__ == '__main__':
    print(main('input.txt'))
