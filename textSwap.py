with open(r"WhiteHat Projects\C98\content1.txt", 'r') as a:
    data_a = a.read()

with open(r"WhiteHat Projects\C98\content2.txt", 'r') as b:
    data_b = b.read()

print(data_a, data_b)

temp = data_a
data_a = data_b
data_b = temp

with open(r"WhiteHat Projects\C98\content1.txt", 'w') as a:
    a.write(data_a)

with open(r"WhiteHat Projects\C98\content2.txt", 'w') as b:
    b.write(data_b)
