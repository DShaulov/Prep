myArr = []
print([1, 2, 3] in myArr)
print([2, 1, 3] in myArr)
print({1, 2, 3} == {2, 1, 3})
for i in range(10):
    for j in range(10):
        for k in range(10):
            myArr.append({i, j, k})

print(myArr)