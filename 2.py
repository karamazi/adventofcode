from collections import Counter


def get_ids():
    with open("2_input.txt") as f:
        for line in f:
            yield line


def get_checksum():
    has_pair_count = 0
    has_triple_count = 0
    for obj_id in get_ids():
        occurrences = set(Counter(obj_id).values())
        has_pair_count += int(2 in occurrences)
        has_triple_count += int(3 in occurrences)
    return has_pair_count * has_triple_count


def get_one_offs():
    ids_list = list(get_ids())
    for visited_ind, obj_id_1 in enumerate(ids_list):
        n = len(obj_id_1)
        for obj_id_2 in ids_list[visited_ind:]:
            indexes_with_difference = [i for i in range(n) if obj_id_1[i] != obj_id_2[i]]
            if len(indexes_with_difference) == 1:
                i = indexes_with_difference[0]
                return obj_id_1[0:i] + obj_id_1[i+1:]


print(get_checksum())
print(get_one_offs())
