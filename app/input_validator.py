from consts import DRIVER, TRIP


def argument_validator(input_list):
    for arg in input_list:
        arg_word_list = arg.split()
        arg_word_list[0] = arg_word_list[0].lower().capitalize().strip()

        if arg_word_list[0] != DRIVER and arg_word_list[0] != TRIP:
            return False

    return True
