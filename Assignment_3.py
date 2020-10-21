
lst = ["e1", "e1", "e1", "e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10"]

exp_dict = {x:lst.count(x)
            for x in lst[:5]}
print(exp_dict)

