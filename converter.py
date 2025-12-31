from colors import CYAN, RESET

# integer to binary converter function  
def convert_integer_to_binary(input_value: int):
    binary_number = bin(input_value)
    print(f"~> The binary number of given interger is: {CYAN}{binary_number}{RESET}")    


# integer to hex converter function  
def convert_integer_to_hex(input_value: int):
    hex_number = hex(input_value)
    print(f"~> The hex number of given interger is: {CYAN}{hex_number}{RESET}")


# integer to octal converter function  
def convert_integer_to_octal(input_value: int):
    octal_number = oct(input_value)
    print(f"~> The octal number of given interger is: {CYAN}{octal_number}{RESET}")

