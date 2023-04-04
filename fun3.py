# Standard way to execute a funtion along with decorator 
# by passing any number of agruments...

def test1(func):
    def test2(*args,**kwargs):
        func(*args,**kwargs)
        print("This is my decorator")
        return func(*args,**kwargs)
    return test2


@test1
def test3(a,b):
    return a+b

a = test3("Rishav","Kumar")
print(a)
print("======================")

@test1
def test4(a=6,b=7):
    return a+ b

print(test4())

