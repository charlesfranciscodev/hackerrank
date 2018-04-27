from collections import OrderedDict

dictionary = OrderedDict()

nb_items = int(input())
for _ in range(nb_items):
    item = input().split()
    item_name = ' '.join(item[0:-1])
    item_price = int(item[-1])
    dictionary[item_name] = dictionary.get(item_name, 0) + item_price

for key, value in dictionary.items():
    print(key, value)
