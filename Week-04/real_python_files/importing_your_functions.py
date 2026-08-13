from asdfinput_validators import get_valid_number, get_yes_or_no
import input_validators as iv

if __name__ == '__main__':
    get_valid_number("Please enter a number (int or float): ")
    iv.get_yes_or_no('Do you like this class, yes or no? ')