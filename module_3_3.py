def print_params(a=1, b='String', c=True):
    print(a, b, c)


values_list = ['Tucker', 45.6, False]
values_dict = {'a': 12, 'b': 'Serbia', 'c': False}
values_list_2 = [17.2, 'Bread']

print_params()
print_params(a='KK', b=25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
