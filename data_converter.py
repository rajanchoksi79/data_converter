import sys

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
BLUE = "\033[34m"
RESET = "\033[0m"

user_input: str = input("\n- Enter an interger number here: ")
data_format: str = input (f"- Enter data format flag ({YELLOW}b{RESET} for binary, {YELLOW}h{RESET} for hex, {YELLOW}o{RESET} for octal and {YELLOW}a{RESET} for all): ")

def convert_str_to_number(input_value: str) -> int:
    try: 
        return int(input_value)
    except ValueError:
        print(f"\n{RED}~> The given number is not a integer number, please enter a valid integer number{RESET}\n")
        sys.exit(1)

input_number: int = convert_str_to_number(user_input)

def convert_integer_to_binary(input_value: int):
    binary_number = bin(input_value)
    print(f"~> The binary number of given interger is: {CYAN}{binary_number}{RESET}")    

def convert_integer_to_hex(input_value: int):
    hex_number = hex(input_value)
    print(f"~> The hex number of given interger is: {CYAN}{hex_number}{RESET}")

def convert_integer_to_octal(input_value: int):
    octal_number = oct(input_value)
    print(f"~> The octal number of given interger is: {CYAN}{octal_number}{RESET}")

# just for space need to display result
print("")

if (data_format == "b"):
    convert_integer_to_binary(input_number)
elif (data_format == "h"):
    convert_integer_to_hex(input_number)
elif (data_format == "o"):    
    convert_integer_to_octal(input_number)
elif (data_format == "a"):
    convert_integer_to_binary(input_number)
    convert_integer_to_hex(input_number)
    convert_integer_to_octal(input_number)
else: 
    print(f"{RED}~> Please enter correct data format flag{RESET}")

# just for space need after displaying result
print("")