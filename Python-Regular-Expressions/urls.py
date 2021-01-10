import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# Here give match of group 2 and 3
subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

matches = pattern.finditer(urls)

for match in matches:
    print(match.group(3))


# groups : for above we have 4 group

# group 0 this entire one and other are between () if not exist value return none
