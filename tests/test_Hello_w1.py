from hello_world import Hello_w0
def sum_mul():
    a = 3
    b = 4
    c = 5
    d = 6
    z = Hello_w0.sum(a,b) + (c * d)
    assert z == 37

print(sum_mul())