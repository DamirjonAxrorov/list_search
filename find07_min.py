def find_min(data):
    """
    Given the list of numbers, return the minimum number in the list
    args:
        data: list of numbers
    returns: minimum number in the list
    """
    minm = data[0]
    for i in data:
        if i<minm:
            minm = i
    return minm
print(find_min([2,3,8,9,4,-6,1]))