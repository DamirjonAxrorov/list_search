def find_max_even(data):
    """
    Given the list of numbers, Find the maximum even number in the list
    args:
        data: list of numbers
    returns: maximum even number in the list
    """
    maks = data[0]
    for i in data:
        if i % 2 == 0:
            if i>maks:
                maks = i
    return maks
print(find_max_even([2,3,8,9,4,6,1]))