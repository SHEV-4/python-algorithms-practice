from structure import get_stucture
import sys

def main():
    if len(sys.argv) > 1:
        structure = get_stucture(sys.argv[1])
        for element in structure:
            print(element)
    else:
        print("Ведіть аргумент")

if __name__ == "__main__":
    main()