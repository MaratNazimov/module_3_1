calls = 0
lis = []


def count_calls():
    print(calls)


def string_info(string):
    global calls
    calls += 1
    tuple_c = (len(string), string.upper(), string.lower())
    return tuple_c


def is_contains(string, list_to_search):
    global calls, lis
    calls += 1
    for i in list_to_search:
        lis = [i.lower()]
    if string.lower() in lis:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
