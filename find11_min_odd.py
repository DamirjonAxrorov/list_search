def find_min_odd(data):
    """
    Given the list of numbers, Find the minimum odd number in the list
    args:
        data: list of numbers
    returns: minimum odd number in the list
    """
    minm = data[0]
    for i in data:
        if i % 2 == 1:
            if i>minm:
                minm = i
    return minm
print(find_min_odd([2,3,8,9,4,6,1]))
