def binary_search_position(a,b):
    lastArray = []
    count = 0
    tempNumber = 0
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if (a[i] > a[j]):
                    tempNumber = a[i]
                    a[i] = a[j]
                    a[j] = tempNumber

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

print(binary_search_position([5,4,3,2,1],1))
print(binary_search_position([1, 2, 5, 6, 7], 6))  
