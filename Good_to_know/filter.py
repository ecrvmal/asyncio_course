my_list = [1, 0, 2, 0, 3, 0 ]

filtered_list = list(filter( lambda x : bool(x) , my_list))

print(filtered_list)