#SOLVED
'''Given: an array containing hashes of names

Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.

Example:

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'''
from operator import itemgetter
def namelist(names):
    #your code here
    getter = itemgetter('name')
    lng = len(names)
    shorter = names[:lng-2]

    if lng == 0 :
        return ''
    elif lng == 1 :
        return getter(names[0])
    else :
        c = ''
        
        for item in shorter:
            c += getter(item)
            c += ', '
        c = c + getter(names[-2]) + ' & ' + getter (names[-1])
        return c

        
        

print(namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])) == 'Bart, Lisa, Maggie, Homer & Marge',
"Must work with many names"