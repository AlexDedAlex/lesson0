tuple_immutable_var = 24, 63, 'Alex', False
print(tuple_immutable_var)
tuple_immutable_var[2] = 'Boris'
print(tuple_immutable_var)
# TypeError: 'tuple' object does not support item assignment

mutable_list = [24, 63, 'Alex', False]
print(mutable_list)
mutable_list[2] = 'Boris'
mutable_list.append('Anna')
print(mutable_list)