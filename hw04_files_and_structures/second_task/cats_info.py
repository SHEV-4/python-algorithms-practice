def get_cats_info(path:str) -> list:
    try:
        with open(path,"r",encoding="utf-8")as file:
            data = []
            for element in file.readlines():
                id = element.strip().split(',')[0]
                name = element.strip().split(',')[1]
                age = element.strip().split(',')[2]

                data.append({"id":id,
                             "name":name,
                             "age":age})
    except FileNotFoundError:
        return data
    except UnicodeDecodeError:
        return data
    return data