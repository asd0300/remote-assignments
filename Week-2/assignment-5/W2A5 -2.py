def binary_search_first(a,b):
    tempNumber = 0
    for i in range(0,len(a)):
        for j in range(i+1,len(a)):
            if (a[i] > a[j]):
                    tempNumber = a[i]
                    a[i] = a[j]
                    a[j] = tempNumber    #get ascent order list
    firstIndex = 0
    smallDistance = 0
    position_number = 0     #choose the target number/ the first high index to target number
    if b < a[0]:
        firstIndex = 0
        return firstIndex
    elif b > a[len(a)-1]:
        firstIndex = len(a)-1
        return firstIndex
    elif a[len(a)-1]>= b >= a[0]:
        for list_number in a:
            if list_number == b:
                return position_number
                break                        #if target number exist in list
            elif list_number != b:
                if (list_number> b) and smallDistance ==0:
                    smallDistance = list_number-b
                    firstIndex = position_number
                if (list_number> b) and (list_number-b<smallDistance):
                    smallDistance = list_number-b
                    firstIndex = position_number
            position_number+=1
        return firstIndex  #else get the most small different absolute value, and higher than target num
    print(a, b)
    


print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2)) # should print 1 (the index of the target number ‘2’)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5)) # should print 2 (the index of the ‘first’ target number ‘5’ shows up)
print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 3)) # should print 2 (since it can’t find number 3,return the index of ‘the smallest number larger then 3', that is, the index of the ‘first’ number 5)