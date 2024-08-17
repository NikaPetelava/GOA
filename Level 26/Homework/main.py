def function(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num // 2)
        else:
            new_list.append(num * 2)
    return new_list

result = function([5,10,3,5])             
print(result)

