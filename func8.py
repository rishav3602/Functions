import os



def test1(fun):
    print("this is my test1")
    def test2():
        print("this is my test2")
        print(os.getcwd())
        fun()
    return test2


# @test1
# def test3 ():
#     print("this is my test3")

# print(test3())

print("---------------------------------------------------")


def test4(func):
    print("this is test4")
    def test5 ():
        func()
        print("this is test5")
    return test5


@test4          
@test1
def test6():
    print("this is my test6")

print(test6())
# print("---------------------------------------------------")


