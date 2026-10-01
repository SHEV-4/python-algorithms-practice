from collections import Counter
import sys
from datetime import datetime
def load_logs(file_path:str)->list:
    try:
        with open(file_path,"r",encoding="utf-8") as log_file:
            return [log.strip() for log in log_file.readlines()]
    except FileNotFoundError:
        []

def parse_log_line(line:str)->dict:
    logs = {}
    words = line.split(" ")
    logs["date"] = words[0]
    logs["time"] = words[1]
    logs["level"] = words[2]
    logs["massage"] = " ".join(words[3:])
    return logs

def count_logs_by_level(logs: list) -> dict:
    logs_count = []
    for log in logs:
        logs_count.append(parse_log_line(log)["level"])
    return Counter(logs_count)

def filter_logs_by_level(logs: list, level: str) -> list:
    try:
        logs_parted = list(filter(lambda element: element.split(" ")[2] == level,logs))
        return logs_parted
    except ValueError:
        return []

def display_log_counts(counts: dict):
    print(f'{"Рівень логування | Кількість"}')
    print("-----------------|----------")
    for key,value in counts.items():
        print(f'{key:<17}| {value:<15}')

def write_logs(info:str):
    try:
        with open("log.txt",'a',encoding="utf-8")as file:
            file.write(info)
    except FileNotFoundError:
            print("Not Found log file")

def main():
    try:
        file_path = sys.argv[1]
        logs = load_logs(file_path)
        counts_log = count_logs_by_level(logs)    
        display_log_counts(counts_log)
        if len(sys.argv)>2:
            print("\n".join(filter_logs_by_level(logs,sys.argv[2])))
    except IndexError:
        write_logs(f'{datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")} ERROR Don`t have argumants\n')
        print("Don`t have argumants")
        
    

if __name__ == "__main__":
    main()