#remove the smallest integer without altering the order of the remaining list
def remove_smallest(numbers):
    raise NotImplementedError("TODO: remove_smallest")
    out = min(numbers)
    for i in numbers :
        if i == out :
            numbers.remove(i)
            break
    return numbers

a = [1,2,3,1,1]
print(remove_smallest(a))

# test.describe("remove_smallest")

# test.it("works for the examples")
# test.assert_equals(remove_smallest([1, 2, 3, 4, 5]), [2, 3, 4, 5], "Wrong result for [1, 2, 3, 4, 5]")
# test.assert_equals(remove_smallest([5, 3, 2, 1, 4]), [5, 3, 2, 4], "Wrong result for [5, 3, 2, 1, 4]")
# test.assert_equals(remove_smallest([1, 2, 3, 1, 1]), [2, 3, 1, 1], "Wrong result for [1, 2, 3, 1, 1]")
# test.assert_equals(remove_smallest([]), [], "Wrong result for []")

# from numpy.random import randint

# def randlist():
#     return list(randint(400, size=randint(1, 10)))


# test.it("returns [] if list has only one element")
# for i in range(10):
#     x = randint(1, 400)
#     test.assert_equals(remove_smallest([x]), [], "Wrong result for [{}]".format(x))
    
# test.it("returns a list that misses only one element")
# for i in range(10):
#     arr = randlist()
#     test.assert_equals(len(remove_smallest(arr[:])), len(arr) - 1, "Wrong sized result for {}".format(arr))
