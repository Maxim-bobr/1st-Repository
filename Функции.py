def test(a, b):
    return a + b
res = test(7, 3)
print(res)
res2 = test("H", 'i')
print(res2)

smth = lambda x, y, z: x*y*z
res = smth(2, 1, 5)
print(res)
