import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T


cat
mat
pat
bat
'''


sentence = 'Start a sentence and then bring it to an end'

# p = re.compile(r'abc')
# p = re.compile(r'coreyms.com')
# p = re.compile(r'')
# p = re.compile(r'\d\d\d.\d\d\d.\d\d\d'))

# Match phone saparete with - or .
# p = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d')

# Match start with 800 or 900
# p = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d')

# match btw a to z
# p = re.compile(r'[a-z]')
# p = re.compile(r'[a-zA-Z]')

# need evey thing extecpt bat
# p = re.compile(r'[^b]at')

# p = re.compile(r'\d{3}.\d{3}.\d{4}')

# p = re.compile(r'Mr\.?\s[A-Z]\w*')
# p = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

# ms = p.finditer(text_to_search)

# It return first match group or list of tuple match list group
# p = re.compile(r'\d{3}.\d{3}.\d{4}')
# ms = p.findall(text_to_search)

# for m in ms:
    # Here will return span=(1,4) found element in position
    # print(m)

# print(text_to_search[1:4])


# *********** Read from file and match **********#
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d')

# with open('data.txt') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print(match)

# Here to ignorecase
# pattern = re.compile(r'start', re.I)

# matches = pattern.search(sentence)

# print(matches)



