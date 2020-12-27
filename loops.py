# using for loop for iteration
x = 10
y = 15
for x in range(0, 5):
    print(y - x)
print('****************')
# using whil loop
x = 1
y = 15
while (y - x == 0):
    if y - x == 0:
        z = y - x
        print(z)
        x += 1
print('****************')
# iterating a loop
for x in range(0, 4):
    x += 1
    for y in range(0, 2):
        y += 1
        print(x, y)
