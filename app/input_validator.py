import enum

class ValidArgs(enum.Enum):
   Driver = 'Driver'
   Trip = 'Trip'


def argument_validator(input_list):
    for arg in input_list:
        arg_word_list = arg.split()
        try:
            ValidArgs(arg_word_list[0])
        except:
            return False

    return True
        