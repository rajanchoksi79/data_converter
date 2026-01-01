import sys
from colors import RED, RESET


# typecasting input string to integer, if error then throw it and terminate program
def casting_str_to_number(input_value: str) -> int:
    try: 
        return int(input_value)
    except ValueError:
        print(f"\n{RED}~> The given number is not a integer number, please enter a valid integer number{RESET}\n")
        sys.exit(1)