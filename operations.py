# Remove Duplicates program
print("Below is for removing duplicates")
s = input("enter a string ")
I = []
for i in s:
    if i not in I:
        I.append(i)
print("".join(I))
############
# Anagrams program
print("Below is for Anagrams")
s1 = "listen"
s2 = "silent"
if (sorted(s1) == sorted(s2)):
    print("Strings are Anagrams ")
else:
    print("Strings are not Anagrams ")
