my_dict ={'Олег': 1975, 'не Олег': 1999, 'Олежа': 2002}
print('Dict:', my_dict)
print('Existing value:', my_dict['не Олег'])
print('Not existing value: ', my_dict.get('Олежка'))
my_dict.update({'Валера': 1998,
                'Вася': 1700})
removed_value = my_dict.pop('Валера')
print("Deleted value 'Валера':", removed_value)
print("Modified my_dict:", my_dict)


my_set = {1, 2, "apple", "apple", 3.14}
print( my_set)
my_set.update({5, "banana"})
my_set.discard(2)
print('Modified set:', my_set)

