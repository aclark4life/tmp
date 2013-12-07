import tempfile


def tmp():
    print(tempfile.mkdtemp())


if __name__ == '__main__':
    tmp()
