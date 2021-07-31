def find_max(a):
    max_number = a[0]
    for test_number in a:
        if test_number >= max_number:
            max_number = test_number
    return max_number
print(find_max([1, 2, 4, 5]) )
print(find_max([5, 2, 7, 1, 6]) )

print("-------------------------------------------------------------------------------------------------------")

def find_position(a,b):
    position_number = 0
    check_number = -1
    for target_number in a:
        if target_number == b:
            return position_number
            position_number+=1
            check_number += 1
            break
        elif target_number != b:
            if position_number+1 < len(a):
                position_number+=1
            elif position_number+1 == len(a):
                return check_number


print(find_position([5, 2, 7, 1, 6], 5))
print(find_position([5, 2, 7, 1, 6], 7))
print(find_position([5, 2, 7, 7, 7, 1, 6], 7))
print(find_position([5, 2, 7, 1, 6], 8))