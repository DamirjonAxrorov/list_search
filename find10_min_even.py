def find_min_even(data):
    """
    Given the list of numbers, Find the minimum even number in the list
    args:
        data: list of numbers
    returns: minimum even number in the list
    """
    minm = data[0]
    for i in data:
        if i % 2 == 0:
            if i<minm:
                minm = i
    return minm
print(find_min_even([2,3,8,9,4,6,1]))