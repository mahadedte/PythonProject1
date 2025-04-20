# arithmetic operator +,-,*,%,/
# assignment operator =, ==, +=, -=
# unary operator 1 => -1 , -1 => 1 , [negative to positive , positive to negative]

x = 100
y = 200
print(x + y)
# 300

x1 = 100
x2 = 10
print(x1 / x2)
print(x1 % x2)
# 10.0
# 0

x1 = 10
x2 = 20
print(x1 == x2)
# False

print(x1 > x2)
# False

print(x1 != x2)
# True


# increment decrement
x3 = 10
x3 = x3 + 10
print(x3)

x3 += 50
print(x3)
# 70

x3 -= 20
print(x3)
# 50

#  unary operator
x4 = 10
y4 = -x4
print(y4)

# relational operator
a = 200
b = 400
c = a < b
print(c)
# True
c = a != b
print(c)
# True
# logical operator
a = 10
b = 20
# c = a < b and b < 5
c = a < b < 5
print(c)
# False

a = True
b = not a
print(b)
# False


# conversion
# decimal to binary
a = 55
b = bin(a)
print(b)
# 0b11001

# decimal to octal
x = 45
y = oct(x)
print(y)
# 0o55

# decimal to hex
x = 45
y = hex(x)
print(y)


# 0x2d


#  binary to decimal
def bin_to_dec(str):
    dec = int(str, 2)
    print(dec)


binStr = "110111"
bin_to_dec(binStr)
# 55

# swapping
value1 = 100
value2 = 200
temp = value2
value2 = value1
value1 = temp
print('value1=', value1)
print('value2=', value2)
# value1= 200
# value2= 100


#  using bitwise XOR Operation
a = 5000
b = 10000
a = a ^ b
b = b ^ a
a = a ^ b
print('a=', a)
print('b=', b)
# a= 10000
# b= 5000

# more simplified ways
a, b = b, a
print(a, b)
# 5000 10000
