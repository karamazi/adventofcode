def get_ids():
	with open("2_input.txt") as f:
		return f.readlines()
		
	
from collections import Counter


ids_list = get_ids()

has_pair = 0
has_triple = 0
for obj_id in get_ids():
	c = Counter(obj_id)
	occurences = set(c.values())
	has_pair += int(2 in occurences)
	has_triple += int(3 in occurences)
print(has_pair * has_triple)



def get_one_offs():
	for visited, obj_id_1 in enumerate(ids_list):
		n = len(obj_id_1)
		for obj_id_2 in ids_list[visited:]:
			diff_inds = [i for i in range(n) if obj_id_1[i] != obj_id_2[i]]
			diff = sum(1 for _ in diff_inds)
			if diff == 1:
				i = diff_inds[0]
				return obj_id_1[0:i] + obj_id_1[i+1:]
				
		
print(get_one_offs())