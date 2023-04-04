c = lambda  a, b : a - b
print(c(2,3))

d = lambda a,b,c,d : a+b-c*d
print(d(2,3,4,5))

e = lambda *args : args
print(e)
print(e(2,3,4,5))