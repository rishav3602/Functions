def test1(func):
    def test2():
        func()
        print("This is my decorator")
        return func()
    return test2

def test3():
    return 9+3

print(test3())
print("----------------------")


@test1
def test3():
    return 9+3


print(test3())
print(test3()+100)




