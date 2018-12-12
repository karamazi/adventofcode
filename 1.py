

def get_list():
	items = []
	with open("1_input.txt") as f:
		for line in f.readlines():
			is_plus = line[0] == '+'
			value = int(line[1:])
			value *= 1 if is_plus else -1
			items.append(value)
	return items


def get_first_repeated_frequency():
	found = False
	ind = 0
	changes = get_list()
	unique_frequencies = set()
	frequency = 0
	while not found:
		frequency += changes[ind]
		found = frequency in unique_frequencies
		unique_frequencies.add(frequency)
		ind = (ind+1)%len(changes)
	return frequency
	

print('part1', sum(get_list()))
print('part2', get_first_repeated_frequency())

