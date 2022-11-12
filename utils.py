from config import CommonConfig


def print_debug(message):
    if CommonConfig.DEBUG_MODE:
        print(message)
