import string

x = list(string.ascii_uppercase)
print(x)

@profile
def test_add():
    s = ''
    for c in x:
        s += c
    return s



@profile
def test_join():
    return ''.join(x)

test_add()
test_join()
