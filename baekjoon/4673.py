dif = []
for i in range(10000):
    result = i
    data = list(str(i).rstrip())
    for ele in data:
       result += int(ele)
    dif.append(result)

for j in range(10000):
    if j not in dif:
        print(j)