def find_max_odd(data):
    """
    Given the list of numbers, Find the maximum odd number in the list
    args:
        data: list of numbers
    returns: maximum odd number in the list
    """
    maxo = data[0]
    for i in data:
        if i % 2 == 1:
            if i>maxo:
                maxo = i
    return maxo
print(find_max_odd([2,3,8,9,4,6,1]))