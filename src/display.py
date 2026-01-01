from converter import convert_integer_to_binary, convert_integer_to_hex, convert_integer_to_octal, convert_integer_to_UTF_8
from colors import RED, RESET


# displaying result based on user choice of data format 
def display_result(data_format: str, input_number: int):
    # just for space need to display result
    print("")

    if (data_format == "b"):
        convert_integer_to_binary(input_number)
    elif (data_format == "h"):
        convert_integer_to_hex(input_number)
    elif (data_format == "o"):    
        convert_integer_to_octal(input_number)
    elif (data_format == "u"):
        convert_integer_to_UTF_8(input_number)    
    elif (data_format == "a"):
        convert_integer_to_binary(input_number)
        convert_integer_to_hex(input_number)
        convert_integer_to_octal(input_number)
        convert_integer_to_UTF_8(input_number)
    else: 
        print(f"{RED}~> Please enter correct data format flag{RESET}")

    # just for space need after displaying result
    print("")
