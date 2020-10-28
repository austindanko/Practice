
lst1 = ["a", "b", "c", "d", "e"]
lst2 = ["d", "e", "f", "f", "f", "g", "h", "h"]
lst3 = []

for x in lst2:
    if x not in lst1:
        lst3.append(x)
#print(lst3)

l_dict = {i:lst3.count(i)
          for i in lst3}
#print(l_dict)

srt_dict = sorted(l_dict.items(), key=lambda x:
                  x[1], reverse=True)
for y in srt_dict:
    print(y[0], y[1])


