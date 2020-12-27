s = input("enter a string ")
I = []
for i in s:
    if i not in I:
        I.append(i)
print("".join(I))
