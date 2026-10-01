from colorama import Fore
from pathlib import Path

def get_stucture(path:str, num:int = 0):
    try:
        directory = Path(path)
        structure = []
        structure.append(f"{Fore.BLUE}{" "*num + directory.name}{Fore.RESET}")
        for path in directory.iterdir():
            if path.is_dir():
                
                structure.extend(get_stucture(path,num + 3))
            else:
                structure.append(f"{Fore.GREEN}{" "*(num+3) + path.name}{Fore.RESET}")
        return structure
    except FileNotFoundError:
        return structure



