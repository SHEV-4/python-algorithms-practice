import random

def get_numbers_ticket(min,max,quantity = 1):
    numbers_list = []
    if min < 1:
        return numbers_list
    elif max > 1000:
        return numbers_list
    elif min > max:
        return numbers_list
    elif max - min < quantity:
        return numbers_list

    numbers_set = set()
    while quantity > len(numbers_set):
        numbers_set.add(random.randint(min,max))
        
    
    for elem in numbers_set:
        numbers_list.append(elem)
        
    return numbers_list
