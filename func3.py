d1 = {

    "apple":"seb",
    "mango":"aam",
    "vegetables":{"potato":"aalu","tomato":"tamatar","carrot":"gazar"}

    }

def test1(d):
    l = list()
    for i in d.keys():
        if type(d[i]) == dict:
            l.append(list(d[i].values()))
    return l

print(test1(d1))