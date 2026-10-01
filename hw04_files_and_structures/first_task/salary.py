def total_salary(path:str)->tuple:
    try:
        with open(path,"r",encoding="utf-8")as file:
            data = [element.strip().split(',') for element in file.readlines()]
            total_salary = sum(int(element[1]) for element in data)
            avg_salary = total_salary / len(data)
    except FileNotFoundError:
        return (0,0)
    except UnicodeDecodeError:
        return (0,0)
    return (total_salary, avg_salary)