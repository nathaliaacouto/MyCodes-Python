#Given two binary strings a and b, return their sum as a binary string.
a = "1010"
b = "1011"
 
x = int(a, 2)

y = int(b, 2)

answer = x + y
binary = format(answer, "b")
bi = str(binary)
print(bi)