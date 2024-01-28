def find_max(data):
    """
    Given the list of numbers, return the maximum number in the list
    args:
        data: list of numbers
    returns: maximum number in the list
    """
    maks = data[0]
    for i in data:
        if i>maks:
            maks = i
    return maks
print(find_max([2,3,8,9,4,6,1]))