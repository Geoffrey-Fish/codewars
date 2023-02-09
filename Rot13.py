#SOLVED, realtive easy with google fu
'''ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
'''
import string

a = list(string.ascii_lowercase*2)
b = list(string.ascii_uppercase*2)
c = list(string.punctuation)

def rot13(message) :
    output = ""
    for i in message:
        if i in a :
            j = a.index(i) + 13
            output += a[j]
        elif i in b :
            j = b.index(i) + 13
            output += b[j]
        elif i in c :
            output += i
        else :
            output += i
    return output


test.assert_equals(rot13("test"),"grfg")
test.assert_equals(rot13("Test"),"Grfg")