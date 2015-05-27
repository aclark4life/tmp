import tempfile


def print_tmp():
    """
    Print temp dir
    """
    print(tmp())


def tmp():
    """
    Create temp dir
    """
    return tempfile.mkdtemp()


if __name__ == '__main__':
    print_tmp()
