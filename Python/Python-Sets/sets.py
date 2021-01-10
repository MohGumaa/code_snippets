
employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']

gym_members = ['April', 'John', 'Corey']

developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

result = set(gym_members).intersection(developers)

result = set(employees).difference(gym_members, developers)

# print(result)

# Set is very useful for test membership test
if 'Corey' in set(developers):
    print('Found!')

# O(n) for list [It has to scan whole list]
# O(1) for a set [Here only one time to find value]


# Examples of set methods
s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

s4 = s1.intersection(s2)
s4 = s1.intersection(s2, s3)

s4 = s1.difference(s2, s3)
s4 = s2.difference(s1, s3)

# Here will give difference in both
s4 = s2.symmetric_difference(s1)

s4 = s2.union(s1, s3)
s4 = s2.union(s3)
# print(s4)

# Here we cast list to remove duplicate and cast back
l1= [1, 2, 3, 1, 2, 3]
l2 = list(set(l1))

# print(l2)
