a=10
b=20

print("a: ", a ,"  b: ",b)

print("After Swapping way 1:")
a,b=b,a
print("a: ", a ,"  b: ",b)

print("After Swapping way 2:")
a=b+a
b=a-b
a=a-b
print("a: ", a ,"  b: ",b)

print("After Swapping way 3:")
a=b*a
b=a//b
a=a//b
print("a: ", a ,"  b: ",b)

print("After Swapping way 4:")
a = a ^ b
b = a ^ b
a = a ^ b
print("a: ", a ,"  b: ",b)
