from consts import DRIVER, TRIP


def argument_validator(input_list):
    if len(input_list) == 0:
        return False

    for arg in input_list:
        arg_word_list = arg.split()

        try:
            arg_word_list[0] = arg_word_list[0].strip().lower().capitalize()
        except:
            raise Exception('input file is not formatted correctly')

        if arg_word_list[0] != DRIVER and arg_word_list[0] != TRIP:
            return False

    return True
