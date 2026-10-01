from typing import Callable
import re
def is_number(text:str)->bool:
    try:
        float(text)
        return True
    except ValueError:
        return False
def generator_numbers(text:str):
    # for word in text.split(' '):    
    #     if is_number(word):
    #         yield float(word)
    regular_patern = r" \d+.\d+ "
    number_list = re.findall(regular_patern,text)
    for number in number_list:
        yield float(number)


def sum_profit(text:str,func:Callable[[str],None]):
    total = 0
    for num in func(text):
        total += num
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
