@profile
def test(s):
    a = s[:]
    b = s[10:-10]
    c = s.split(',')
    return a,b,c

s = '0,' * (1<<20)
test(s)
