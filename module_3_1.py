calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    tuple_new = (len(string), string.upper(), string.lower())
    count_calls()
    print(tuple_new)


def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() in i.lower():
            return True
        else:
            return False


string_info('Baratheon')
print(is_contains('Urban', ['UrBaN', 'banner', 'banana']))
print(is_contains('gorillaz', ['grizzly', 'gora']))
print(calls)
