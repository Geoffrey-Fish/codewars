#SOLVED it was a fun ride,was too tired the evening before. now,it was easy peasy
'''Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

a -> 1
e -> 2
i -> 3
o -> 4
u -> 5

For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

For example, decode("h3 th2r2") would return "hi there".

For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.'''
import re
def encode(st):
    a = re.sub("a","1",st)
    e = re.sub("e","2",a)
    i = re.sub("i","3",e)
    o = re.sub("o","4",i)
    u = re.sub("u","5",o)
    return u
def decode(st):
    a = re.sub("1","a",st)
    e = re.sub("2","e",a)
    i = re.sub("3","i",e)
    o = re.sub("4","o",i)
    u = re.sub("5","u",o)
    return u

print(decode("Th3s 3s 1n 2nc4d3ng t2st."))
print(encode("this is an encoding test."))

(encode("this is a TestString for use."))
(encode("this is a TestString for use."))


'''test.assert_equals(encode('hello'), 'h2ll4')
test.assert_equals(encode('How are you today?'), 'H4w 1r2 y45 t4d1y?')
test.assert_equals(eecode('This is an encoding test.'), 'Th3s 3s 1n 2nc4d3ng t2st.')
test.assert_equals(decode('h2ll4'), 'hello')'''

