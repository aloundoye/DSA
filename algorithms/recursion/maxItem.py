def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max


sumarr = maxItem([2,4,6,6,3,6,3,63,6765,35,63,763,33,76,63,4352452, 6765])

print(sumarr)