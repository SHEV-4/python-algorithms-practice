import re 

def normalize_phone(phone_number):
    phone_number= phone_number.strip()
    pattern = r"[ \- \\t \\n \\r \( \)]"
    replacement = ""
    formatted_phone = re.sub(pattern,replacement,phone_number)
    if formatted_phone[:3] != '+38' and formatted_phone[:2] !='38':
        return "+38"+ formatted_phone
    elif phone_number[0] != '+':
        return "+" + formatted_phone
    else: 
        return formatted_phone 
