l = [3,5,5,6,78,"rishav",67.6,"kumar",4,"seth"]
l1 = list()

def test12(l):
    """zzzzzzzzzzzz"""
    for i in l:
        if type(i) == str:
            l1.append(i)
            return l1

li = [3,4,55,"e","4"]
k = test12(li)
print(k)
