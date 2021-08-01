#! python3

import sys
from random import choice

details = '''
    This program generates story randomly
    version 0.0.1
    Type --version to display version info

'''

def version():
    if sys.argv[-1] == '--version':
        d = details.splitlines(3)
        return d[2].strip()


stories = dict(
story_1 = 'A man was born poor but later in life he became ' + 'rich'.upper(),
story_2 = 'A woman was slaped because she dressed unusual',
story_3 = 'This is same story_1',
story_4 = 'This is combination of story_1 and _2'
)

st_keys = []

def storys():
    if version():
        print(version())

    for k, v in stories.items():
        st_keys.append(k)
        choose = choice(st_keys)
    print(f'{choose}: {stories[choose]}')



   
    
    
    





if __name__ == '__main__':
    storys()