from consts import DRIVER, TRIP

"""
    input_validator.py houses the argument_validator
    method, which verifies if the commands in the input
    are valid or not. Return a boolean. If there is a formatting
    issue, there is an exception thrown.
"""


def argument_validator(content_arg):
    command_array = content_arg.split('\n')

    if len(command_array) == 0:
        return False

    for arg in command_array:
        arg_word_list = arg.split()

        try:
            arg_word_list[0] = arg_word_list[0].strip().lower().capitalize()
        except:
            raise Exception('input file is not formatted correctly')

        if arg_word_list[0] != DRIVER and arg_word_list[0] != TRIP:
            return False

    return True
