my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_index_list = []

for x in range(0, len(my_list), 2):
  even_index_list.append(my_list[x])

print(even_index_list)