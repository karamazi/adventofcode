import string


def will_react(u1: str, u2: str) -> bool:
    return abs(ord(u1) - ord(u2)) == 32


# TFW no linked list in python
def process_polymer(polymer: str) -> str:
    try:
        i = 0
        while i < len(polymer):
            u1 = polymer[i]
            u2 = polymer[i+1]
            if will_react(u1, u2):
                polymer = polymer[:i] + polymer[i+2:]
                i = max(i-1, 0)
            else:
                i += 1
    except IndexError:
        pass
    finally:
        return polymer


def part_one():
    with open('5_input.txt') as f:
        polymer = f.readline().strip()
    # polymer = 'dabAcCaCBAcCcaDA'
    processed = process_polymer(polymer)
    print(len(processed))


def part_two():
    with open('5_input.txt') as f:
        polymer = f.readline().strip()
    polarized_pairs = zip(string.ascii_lowercase, string.ascii_uppercase)
    lengths = []
    for u1, u2 in polarized_pairs:
        new_polymer = process_polymer(polymer.replace(u1, '').replace(u2, ''))
        lengths.append(len(new_polymer))
    print(min(lengths))


part_one()
part_two()

