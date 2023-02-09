#bus stop. array of integers. first number passengers go in, second passengers go out. 
# how many are left after the last bus stop?
def number(bus_stops):
    # Good Luck!
    a = 0
    b = 0
    for i in bus_stops:
        a += i[0]
        b += i[1]
    return a-b







a = [[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]
print(number(a))
#     import codewars_test as test
# from solution import number

# @test.describe("Fixed Tests")
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():
#         test.assert_equals(number([[10,0],[3,5],[5,8]]),5)
#         test.assert_equals(number([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]),17)
#         test.assert_equals(number([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]),21)
