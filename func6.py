# def test1(a):
#     print ("This is my test1")

#     def test2():
#         print("This is my test2")

#     def test3():
#         print("this is my test3")

#     if a == "ris":
#         return test2()
#     elif a== "kumar" :
#         return test3()

# print(test1("ris"))
# print(test1("kumar"))


# # way to execute three function at a time 

# def test4(*args):
#     print ("this is my test4")

# def test5(fun):
#     print("this is test5")
#     def test6():
#         print("Im test6")
#         # fun()
#     return test6()
   

# a = (test5(test4()))
# print(a)


# way to execute function inside function at a time 

def test7():
    print ("this is test7")
    def test8():
        print("this is test8")
        
    return test8()

print(test7())
