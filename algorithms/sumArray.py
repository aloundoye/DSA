def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])

sumarr = sum([2,4,6,6,3,6,3,63,6765,35,63,763,33,76,63])

print(sumarr)