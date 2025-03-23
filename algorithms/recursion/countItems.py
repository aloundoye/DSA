def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


sumarr = count([2,4,6,6,3,6,3,63,6765,35,63,763,33,76,63])

print(sumarr)