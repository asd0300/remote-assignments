# def count(input):
#     finalDic= {}
#     while(len(input)!=0):
#         if (input[0] in finalDic):
#             finalDic[input[0]] +=1
#             input.remove(str(input[0]))
#         elif (input[0] not in finalDic):
#             finalDic[input[0]] =1            
#             input.remove(str(input[0]))
#     return finalDic
 
# input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
# print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}
# print("-----------------------------------------------------------------------------------")
def group_by_key(input):
 # your code here
    finalDic= {}
    while(len(input)!=0):   
        tempDic =input[0].values()
        if (list(tempDic)[0] in finalDic): 
            finalDic[(str(list(tempDic)[0]))] +=list(tempDic)[1]  
            input.remove(input[0])
        elif (list(tempDic)[0] not in finalDic):
            finalDic[list(tempDic)[0]] =list(tempDic)[1]          
            input.remove(input[0])
    return finalDic
input2 = [
 {'key': 'a', 'value': 3},
 {'key': 'b', 'value': 1},
 {'key': 'c', 'value': 2},
 {'key': 'a', 'value': 3},
 {'key': 'c', 'value': 5}
]
print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}