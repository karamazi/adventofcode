""" 20 overlapping:
#1 @ 1,2: 5x5
#2 @ 2,1: 3x3
#3 @ 0,0: 2x2
#4 @ 7,7: 1x1
"""


def parsed_lines():
    i = 0
    with open('3_input.txt') as f:
        for line in f:
            if not line.strip():
                break
            no, _, pos, size = line.split(' ')
            no = int(no[1:])
            x, y = tuple(map(int, pos[:-1].split(',')))
            w, h = tuple(map(int, size.split('x')))

            yield no, (x, y), (w, h)


def part_one():
    n = 1000
    # area = [[0]*n]*n # Each row is the same pointer!!!
    area = [[0] * n for _ in range(n)]
    for _, pos, size in parsed_lines():
        x, y = pos
        w, h = size
        for row in range(y, y+h):
            for col in range(x, x+w):
                area[row][col] += 1

    overlapped = sum(sum(1 for col in row if col > 1) for row in area)
    return overlapped


def overlaps(c1, c2):
    _, c1_top_left, c1_size = c1
    c1_bot_right = tuple(map(sum, zip(c1_top_left, c1_size)))
    _, c2_top_left, c2_size = c2
    c2_bot_right = tuple(map(sum, zip(c2_top_left, c2_size)))

    if c1_top_left[0] > c2_bot_right[0] or c2_top_left[0] > c1_bot_right[0]:
        return False

    if c1_top_left[1] > c2_bot_right[1] or c2_top_left[1] > c1_bot_right[1]:
        return False
    return True


def part_two():
    claims = list(parsed_lines())
    for i, c1 in enumerate(claims):
        overlapped = False
        for c2 in claims[i+1:]:
            overlapped = overlaps(c1, c2)
            if overlapped:
                break
        if not overlapped:
            return c1[0]
    return -1


print(part_one())
print(part_two())
