symbols_list = ['a', 'b', 'c', 'c', 'a']


def return_match():
    loop = True
    while loop:
        for index, element in enumerate(symbols_list):
            item = element
            next_item = symbols_list[(index+1) % len(symbols_list)]

            if item == next_item:
                print(item)
                return item

        loop = False


return_match()
