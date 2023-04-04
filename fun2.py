def test1(func):
    def test2():
        func()
        print("This is my decorator")
        return func()
    return test2

def test3(a,b):
    return a+b


print(test3("ris","kumar"))
print("-----------------")



@test1
def test3(a,b):
    return a+b

# print(test3("ris","kumar")) Will throw an error
print("===================")


def test4(func):
    def test5(c,d):
        func(c,d)
        print("This is my decorator")
        return func(c,d)
    return test5
    
'''


If we are passing any argument in the root
function, then in order the execute the 
function along with the decorator we need to
pass same number of arguments as in the root
function other the program will throw error    


'''


def test6(a,b):
    return a+b

print(test6(9,5))
print("-----------------")


@test4
def test6(a,b):
    return a+b


print(test6(9,5))

