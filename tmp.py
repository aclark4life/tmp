import tempfile


def tmp():
    tmpdir = tempfile.mkdtemp()
    print(tmpdir)
    return tmpdir


if __name__ == '__main__':
    tmp()
