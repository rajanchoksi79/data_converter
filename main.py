from casting import casting_str_to_number
from display import display_result
from colors import YELLOW, RESET

def main():
    user_input: str = input("\n- Enter an interger number here: ")

    data_format: str = input (f"- Enter data format flag ({YELLOW}b{RESET} for binary, {YELLOW}h{RESET} for hex, {YELLOW}o{RESET} for octal and {YELLOW}a{RESET} for all): ")

    input_number: int = casting_str_to_number(user_input)

    display_result(data_format, input_number)


if __name__ == "__main__":
    main()