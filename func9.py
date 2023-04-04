import time

def test1(func):
    def test2():
        print("this is my beautiful decorater")
        start = time.time()
        func()
        print(func())
        end = time.time()
        print(f"Time taken to execute this function is : {end-start}")
    return test2

print("????????????????????????????????????????")



@test1
def test3():
    l = [1,2,3,4,4,56,6,7,8,9]
    l1 = []
    for i in l:
        if type(i) == int:
            l1.append(i)
    # print(l1)
    return l1
    

print(test3())
