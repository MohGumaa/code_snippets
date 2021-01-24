# Function return list as string
def list_to_string(values):
    string_value = ''
    for value in values:
        if value != values[-1]:
            string_value +=  value + ', '
        else:
            string_value += 'and ' + value

    return string_value


spam = ['apples', 'bananas', 'tofu', 'cats']

print(list_to_string(spam))
