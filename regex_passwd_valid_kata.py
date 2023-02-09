import re
''' Write a regex that will validate a passwort to match the following criteria:
    At least six chars
    a lowercase letter
    an uppercase letter
    a number.
    Passwords will only be alphanumeric'''
#must be inside:
regex ="ghdfj32A"
if re.findall("[a-z]",regex) and re.findall("[A-Z]",regex) and re.findall("[0-9]",regex) and re.findall("......+",regex) :
        print("True")
else :
    print("False")

'''    from re import search
test.describe("Basic tests")
test.assert_equals(bool(search(regex, 'fjd3IR9')), True)
test.assert_equals(bool(search(regex, 'ghdfj32')), False)
test.assert_equals(bool(search(regex, 'DSJKHD23')), False)
test.assert_equals(bool(search(regex, 'dsF43')), False)
test.assert_equals(bool(search(regex, '4fdg5Fj3')), True)
test.assert_equals(bool(search(regex, 'DHSJdhjsU')), False)
test.assert_equals(bool(search(regex, 'fjd3IR9.;')), False)
test.assert_equals(bool(search(regex, 'fjd3  IR9')), False)
test.assert_equals(bool(search(regex, 'djI38D55')), True)
test.assert_equals(bool(search(regex, 'a2.d412')), False)
test.assert_equals(bool(search(regex, 'JHD5FJ53')), False)
test.assert_equals(bool(search(regex, '!fdjn345')), False)
test.assert_equals(bool(search(regex, 'jfkdfj3j')), False)
test.assert_equals(bool(search(regex, '123')), False)
test.assert_equals(bool(search(regex, 'abc')), False)
test.assert_equals(bool(search(regex, '123abcABC')), True)
test.assert_equals(bool(search(regex, 'ABC123abc')), True)
test.assert_equals(bool(search(regex, 'Password123')), True
'''
