def find_uniq(arr):
    sorted_arr = sorted(arr)
    if sorted_arr[0] == sorted_arr[1]:
        n = sorted_arr[-1]
    else:
        n = sorted_arr[0]
    
    return n   # n: unique integer in the array
    

test.describe("Basic Tests")
test.assert_equals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
test.assert_equals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
test.assert_equals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)