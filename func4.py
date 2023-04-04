def test1(**kwargs):
    return kwargs
print(test1(a=2,b=3,c=4))
print(test1(a=2,b=3,c=4,ris=[1,2,3,4]))
print(type(test1()))

def test2(**ris):
    return ris
print(test2(a="apple",b = "ball",c= "cat"))