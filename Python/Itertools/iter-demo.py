
import itertools


def get_state(person):
    return person['state']


people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

# with open('test.log') as f:
#     header = itertools.islice(f, 3)
#     for line in header:
#         print(line, end='')

person_group = itertools.groupby(people, get_state)

copy1, copy2 = itertools.tee(person_group)
# copies = itertools.tee(person_group, 2)

print(list(copy2),list(copy1))

# for key, group in person_group:
#     # print(key, group)
#     # print(key, len(list(group)))
#     print(key)
#     for person in group:
#         print(person)
    # print()
