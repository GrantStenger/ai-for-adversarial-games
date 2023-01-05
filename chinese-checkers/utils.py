DEBUG = False


def my_print(*args, **kwargs):
    # my_print is a wrapper for print that only prints if DEBUG is True
    if DEBUG:
        print(*args)
