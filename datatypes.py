'''
Data Types:-
Text Type:	str
Numeric Types   :	int, float, complex
Sequence Types  :	list, tuple, range
Mapping Type    :	dict
Set Types       :	set, frozenset
Boolean Type    :	bool
Binary Types    :	bytes, bytearray, memoryview
'''
# getting the info of vairables
x = 99
y = True
z = 'abc'
a = 10.65
b = '10100abc'
n = 1 - 5j  # for complex numbers only 'j' must be used
print(type(x), type(y), type(z), type(a), type(b), type(n))
# conversion of data types
x = 10  # int
y = 10.5  # float
z = '105'
r = 1 + 2j  # complex
a = complex(y)
b = int(y)
print(b)
k = 'abc'
b = str(int(y)+int(z))+str(k)
c = float(x)
d = complex(x)
print(a, b, c, d)
print(type(a), type(b), type(c), type(d))
