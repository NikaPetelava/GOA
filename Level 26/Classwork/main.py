def even_number(numbers):
    empty_list = []
    for number in numbers:
        if number % 2 == 0:
            empty_list.append(number)
    return empty_list

numbers_list = [1,2,3,4,5,6]
print(numbers_list)
print(even_number(numbers_list))