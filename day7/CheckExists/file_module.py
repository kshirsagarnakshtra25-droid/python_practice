import os


def check_exists(filename):

    if os.path.exists(filename):
        return True
    else:
        return False