def check_row(row, position):
    check_tree = row[position]
    left = True
    for i, tree in enumerate(row):
        if tree >= check_tree:
            if i < position:
                left = False  # TODO: optimize, we don't need to check more on the left side in this row
            elif i > position:
                return False
            elif left:
                # Got to i == position and left is still True, the tree is visible form left, so we don't need to check
                # from the other side
                return True
    return True


def visible_from_any_side(matrix: list[list[int]]):
    visible: int = 0
    visible += len(matrix[0]) * 2  # Add outer rows
    visible += len(matrix) * 2  # Add outer columns
    visible -= 4  # Don't count the corners twice
    for i, line in enumerate(matrix[1:-1]):  # removed first and last rows
        for j in range(1, len(line) - 1):
            # Check this tree if its NOT visiable from:
            # right and left
            if check_row(line, j):  # Right and left
                visible += 1
            elif check_row([x[j] for x in matrix], i + 1):  # Up and Down, +1 because we removed the first row
                visible += 1

    return visible


def main(file_name: str) -> tuple[int, int]:
    tree_matrix: list[list[int]] = []
    with open(file_name) as f:
        for line in f:
            tree_matrix.append([int(x) for x in list(line.strip())])
    return visible_from_any_side(tree_matrix), 0


if __name__ == '__main__':
    print(main('input.txt'))
